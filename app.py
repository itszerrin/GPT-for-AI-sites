# import all neccessary modules for the server
from flask import Flask, request, jsonify
from flask_cors import CORS
from tiktoken import get_encoding # to count tokens

# import the ai's chattign module
from modules.chat import chat_gen as generate

# load the auth checker (check if key is correct)
from settings.check_auth import check

# ai settings
MODEL = "gpt-3.5-turbo" # defaaaaault
TEMPERATURE = 1 # default setting

# list the list of messages to track the conversation (it's empty at the beginning)
messages: list = [

]

# Configuration
KEY_VALID: bool = False
SERVER_PORT = 3000
DEBUG = False
HOST = '0.0.0.0'

# create the app
app = Flask(__name__)
CORS(app) # handle CORS


@app.route("/chat/completions", methods=["POST"])
async def chat():

    global messages, KEY_VALID, TEMPERATURE, MODEL

    # immediately check if the entered key isn't even valid
    if not KEY_VALID:

        return jsonify({"status": False, "error": "Your API key was incorrect! Enter a valid key!", "type": "Invalid API key"}), 403
    
    # or else we just continue lol
    request_data = request.get_json()
    
    # transfer all messages over to the empty list
    for message in request_data.get("messages", []):

        # make sure we dont get the first non-message entry (which is settings)
        if message["role"] == "system" or "user" or "assistant":

            messages.append(message)

    # create the token encoder
    encoding = get_encoding("cl100k_base")

    # count input tokens (what user wrote)
    input_tokens: int = len(encoding.encode(messages[-1]["content"]))

    # copy the temperature (which can change at each generation)
    TEMPERATURE = request_data.get('temperature', None)
    MODEL = request_data.get('model', None)

    # generate a response
    #api_gen = generate(client, messages, params={"temperature": TEMPERATURE}) ! DEPRACATED !
    api_gen = generate(messages, model=MODEL)

    # count output tokens
    output_tokens: int = len(encoding.encode(messages[-1]["content"]))

    print("Input: ", input_tokens)
    print("Output: ", output_tokens, "\n")

    # wrap the ai's response into json format
    api_response = jsonify({"id": "chatcmpl-abc123", "object": "chat.completion", "created": 1677858242, "model": "NymphGPT", "usage": {"prompt_tokens": input_tokens, "completion_tokens": output_tokens, "total_tokens": input_tokens+output_tokens}, "choices": [{"message": {"role": "assistant", "content": f"\n\n{api_gen}"}, "finish_reason": "stop", "index": 0}]})

    # delete all messages afterwards and create a new list
    messages = []
    
    # return the wrapped response
    return api_response

# handler for model fetching
@app.route("/models")
def root():

    global KEY_VALID

    # get the key the user provided
    authorization_key = request.headers.get("Authorization").replace("Bearer ", "")

    # use the authorization checker file to check if the entered keys is true
    if check("settings\\auth.json", authorization_key):

        # if yes, return the models
        KEY_VALID = True
        return jsonify({"data": [{"id": "gpt-3.5-turbo"}, {"id": "gpt-4-0613"}, {"id": "llama13b-v2-chat"}, {"id": "llama7b-v2-chat"}, {"id": "claude-v2"}, {"id": "claude-instant-v1"}]}), 200
    
    else:

        KEY_VALID = False
        return jsonify({"status": False, "error": "Invalid API key entered"}), 403

# run the code and host the server lol
if __name__ == "__main__":

    app.run(port=SERVER_PORT, debug=DEBUG, host=HOST)

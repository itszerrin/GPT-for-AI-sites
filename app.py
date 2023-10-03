# import all neccessary modules for the server
from flask import Flask, request, jsonify
from flask_cors import CORS
from tiktoken import get_encoding # to count tokens

# import the ai's chatting modules
from modules.client import newClient
from modules.chat import chat_gen as generate

# create an Ai client
client = newClient(proxy=None)

# ai settings and a bunch of default variables
MODEL = "replicate:replicate/llama-2-70b-chat" 
TEMPERATURE = 1 
FREQUENCY_PENALTY = 0.85
PRESENCE_PENALTY = 0.85
MAX_TOKENS = 1000

# list the list of messages to track the conversation (it's empty at the beginning)
messages: list = [

]

# Configuration
SERVER_PORT = 3000
DEBUG = False
HOST = '0.0.0.0'

# create the app
app = Flask(__name__)
CORS(app) # handle CORS

@app.route("/chat/completions", methods=["POST"])
async def chat():

    global messages, TEMPERATURE, MODEL, FREQUENCY_PENALTY, PRESENCE_PENALTY, MAX_TOKENS
    
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

    # get new versions of each parameter (they might change at each prompt, lol)
    TEMPERATURE = request_data.get('temperature', None)
    MODEL = request_data.get('model', None)
    FREQUENCY_PENALTY = request_data.get('frequency_penalty', None)
    PRESENCE_PENALTY = request_data.get('presence_penalty', None)
    MAX_TOKENS = request_data.get('max_tokens', None)

    # generate a response
    api_gen = generate(client, messages, params={"temperature": TEMPERATURE, "maximumLength": MAX_TOKENS, "max_tokens": MAX_TOKENS, "presencePenalty": PRESENCE_PENALTY, "frequencyPenalty": FREQUENCY_PENALTY})

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

    # return a list of our models
    return jsonify(
    {"data": [
        {"id": "openai:gpt-3.5-turbo"},
        {"id": "openai:gpt-3.5-turbo-16k-0613"},
        {"id": "openai:gpt-3.5-turbo-16k"},
        {"id": "cohere:command-nightly"}, 
        {"id": "huggingface:bigcode/santacoder"}, 
        {"id": "huggingface:OpenAssistant/oasst-sft-1-pythia-12b"}, 
        {"id": "huggingface:OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5"}, 
        {"id": "huggingface:EleutherAI/gpt-neox-20b"},
        {"id": "replicate:a16z-infra/llama7b-v2-chat"},
        {"id": "replicate:a16z-infra/llama13b-v2-chat"},
        {"id": "replicate:replicate/llama-2-70b-chat"},
        {"id": "huggingface:bigscience/bloom"},
        {"id": "openai:text-davinci-003"},
        {"id": "huggingface:google/flan-t5-xxl"},
    ]}), 200

# run the code and host the server lol
if __name__ == "__main__":

    app.run(port=SERVER_PORT, debug=DEBUG, host=HOST)

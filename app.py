# import all neccessary modules for the server
from flask import Flask, request, jsonify
from flask_cors import CORS

# import the ai's chatting modules
from modules.client import newClient
from modules.chat import chat_gen as generate

# get the modules to count tokens
from modules.tokens.create_encoding import create_encoder
from modules.tokens.token_counter import count_tokens

# import the model switcher module 
from modules.conv.janitorai import switch_models

# ai settings and a bunch of default variables
MODEL = "openai:gpt-3.5-turbo" 
TEMPERATURE = 1 
FREQUENCY_PENALTY = 0.85
PRESENCE_PENALTY = 0.85
MAX_TOKENS = 600

# list the list of messages to track the conversation (it's empty at the beginning)
messages: list = [

]

# Configuration
SERVER_PORT = 3000
DEBUG = True
HOST = '0.0.0.0'

# create a token encoder (to convert strings to token counts, aka int))
encoding = create_encoder()

# create the app
app = Flask(__name__)
CORS(app) # handle CORS

@app.route("/chat/completions", methods=["POST"])
def chat():

    global messages

    # create a new random client
    client = newClient()
    
    # get the request data which was also sent over by the site
    request_data = request.get_json()

    # get new versions of each parameter (they might change at each prompt, lol)
    TEMPERATURE = request_data.get('temperature', None)
    MODEL = request_data.get('model', None)
    FREQUENCY_PENALTY = request_data.get('frequency_penalty', None)
    PRESENCE_PENALTY = request_data.get('presence_penalty', None)
    MAX_TOKENS = request_data.get('max_tokens', None)

    # check if we need to convert model name first for janitorai support
    if "openai" not in MODEL:   MODEL=switch_models(MODEL)
    
    # transfer all messages over to the empty list
    for message in request_data.get("messages", []):

        messages.append(message)


    # count input tokens (what user wrote)
    input_tokens: int = count_tokens(encoding, messages[-1]["content"])

    # generate a response
    api_gen = generate(client, messages, model=MODEL, params={"temperature": TEMPERATURE, "maxTokens": MAX_TOKENS, "presencePenalty": PRESENCE_PENALTY, "frequencyPenalty": FREQUENCY_PENALTY})

    # count output tokens
    output_tokens: int = count_tokens(encoding, messages[-1]["content"])

    print("Input: ", input_tokens)
    print("Output: ", output_tokens, "\n")

    # wrap the ai's response into json format
    api_response = jsonify({"id": "chatcmpl-abc123", "object": "chat.completion", "created": 1677858242, "model": f"{MODEL}", "usage": {"prompt_tokens": input_tokens, "completion_tokens": output_tokens, "total_tokens": input_tokens+output_tokens}, "choices": [{"message": {"role": "assistant", "content": f"{api_gen}"}, "finish_reason": "stop", "index": 0}]})

    # delete all messages afterwards and create a new list
    messages = []
    
    # return the wrapped response
    return api_response

# handler for model fetching
@app.route("/models")
def models():

    # return a list of our models
    return jsonify(
    {"data": [
        {"id": "openai:gpt-3.5-turbo"},
        {"id": "openai:gpt-3.5-turbo-16k-0613"},
        {"id": "openai:gpt-3.5-turbo-16k"},
        #{"id": "openai:llama-2-70"},
        #{"id": "cohere:command-nightly"}, 
        #{"id": "huggingface:bigcode/santacoder"}, 
        #{"id": "huggingface:OpenAssistant/oasst-sft-1-pythia-12b"}, 
        #{"id": "huggingface:OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5"}, 
        #{"id": "huggingface:EleutherAI/gpt-neox-20b"},
        #{"id": "replicate:a16z-infra/llama7b-v2-chat"},
       # {"id": "replicate:a16z-infra/llama13b-v2-chat"},
        #{"id": "replicate:a16z-infra/llama70b-v2-chat"},
        #{"id": "huggingface:bigscience/bloom"},
        #{"id": "openai:text-davinci-003"},
        #{"id": "huggingface:google/flan-t5-xxl"},
    ]}), 200

# the root (for google colab)
@app.route("/")
def root():

    global MODEL, messages

    return f"<h1>Your generated link works.<h1><br><br><h2>Your selected model is: {MODEL} and a total {len(messages} messages were sent"

# run the code and host the server lol
if __name__ == "__main__":

    app.run(port=SERVER_PORT, debug=DEBUG, host=HOST)

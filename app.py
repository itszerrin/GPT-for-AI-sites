# import all neccessary modules for the server
from flask import Flask, request, jsonify, Response, make_response
from flask_cors import CORS

# import the ai's chatting modules
from modules.chat import chat_gen as generate
from modules.chat import stream as stream

# get the modules to count tokens
from modules.tokens.create_encoding import create_encoder
from modules.tokens.token_counter import count_tokens

# import converion module (to convert messages to strings)
from modules.transform.msg_to_str import msg_to_str

# import the global server host from cloudflare
from flask_cloudflared import run_with_cloudflared

# logging module to keep track of info
import logging

# time module (to delay execution)
import time

# ai settings and a bunch of default variables
MODEL = "gpt-3.5-turbo" 
TEMPERATURE = 1 
FREQUENCY_PENALTY = 0.85
PRESENCE_PENALTY = 0.85
MAX_TOKENS = 600
TOP_P: int = 1

# list the list of messages to track the conversation (it's empty at the beginning)
messages: list = [

]

# Configuration
SERVER_PORT = 5000
DEBUG = False
HOST = '0.0.0.0'

# create a token encoder (to convert strings to token counts, aka int))
encoding = create_encoder()

# create the app
app = Flask(__name__)
CORS(app) # handle CORS

# create a new logger and configure it
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# method for chat completions
@app.route("/chat/completions", methods=["POST"])
def chat():

    # make the messages accessible in a bigger scope
    global messages

    def streaming():

        logger.info("\nStreaming requested...\n")

        while True:

            try:

                for chunk in stream(MODEL, messages, params):

                    yield b'data: ' + str((chunk)).encode() + b'\n\n'

                break

            except Exception as e:

                logger.error(f"Error occurred: {str(e)}")
                time.sleep(1)
                continue

        yield b'data: [DONE]'

    # get the request data which was also sent over by the site
    request_data = request.get_json()

    # get new versions of each parameter (they might change at each prompt, lol)
    TEMPERATURE = request_data.get('temperature', None)
    MODEL = request_data.get('model', None)
    FREQUENCY_PENALTY = request_data.get('frequency_penalty', None)
    PRESENCE_PENALTY = request_data.get('presence_penalty', None)
    MAX_TOKENS = request_data.get('max_tokens', None)
    TOP_P = request_data.get('top_p', None)

    # compile parameters to a dict
    params: dict = {"temperature": TEMPERATURE, "frequency_penalty": FREQUENCY_PENALTY, "presence_penalty": PRESENCE_PENALTY, "max_tokens": MAX_TOKENS, "top_p": TOP_P}

    # transfer all messages over to the empty list
    for message in request_data.get("messages", []):

        messages.append(message)

    # count input tokens (what user wrote)
    input_tokens: int = count_tokens(encoding, messages[-1]["content"])

    # generate a response
    if request_data.get("stream", None) == False:

        generate(MODEL, messages, params)

    else:

        return Response(streaming(), mimetype='text/event-stream')

    # count output tokens
    output_tokens: int = count_tokens(encoding, messages[-1]["content"])

    # calculate total tokens
    total_tokens: int = input_tokens + output_tokens

    # log (for developing purposes)
    logger.info(f"\n\nModel: {MODEL}\nPrompt: {input_tokens}\nTotal Input: {count_tokens(encoding, msg_to_str(messages))}\nOutput: {output_tokens}\nTemperature: {TEMPERATURE}\nFrequency Penalty: {FREQUENCY_PENALTY}\nPresence Penalty: {PRESENCE_PENALTY}\nTop P: {TOP_P}\n")

    # wrap the ai's response into a generic json format
    api_response = jsonify(
        {"id": "chatcmpl-abc123",
         "object": "chat.completion",
         "created": 1677858242,
         "model": f"{MODEL}",
         "usage":
          {
           "prompt_tokens":
             input_tokens,
           "completion_tokens":
             output_tokens,
           "total_tokens":
             total_tokens
          },
         "choices": [
             {
              "message": messages[-1],
              "finish_reason": "stop",
              "index": 0
             }
         ]
        }
    ), 200

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

        {"id": "gpt-4"},
        {"id": "gpt-3.5-turbo"},
        {"id": "gpt-3.5-turbo-16k"},
    ]}), 200

# the root (for google colab, not needed to access)
@app.route("/")
def root():

    # return a string if the link does work
    return "<h1>Your generated link works. Use it as a reverse proxy.</h1>"

# run the code and host the server lol
if __name__ == "__main__":

    run_with_cloudflared(app)
    app.run(port=SERVER_PORT, debug=DEBUG, host=HOST)

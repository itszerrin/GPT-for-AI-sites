# only necessary imports
from g4f import ChatCompletion, Provider

# to convert and read from json
import json

import logging

# generative, doesn't print
def chat_gen(model: str, messages: list, params: dict = {"temperature": 0.7, "top_p": 1, "frequency_penalty": 0, "presence_penalty": 0}) -> str:

    
    # try statement due to a common error
    try:
        
        # send a request to the api
        response = ChatCompletion.create(
            model=model,
            messages=messages,
            stream=False,

            temperature=params["temperature"],
            top_p=params["top_p"],
            frequency_penalty=params["frequency_penalty"],
            presence_penalty=params["presence_penalty"]
        )

    # common issues (brute-forcing a response usually works)
    except:

        logging.error("An error occured, retrying")
        return chat_gen(model, messages)


    # add the ai's response to the current list of messages
    messages.append({"role": "assistant", "content": f"{response}"})

    # return the generated response
    return response

# streaming, generative
def stream(model: str, messages: list, params: dict = {"temperature": 0.7, "top_p": 1, "frequency_penalty": 0, "presence_penalty": 0}) -> str:

    # try statement due to a common error
    try:
        
        # send a request to the api
        response = ChatCompletion.create(
            model=model,
            messages=messages,
            stream=True,

            temperature=params["temperature"],
            top_p=params["top_p"],
            frequency_penalty=params["frequency_penalty"],
            presence_penalty=params["presence_penalty"]
        )

    # common issues (brute-forcing a response usually works)
    except:

        logging.error("An error occured, retrying")
        return stream(model, messages)

    # add the ai's response to the current list of messages
    messages.append({"role": "assistant", "content": f"{response}"})

    # iter through the chunks
    for chunk in response:

        # return the response in generic openai format
        yield json.dumps({
            "id": "chatcmpl-abc123",
            "object": "chat.completion.chunk",
            "created": 1677858242,
            "model": f"{model}",
            "system_fingerprint": None,
            "choices": [
                {
                    "index": 0,
                    "delta": {
                        "content": f"{chunk}",
                    },
                    "finish_reason": None,
                }
            ]
        })

    # once we're done with all chunks, return an empty one to signal end
    yield json.dumps({
        "id": "chatcmpl-abc123",
        "object": "chat.completion.chunk",
        "created": 1677858242,
        "model": f"{model}",
        "system_fingerprint": None,
        "choices": [
            {
                "index": 0,
                "delta": {},
                "finish_reason": "stop",
            }
        ]
    })





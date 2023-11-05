# only necessary imports
from g4f import ChatCompletion

# generative, doesn't print
def chat_gen(model: str, messages: list) -> str:

    # send a request to the api
    response = ChatCompletion.create(
        model=model,
        messages=messages,
        stream=False, # streaming support coming soon
    )

    # add the ai's response to the current list of messages
    messages.append({"role": "assistant", "content": f"{response}"})

    # return the generated response
    return response







# only necessary imports
from g4f import ChatCompletion, Provider

# generative, doesn't print
def chat_gen(model: str, messages: list) -> str:

    
    # try statement due to a common error
    try:
        
        # send a request to the api
        response = ChatCompletion.create(
            model=model,
            messages=messages,
            provider=Provider.Bing,
            cookies={"Fake": ""},
            stream=False, # streaming support coming soon
        )

    # common issue with gpt-3.5-turbo-16k model
    except RuntimeError:

        return chat_gen(model, messages)

    # add the ai's response to the current list of messages
    messages.append({"role": "assistant", "content": f"{response}"})

    # return the generated response
    return response







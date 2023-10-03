# only necessary imports
from vercel_ai import Client
from curl_cffi.requests.errors import RequestsError

def chat(client: Client, messages: list, model: str = "openai:gpt-3.5-turbo", params: dict = {"temperature": 0.8}) -> None:

    response: str = ""

    try:

        for chunk in client.chat(model, messages, params):

            # just make sure we dont process the returned error lol
            if chunk != 'Internal Server Error':

                response += chunk
                print(chunk, end="", flush=True)

        # append the ai's response to the message list
        messages.append({'role': 'assistant', 'content': f'{response}'})

    # error-driven recursive call
    except RequestsError:

        chat(client, messages, params=params, model=model)

# generative, doesn't print
def chat_gen(client: Client, messages: list, model: str = "openai:gpt-3.5-turbo", params: dict = {"temperature": 0.8}) -> str:

    response: str = ""

    try:

        for chunk in client.chat(model, messages, params):

            # just make sure we dont process the returned error lol
            if chunk != 'Internal Server Error':

                response += chunk

        # append the ai's response to the message list
        messages.append({'role': 'assistant', 'content': f'{response}'})
    
        return response

    # error-driven recursive call
    except RequestsError:

        return chat_gen(client, messages, params=params, model=model)





# only necessary imports
from vercel_ai import Client
from curl_cffi.requests.errors import RequestsError

from json import dumps

# generative, doesn't print
def chat_gen(client: Client, messages: list, model: str = "openai:gpt-3.5-turbo", params: dict = {"temperature": 0.8, "maxTokens": 500}) -> str:

    response: str = ""

    try:

        for chunk in client.chat(model, messages, params):

            # just make sure we dont process the returned error lol
            if chunk != 'Internal Server Error':
            
                if "help.openai.com" not in chunk:

                    response += chunk

                else:

                    return chat_gen(Client(client.proxy), messages, model, params)

                
                # check if we're rate limited :sad_face_
                #print(f"\n{chunk}\n")

        # append the ai's response to the message list
        messages.append({'role': 'assistant', 'content': f'{response}'})
    
        return response

    # error-driven recursive call
    except RequestsError:

        return chat_gen(client, messages, params=params, model=model)





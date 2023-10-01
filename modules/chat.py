from g4f import ChatCompletion # import the completions module

from requests.exceptions import HTTPError

# import the async module to configure it later on
from asyncio import set_event_loop_policy, WindowsSelectorEventLoopPolicy

# some setup so asyncio doesnt give a warning
set_event_loop_policy(WindowsSelectorEventLoopPolicy())

# function to generate a response to a current list of messages
def chat_gen(messages: list, model: str = "gpt-3.5-turbo") -> str:

    try:

        # generate a response
        response: str = ChatCompletion.create(
            model=model,
            messages=messages,
        )

        # add the response to the list of messages
        messages.append({"role": "assistant", "content": f"{response}"})

        # return the response
        return response
    
    # common error: error 500. unpreventable from our side and an error on the host's end.
    # thats why we're recursively going to retry (aka brute) our way to a response
    except HTTPError:

        return chat_gen(messages, model)
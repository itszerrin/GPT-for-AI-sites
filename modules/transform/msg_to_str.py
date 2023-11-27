# this function takes a list of messages and converts it to a string (to make it convertable to tokens)
def msg_to_str(messages: list) -> str:
    
    # create an empty string
    string = ""
    
    # iterate over the messages
    for message in messages:
        
        # add the message to the string
        string += f"{message['content']} "
    
    # return the string
    return string
from tiktoken import Encoding

# function which counts tokens
def count_tokens(encoding: Encoding, text: str):

    # returns an int
    return len(encoding.encode(text))
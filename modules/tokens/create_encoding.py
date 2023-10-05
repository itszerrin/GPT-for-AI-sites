from tiktoken import get_encoding

# function which returns an encoder-capable entity
def create_encoder(base: str = "cl100k_base"):

    return get_encoding(base)
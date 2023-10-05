from vercel_ai import Client

# function to create a new client for generation
def newClient(proxy: str = None) -> Client:

    #return Client(proxy=proxy)
    return Client(proxy)


from .core import GFModel

_client = GFModel()

def __getattr__(name):
    return getattr(_client, name)

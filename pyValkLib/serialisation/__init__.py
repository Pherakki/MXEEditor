if (__name__ == "__main__"):
    from ReadWriter import Reader, Writer
    from Serializable import Serializable
else:
    from .ReadWriter import Reader, Writer
    from .Serializable import Serializable

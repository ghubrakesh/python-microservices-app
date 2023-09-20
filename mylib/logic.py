import wikipedia


def wiki(name, length):
    """This is wiki fetcher"""

    my_wiki = wikipedia.summary(name, sentences=length)
    return my_wiki

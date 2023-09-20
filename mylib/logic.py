import wikipedia


def wiki(name="wondder woman", length=2):
    """This is wiki fetcher"""

    my_wiki = wikipedia.summary(name, sentences=length)
    return my_wiki

import wikipedia

def search_wiki(query):
    """get search query results (page ids)"""
    my_wiki = wikipedia.search(query)
    return my_wiki

def wiki(name="wondder woman", length=2):
    """This is wiki fetcher"""
    my_wiki = wikipedia.summary(name, sentences=length)
    return my_wiki
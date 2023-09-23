import wikipedia
from textblob import TextBlob


def search_wiki(query):
    """get search query results (page ids)"""
    my_wiki = wikipedia.search(query)
    return my_wiki


def wiki(name="wondder woman", length=5):
    """This is wiki fetcher"""
    my_wiki = wikipedia.summary(name, sentences=length)
    return my_wiki


def phrase(name):
    """returns phrases from wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases

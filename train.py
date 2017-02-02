#!/usr/bin/env python2
import gensim
import itertools
from gensim.utils import smart_open, simple_preprocess
from gensim.corpora.wikicorpus import _extract_pages, filter_wiki
from gensim.parsing.preprocessing import STOPWORDS
import sys

def tokenize(text):
    return [token for token in simple_preprocess(text) if token not in STOPWORDS]

def iter_wiki(dump_file):
    """Yield each article from the Wikipedia dump, as a `(title, tokens)` 2-tuple."""
    ignore_namespaces = 'Wikipedia Category File Portal Template MediaWiki User Help Book Draft'.split()
    for title, text, pageid in _extract_pages(smart_open(dump_file)):
        text = filter_wiki(text)
        tokens = tokenize(text)
        if len(tokens) < 50 or any(title.startswith(ns + ':') for ns in ignore_namespaces):
            continue  # ignore short articles and various meta-articles
        yield title, tokens

corpuses=sys.argv[1:]

class WikiCorpus(object):
    def __init__(self, dump_file, dictionary=None):
        self.dump_file = dump_file
        if not dictionary:
            self.dictionary = gensim.corpora.Dictionary()
            for df in self.dump_file:
                ts = []
                for title, tokens in iter_wiki(df):
                    ts.append(tokens)
                self.dictionary.add_documents(ts)
            self.dictionary.filter_extremes(no_below=20, no_above=0.1)
        else:
            self.dictionary = dictionary

    def __iter__(self):
        for df in self.dump_file:
            for title, tokens in iter_wiki(df):
                yield self.dictionary.doc2bow(tokens)

wiki_corpus = WikiCorpus(corpuses)#, id2word_wiki)

tfidf_model = gensim.models.TfidfModel(wiki_corpus, id2word=wiki_corpus.dictionary)
tfidf_model.save('./tfidf_wiki.model')


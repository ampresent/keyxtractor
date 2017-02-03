import gensim
from gensim.utils import smart_open, simple_preprocess
import logging
from operator import itemgetter
from gensim.parsing.preprocessing import STOPWORDS
import re

gensim.utils.PAT_ALPHABETIC = re.compile('(((?![\d])[\w-])+)', re.UNICODE)

def tokenize(text):
    return [token for token in simple_preprocess(text) if token not in STOPWORDS]

logging.getLogger().setLevel(logging.DEBUG)

class Extractor(object):
    
    def extract(self, text, top=None, ratio=0.1):
        try:
            logging.info('Creating bag of words.')
            bow = self.dic.doc2bow(tokenize(text))
            logging.debug('bow: '+str(bow))
            logging.info('Running TFIDF model.')
            if top is None:
                top = int(len(bow) * ratio)
            logging.debug('top: '+str(top))
            if top < 0:
                keyid = sorted(self.tfidf[bow], key=itemgetter(1), reverse=True)
            else:
                keyid = sorted(self.tfidf[bow], key=itemgetter(1), reverse=True)[:top]
            logging.debug('keyid: '+str(keyid))
            logging.info('Retrieving keywords from ids.')
            kws = [self.dic[i[0]] for i in keyid]
            logging.debug('kws: {} ...'.format(kws))
            return kws

        except Exception, e:
            logging.error('Failed to extract: {}\n\t{}...'.format(str(e), text[:50])) 
            return []

    def __init__(self):
        try:
            logging.info('Loading pre-trained TFIDF model.')
            self.tfidf = gensim.models.tfidfmodel.TfidfModel.load('./tfidf_wiki.model')
            logging.debug('tfidf: '+str(self.tfidf))
            logging.info('Loading dictionary.')
            self.dic = gensim.corpora.dictionary.Dictionary.load('./wiki.dic')
        except Exception, e:
            logging.error('Failed to initialize TFIDF model: {}'.format(str(e)))
            raise e

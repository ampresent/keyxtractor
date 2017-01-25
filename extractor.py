import gensim
import pdb
from gensim.utils import tokenize, smart_open
import logging
from operator import itemgetter

logging.getLogger().setLevel(logging.DEBUG)

def group_lines(text, step):
    l = len(text)
    # Start of paragraph
    i = 0
    # End of paragraph
    i2= i
    while i < l and i >= 0:
        for s in range(step):
            # Previous line
            i1 = i2
            i2 = text.find("\n", i1)
            if i2 < 0:
                break
            while i2 < l and (text[i2] == '\n' or text[i2] == ' ' or text[i2] == '\t'):
                i2 += 1
        if i2 < 0:
            yield text[i:]
        else:
            yield text[i:i2]
        i = i2

def merge(a, b):
    for k,v in b:
        if k in a:
            a[k] += v
        else:
            a[k] = v

class Extractor(object):

    def extract(self, orig_text, top=None, ratio=0.1):
        try:
            keyid = {}
            for text in group_lines(orig_text, 8):
                logging.info('Creating bag of words.')
                bow = self.dic.doc2bow(tokenize(text))
                if len(bow) < 10:
                    logging.info('Paragraph has too little words')
                    continue
                logging.debug('bow: '+str(bow))
                logging.info('Running TFIDF model.')
                if top is None:
                    top = int(len(bow) * ratio)
                logging.debug('top: '+str(top))
                merge(keyid, self.tfidf[bow])
            if top < 0:
                keyid = sorted(keyid.iteritems(), key=itemgetter(1), reverse=True)
            else:
                keyid = sorted(keyid.iteritems(), key=itemgetter(1), reverse=True)[:top]
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

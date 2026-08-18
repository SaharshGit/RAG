from math import log

from .preprocess import preprocess
from .models import DocumentPage
class TFIDF:

    def _term_frequency(self,
                       tokens: list[str],
                       )-> dict[str,int]:
        word_freq = {}
        
        for token in tokens:
            if token in word_freq:
                word_freq[token] += 1

            else:
                word_freq[token] = 1 

        return word_freq
    
    def normalized_term_frequency(self, tokens) ->  dict[str,float]:
        total_tokens = len(tokens)

        normalized_word_freq = {}
        word_freq = self._term_frequency(tokens)

        for word,count in word_freq.items():
             normalized_word_freq[word] = count/total_tokens

        return normalized_word_freq


    def _document_frequency(self,
                           pages: list[DocumentPage],
                           ) ->  dict[str, int]:

        document_frequency = {}

        for page in pages:

            tokens = preprocess(page.text)

            unique_words = set(tokens)

            for word in unique_words:
                if word not in document_frequency:
                    document_frequency[word] = 1
                else:
                    document_frequency[word] += 1

        return document_frequency

    def inverse_document_frequency(self,
                                   pages: list[DocumentPage],
                                   ) -> dict[str, float]:

        document_frequency = self._document_frequency(pages)

        total_documents = len(pages)

        idf={}

        for word, df in document_frequency.items():
            idf[word] = log(total_documents / df)

        return idf

    def tfidf(
            self,
            tokens: list[str],
            idf: dict[str,float],


    ) -> dict[str,float]:

        tf = self.normalized_term_frequency(tokens)
        tfidf_scores = {}

        for term, freq in tf.items():
            tfidf_scores[term] = freq*idf.get(term, 0.0)

        return tfidf_scores
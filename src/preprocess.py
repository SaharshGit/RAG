import re

from nltk.corpus import stopwords


stop_words = set(stopwords.words("english"))



def preprocess(text:str) -> list[str]:


        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", "",text)
        text_tokens = [token for token in text.split() if token not in stop_words] 

        return text_tokens

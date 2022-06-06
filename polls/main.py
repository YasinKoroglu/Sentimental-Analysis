import nltk
from django.core.files.storage import FileSystemStorage



nltk.download([
 "names",
"stopwords",
 "state_union",
"twitter_samples",
 "movie_reviews",
    "averaged_perceptron_tagger",
    "vader_lexicon",
  "punkt",
])
with open('./media/EX.txt','r') as file:
    countriesStr = file.read()

words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]  #alpha --> true döndürür. Stateunion --> büyük harfle ayırır.

stopwords = nltk.corpus.stopwords.words("english") #stopwords --> en common kelimeler

words = [w for w in words if w.lower() not in stopwords]


from pprint import pprint



text = countriesStr

pprint(nltk.word_tokenize(text)) # word_tokenize --> cümleyi kelemelere böler

selam = nltk.word_tokenize(text)

analysis=[w for w in selam if w.lower() not in stopwords]

fd = nltk.FreqDist(analysis)


fd.most_common(10)


# parantez içini words yapıp çalıştırınca kelime alıyorum ama şu an harf alıyorum çözemedim bi türlü NLTK kütüphanesi olarak bakabilirsin
text = nltk.Text(analysis)


fd.tabulate(10)



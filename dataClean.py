from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
file_content = open("tweets_faced.txt").read()
tokens = word_tokenize(file_content)
tokensDist = FreqDist(w.lower() for w in tokens)

stop_words = stopwords.words('english')
stop_words.append(':')
stop_words.append('#')
stop_words.append('@')
stop_words.append(',')
stop_words.append('.')
stop_words.append('https')
stop_words.append('i')
stop_words.append('\'')
stop_words.append('\'s')
stop_words.append('the')
stop_words.append('`')
stop_words.append('\"')
stop_words.append('?')
stop_words.append('!')
stop_words.append('i')
stop_words.append('’')
stop_words.append('the')
stop_words.append('”')
stop_words.append('“')
stop_words.append('``')
stop_words.append('the')
stop_words.append('it')
stop_words.append('a')
stop_words.append(';')
stop_words.append('RT')
stop_words.append('co')
stop_words.append('CO')

allWordsExcept = FreqDist(w.lower() for w in tokens if w not in stop_words)

mostCommon = allWordsExcept.most_common(20)
print("fuck: ", mostCommon.get('fuck'))

wordcloud = WordCloud(stopwords = stop_words, background_color = "white").generate(file_content)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


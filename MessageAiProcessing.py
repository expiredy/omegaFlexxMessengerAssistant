import nltk
from pprint import pprint
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

written_text_by_user = input()

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

# Разделяем на слова (токенизируем)
pprint(nltk.word_tokenize(written_text_by_user), width=79, compact=True)
written_text_by_user = nltk.word_tokenize(written_text_by_user)

# Удаляем stop words
filtered_written_text_by_user = [word for word in written_text_by_user if word not in stopwords.words('english')]
print(filtered_written_text_by_user)

# Обратно делаем единый текст
filtered_written_text_by_user = " ".join(filtered_written_text_by_user)

# Модель предсказывания
sia = SentimentIntensityAnalyzer()
results = sia.polarity_scores(filtered_written_text_by_user)
print(results)
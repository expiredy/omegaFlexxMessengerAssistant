import nltk
from pprint import pprint
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

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


def get_messege_processing_info(written_text_by_user: str, written_text_by_user_for_connection: dict) -> tuple:
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
    results_for_connection = sia.polarity_scores(written_text_by_user_for_connection)
    results_for_karma = sia.polarity_scores(filtered_written_text_by_user)
    negative_res = results_for_karma['neg']

    positive_res = results_for_karma['pos']

    neutral_res = results_for_karma['neu']

    connection_res = results_for_connection['compound']

    return negative_res, positive_res, neutral_res, connection_res

from AiProcessors import MessageAiProcessing
from DictKeyConfig import *


list_of_fricking_shit = ["You are dumb ass",
                         "You are sucking my dick every day",
                         "Hope your mom is healthy",
                         "I hate you",
                         "You hate me",
                         "You are stupid bitch",
                         "Stupido",
                         "I fucked your mom",
                         "Stupid",
                         "Dumb"]


def get_decorated_data_from_ai(sentence_for_analyze: str) -> str:
    data = MessageAiProcessing.get_messege_processing_info(sentence_for_analyze, sentence_for_analyze)
    param_name_keys = [NEGATIVE_COEFFICIENT_KEY,
                       POSITIVE_COEFFICIENT_KEY,
                       NEUTRAL_COEFFICIENT_KEY,
                       CONNECTION_COEFFICIENT_KEY]
    return "\n".join([key + ": " + str(data[key]) for key in param_name_keys])


for sentence in list_of_fricking_shit:
    print(sentence + ":\n" + get_decorated_data_from_ai(sentence))
    print()

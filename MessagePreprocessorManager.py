from DictKeyConfig import *
import MessageAiProcessing
UPPER_KARMA_LIMITER = 5
LOWER_KARMA_LIMITER = -5
BINARY_PARAMS_CONVERTOR = {POSITIVE_COEFFICIENT_KEY: (),
                           NEGATIVE_COEFFICIENT_KEY: (),
                           NEUTRAL_COEFFICIENT_KEY: (),
                           CONNECTION_COEFFICIENT_KEY: ()
                           }


def convert_ai_data(parameter_key: str, param: float) -> str:

    return ""


def message_preprocessor(message_text: str, chat_messages_data_dict: dict) -> dict:
    previews_karma_counter = MessageAiProcessing.get_messege_processing_info(message_text, chat_messages_data_dict)
    return dict()

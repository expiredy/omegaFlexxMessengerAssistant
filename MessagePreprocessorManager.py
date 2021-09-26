from DictKeyConfig import *
import MessageAiProcessing
UPPER_KARMA_LIMITER = 5
LOWER_KARMA_LIMITER = -5


def message_preprocessor(message_text: str, chat_messages_data_dict: dict):

    previews_karma_counter = MessageAiProcessing.get_messege_processing_info(message_text, chat_messages_data_dict)

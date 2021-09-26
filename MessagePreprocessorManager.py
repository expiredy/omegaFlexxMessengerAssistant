from DictKeyConfig import *
import MessageAiProcessing
UPPER_KARMA_LIMITER = 5
LOWER_KARMA_LIMITER = -5


def message_preprocessor(message_text: str, chat_messages_data_dict: dict):

    def get_chat_history_karma(chat_information_dict: dict) -> float:
        for id_of_message in (chat_information_dict.keys()):
            pass
        return 0.0

    def get_message_analyzed_by_ai_info(text_for_processing: str, user_karma_count: int) -> dict:
        pass

    previews_karma_counter = get_chat_history_karma(chat_messages_data_dict)

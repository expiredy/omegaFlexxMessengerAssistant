from DictKeyConfig import *
from AiProcessors import MessageAiProcessing

BINARY_PARAMS_CONVERTOR_PARAMS = {POSITIVE_COEFFICIENT_KEY: (),
                                  NEGATIVE_COEFFICIENT_KEY: (),
                                  NEUTRAL_COEFFICIENT_KEY: (),
                                  CONNECTION_COEFFICIENT_KEY: ()
                                  }

USERS_MODES_PARAMS_MULTIPLIERS = {CUTIE_MODE_ID: ((-1, -0.25), (-0.25, 0), (0, 0), (0, 0.25), (0.25, 1)),
                                  AVERAGE_MODE_ID: ((-1, -0.5), (-0.5, 0), (0, 0), (0, 0.5), (0.5, 1)),
                                  MORGENSHTERN_MODE_ID: ((-1, -0.75), (-0.75, 0), (0, 0), (0, 0.75), (0.75, 1))}

KARMA_SCORE_CONSTANTS = (2, 1, 0, -1, -2)


class ServerCallbackAnswer():
    callback_data = {}
    DEFAULT_KARMA_SCORE_INDEX = 0

    def __init__(self, neural_data_dict: dict, user_mode_id: int):
        self.callback_data = {}
        negative_coef = neural_data_dict[NEGATIVE_COEFFICIENT_KEY]
        neutral_coef = neural_data_dict[NEUTRAL_COEFFICIENT_KEY]
        self.compound_coef = neural_data_dict[CONNECTION_COEFFICIENT_KEY]
        analyze_weights = USERS_MODES_PARAMS_MULTIPLIERS[user_mode_id]
        self.karma_score_index = self.get_karma_score_index(negative_coef,
                                                            neutral_coef,
                                                            analyze_weights)
        self.karma_score = KARMA_SCORE_CONSTANTS[self.karma_score_index]

    def get_final_answer(self):
        return self.karma_score, self.karma_score_index

    def get_karma_score_index(self, negative: int, neutral: int, weights: tuple):
        for karma_score_index in range(len(weights)):
            if weights[karma_score_index][0] < negative < weights[karma_score_index][-1]:
                return karma_score_index
        return self.DEFAULT_KARMA_SCORE_INDEX


def get_text_form_data(chat_messages_data_list_of_dicts: list) -> str:
    return " ".join([sentence_data[MESSAGE_TEXT_KEY] for sentence_data in chat_messages_data_list_of_dicts])


def get_server_callback_from_message_preprocessor(message_text: str,
                                                  chat_messages_data_list_of_dicts: list,
                                                  user_mode_id: int) -> ServerCallbackAnswer:

    chat_messages_data_dict_converted_to_text = get_text_form_data(chat_messages_data_list_of_dicts)
    current_message_stats_counter =\
        MessageAiProcessing.get_messege_processing_info(message_text, chat_messages_data_dict_converted_to_text)
    new_callback = ServerCallbackAnswer(current_message_stats_counter, user_mode_id)
    return new_callback

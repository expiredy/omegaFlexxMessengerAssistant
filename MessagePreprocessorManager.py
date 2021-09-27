from DictKeyConfig import *
import MessageAiProcessing
BINARY_PARAMS_CONVERTOR_PARAMS = {POSITIVE_COEFFICIENT_KEY: (),
                                  NEGATIVE_COEFFICIENT_KEY: (),
                                  NEUTRAL_COEFFICIENT_KEY: (),
                                  CONNECTION_COEFFICIENT_KEY: ()
                                  }

USERS_MODES_PARAMS_MULTIPLIERS = {CUTIE_MODE_ID: [(0, 0.25), (0.25, 1)],
                                  AVERAGE_MODE_ID: [(0, 0.5), (0.5, 1)],
                                  MORGENSHTERN_MODE_ID: [(0, 0.75), (0.75, 1)]}


class ServerCallbackAnswer():
    callback_data = {}

    def __init__(self):
        self.callback_data = {}

    def get_final_answer(self):
        pass

    def add_parameter(self, key, data):
        pass


def convert_ai_data(parameter_key: str, param: float, user_mode_id: int) -> int:
    convertor_params = BINARY_PARAMS_CONVERTOR_PARAMS[parameter_key]

    return 0


def get_text_form_data(chat_messages_data_list_of_dicts: list) -> str:
    return " ".join([sentence_data[MESSAGE_TEXT_KEY] for sentence_data in chat_messages_data_list_of_dicts])


def message_preprocessor(message_text: str,
                         chat_messages_data_list_of_dicts: list,
                         user_mode_id: int) -> ServerCallbackAnswer:

    chat_messages_data_dict_converted_to_text = get_text_form_data(chat_messages_data_list_of_dicts)
    current_message_stats_counter =\
        MessageAiProcessing.get_messege_processing_info(message_text, chat_messages_data_dict_converted_to_text)
    new_callback = ServerCallbackAnswer()
    # for param_key in list(BINARY_PARAMS_CONVERTOR_PARAMS.keys()):
    #     converted_data = convert_ai_data(param_key, current_message_stats_counter[param_key], user_mode_id)
    #     new_callback.add_parameter(key=param_key, data=converted_data)

    return new_callback

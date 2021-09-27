from DictKeyConfig import *
import MessageAiProcessing
BINARY_PARAMS_CONVERTOR_PARAMS = {POSITIVE_COEFFICIENT_KEY: (),
                                  NEGATIVE_COEFFICIENT_KEY: (),
                                  NEUTRAL_COEFFICIENT_KEY: (),
                                  CONNECTION_COEFFICIENT_KEY: ()
                                  }


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


def message_preprocessor(message_text: str, chat_messages_data_dict: dict, user_mode_id: int) -> ServerCallbackAnswer:
    current_message_stats_counter = MessageAiProcessing.get_messege_processing_info(message_text,
                                                                                    chat_messages_data_dict)
    new_callback = ServerCallbackAnswer()
    for param_key in list(BINARY_PARAMS_CONVERTOR_PARAMS.keys()):
        converted_data = convert_ai_data(param_key, current_message_stats_counter[param_key], user_mode_id)
        new_callback.add_parameter(key=param_key, data=converted_data)

    return new_callback

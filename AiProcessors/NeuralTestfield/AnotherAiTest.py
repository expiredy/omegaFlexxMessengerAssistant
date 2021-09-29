import MessagePreprocessorManager
from DictKeyConfig import *

messages_list = ["Hello, Peter",
                 "I hope you will die",
                 "I have no idea what is going on",
                 "Somebody once told me"]

previews_messages_lists = [[{MESSAGE_TEXT_KEY: "So, i watched new Spider-man movie trailer", KARMA_SCORE_KEY: -2},
                            {MESSAGE_TEXT_KEY: "And my favorite phrase is:", KARMA_SCORE_KEY: 0}],
                           [{MESSAGE_TEXT_KEY: "Fuck you", KARMA_SCORE_KEY: -2},
                            {MESSAGE_TEXT_KEY: "That doesn't fair", KARMA_SCORE_KEY: 1}],
                           [{MESSAGE_TEXT_KEY: "I love niggers", KARMA_SCORE_KEY: 1},
                            {MESSAGE_TEXT_KEY: "they are my favorite animals", KARMA_SCORE_KEY: 0}],
                           [{MESSAGE_TEXT_KEY: "I love animals", KARMA_SCORE_KEY: 1},
                            {MESSAGE_TEXT_KEY: "they are my friends", KARMA_SCORE_KEY: 2}]
                          ]

user_mode_ids_list = [0, 2, 0, 2]

for situation_index in range(len(messages_list)):
    callback =\
        MessagePreprocessorManager.get_server_callback_from_message_preprocessor(
            messages_list[situation_index],
            previews_messages_lists[situation_index],
        user_mode_ids_list[situation_index])
    print(callback.get_final_answer())
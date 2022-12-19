# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from transformers import pipeline
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

class ActionEmotion(Action):

    def name(self) -> Text:
        return "action_emotion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = str(tracker.latest_message["text"])

        emotion = classifier(text)
        output = emotion[0]
        keys = []
        values = []
        for i in output:
            for j in i.values():
                if type(j) == str:
                    keys.append(j)
                else:
                    values.append(j)

        newdict = dict(zip(keys, values))
        max_key = max(newdict, key=newdict.get)
        max_key = str(max_key)

        return [SlotSet("emotion", max_key)]

# class ResponseEmotion(Action):
#
#     def name(self) -> Text:
#         return "response_emotion"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         text = str(tracker.latest_message["text"])
#
#         emotion = classifier(text)
#         output = emotion[0]
#         keys = []
#         values = []
#         for i in output:
#             for j in i.values():
#                 if type(j) == str:
#                     keys.append(j)
#                 else:
#                     values.append(j)
#
#         newdict = dict(zip(keys, values))
#         max_key = max(newdict, key=newdict.get)
#
#         dispatcher.utter_message(text="top emotion is: {}".format(max_key))
#
#         return []

        # dispatcher.utter_message(text="top emotion is: {}".format(max_key))

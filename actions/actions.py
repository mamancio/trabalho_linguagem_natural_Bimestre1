from datetime import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Dict, List, Text
from rasa_sdk.events import SlotSet

class ActionVerificarFuncionamento(Action):
    def name(self) -> Text:
        return "action_verificar_funcionamento"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        agora = datetime.now()
        dia_semana = agora.weekday()
        hora = agora.hour

        if dia_semana < 5 and 8 <= hora < 18:
            dispatcher.utter_message(text="Sim, estamos abertos! Funcionamos de segunda a sexta, das 8h às 18h.")
        else:
            dispatcher.utter_message(text="Infelizmente, estamos fechados no momento. Nosso horário é de segunda a sexta, das 8h às 18h.")
        return []

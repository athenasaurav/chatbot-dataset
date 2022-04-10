from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.forms import FormAction
from rasa_sdk import Tracker, FormValidationAction
from .database_connectivity import FeedbackUpdate
import mysql.connector
from mysql.connector import Error
from PIL import Image
import os
from .global_setup import *

try:
    connection = mysql.connector.connect(host=host,
                                         database=database,
                                         port = port,
                                         user=user,
                                         password=password)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor(buffered=True)
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

class ActionFindGreet1(Action):

    def name(self) -> Text:
        return "action_find_greet_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent

        if intent=="greet":
            utter_greet_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_greet_1'")  
            cursor.execute(utter_greet_1)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindGreet2(Action):

    def name(self) -> Text:
        return "action_find_greet_2"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        utter_greet_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_greet_2'")  
        cursor.execute(utter_greet_2)       
        for (response) in cursor:
            dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindGreet3(Action):

    def name(self) -> Text:
        return "action_find_greet_3"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_course_type = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type) 
        find_course_type = cursor.fetchone()

        find_login_query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query) 
        find_login_query = cursor.fetchone()
        
        find_reg_query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query) 
        find_reg_query = cursor.fetchone()        

        find_course_query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query) 
        find_course_query = cursor.fetchone()  

        find_finalexam_query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_query'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_query) 
        find_finalexam_query = cursor.fetchone()          

        utter_greet_3 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_greet_3'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_greet_3) 
        utter_greet_3 = cursor.fetchone()        

        buttons = []

        buttons = [{"title": find_course_type, "payload": "/find_course_type"},{"title": find_login_query, "payload": "/find_login_query"},
                   {"title": find_reg_query, "payload": "/find_reg_query"},{"title": find_course_query, "payload": "/find_course_query"},
                   {"title": find_finalexam_query, "payload": "/find_finalexam_query"}]
        
        dispatcher.utter_message(str(utter_greet_3).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindLoginQuery1(Action):

    def name(self) -> Text:
        return "action_find_login_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_login_query":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_login_query_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindRegQuery1(Action):

    def name(self) -> Text:
        return "action_find_reg_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_reg_query":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_reg_query_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindRegQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_reg_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_genreg_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_genreg_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_genreg_queries) 
        find_genreg_queries = cursor.fetchone()

        find_altreg_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_altreg_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_altreg_queries) 
        find_altreg_queries = cursor.fetchone()
        
        find_unenroll_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_unenroll_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_unenroll_queries) 
        find_unenroll_queries = cursor.fetchone()        

        find_sec_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_sec_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_sec_queries) 
        find_sec_queries = cursor.fetchone()  

        find_paym_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_paym_queries) 
        find_paym_queries = cursor.fetchone()  

        utter_find_reg_query_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_reg_query_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_reg_query_2) 
        utter_find_reg_query_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_genreg_queries, "payload": "/find_genreg_queries"},{"title": find_altreg_queries, "payload": "/find_altreg_queries"},
                   {"title": find_unenroll_queries, "payload": "/find_unenroll_queries"},{"title": find_sec_queries, "payload": "/find_sec_queries"},
                   {"title": find_paym_queries, "payload": "/find_paym_queries"},{"title": find_rollback, "payload": "/back_action_find_greet_3"}]
                   
        dispatcher.utter_message(str(utter_find_reg_query_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindGenRegQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_genreg_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_genreg_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_genreg_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_genreg_queries_2) 
        find_genreg_queries_2 = cursor.fetchone()

        find_genreg_queries_3 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_genreg_queries_3'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_genreg_queries_3) 
        find_genreg_queries_3 = cursor.fetchone()
        
        find_genreg_queries_4 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_genreg_queries_4'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_genreg_queries_4) 
        find_genreg_queries_4 = cursor.fetchone()        

        utter_find_genreg_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_genreg_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_genreg_query_1) 
        utter_find_genreg_query_1 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_genreg_queries_2, "payload": "/find_genreg_queries_2"},{"title": find_genreg_queries_3, "payload": "/find_genreg_queries_3"},
                   {"title": find_genreg_queries_4, "payload": "/find_genreg_queries_4"},{"title": find_rollback, "payload": "/back_action_find_reg_query_buttons"}]

        dispatcher.utter_message(str(utter_find_genreg_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindAltRegQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_altreg_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_altreg_queries_3 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_altreg_queries_3'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_altreg_queries_3) 
        find_altreg_queries_3 = cursor.fetchone()

        find_altreg_queries_5 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_altreg_queries_5'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_altreg_queries_5) 
        find_altreg_queries_5 = cursor.fetchone()
        
        find_altreg_queries_1 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_altreg_queries_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_altreg_queries_1) 
        find_altreg_queries_1 = cursor.fetchone()        

        utter_find_altreg_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_altreg_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_altreg_query_1) 
        utter_find_altreg_query_1 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_altreg_queries_3, "payload": "/find_altreg_queries_3"},{"title": find_altreg_queries_5, "payload": "/find_altreg_queries_5"},
                   {"title": find_altreg_queries_1, "payload": "/find_altreg_queries_1"},{"title": find_rollback, "payload": "/back_action_find_reg_query_buttons"}]
        dispatcher.utter_message(str(utter_find_altreg_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindUnenrollQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_unenroll_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_unenroll_queries_1 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_unenroll_queries_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_unenroll_queries_1) 
        find_unenroll_queries_1 = cursor.fetchone()      

        utter_find_unenroll_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_unenroll_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_unenroll_query_1) 
        utter_find_unenroll_query_1 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_unenroll_queries_1, "payload": "/find_unenroll_queries_1"},{"title": find_rollback, "payload": "/back_action_find_reg_query_buttons"}]
        dispatcher.utter_message(str(utter_find_unenroll_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindSecQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_sec_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_sec_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_sec_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_sec_queries_2) 
        find_sec_queries_2 = cursor.fetchone()      

        find_sec_queries_6 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_sec_queries_6'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_sec_queries_6) 
        find_sec_queries_6 = cursor.fetchone()      

        find_sec_queries_7 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_sec_queries_7'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_sec_queries_7) 
        find_sec_queries_7 = cursor.fetchone()      

        utter_find_sec_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_sec_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_sec_query_1) 
        utter_find_sec_query_1 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_sec_queries_2, "payload": "/find_sec_queries_2"},{"title": find_sec_queries_6, "payload": "/find_sec_queries_6"},
                   {"title": find_sec_queries_7, "payload": "/find_sec_queries_7"},{"title": find_rollback, "payload": "/back_action_find_reg_query_buttons"}]
        dispatcher.utter_message(str(utter_find_sec_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindPaymQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_paym_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_paym_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_paym_queries_2) 
        find_paym_queries_2 = cursor.fetchone()      

        find_paym_queries_9 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_9'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_paym_queries_9) 
        find_paym_queries_9 = cursor.fetchone()      

        find_paym_queries_20 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_20'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_paym_queries_20) 
        find_paym_queries_20 = cursor.fetchone()      

        utter_find_paym_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_paym_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_paym_query_1) 
        utter_find_paym_query_1 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_paym_queries_2, "payload": "/find_paym_queries_2"},{"title": find_paym_queries_9, "payload": "/find_paym_queries_9"},
                   {"title": find_paym_queries_20, "payload": "/find_paym_queries_20"},{"title": find_rollback, "payload": "/back_action_find_reg_query_buttons"}]
        dispatcher.utter_message(str(utter_find_paym_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindCourseQuery1(Action):

    def name(self) -> Text:
        return "action_find_course_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_course_query":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_course_query_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindCourseQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_coursequery_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_courseaccess_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_courseaccess_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_courseaccess_queries) 
        find_courseaccess_queries = cursor.fetchone()

        find_courseeval_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_courseeval_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_courseeval_queries) 
        find_courseeval_queries = cursor.fetchone()
        
        find_coursecontent_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_coursecontent_queries) 
        find_coursecontent_queries = cursor.fetchone()        

        find_tutorials_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_tutorials_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_tutorials_queries) 
        find_tutorials_queries = cursor.fetchone()  

        find_assignments_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_assignments_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_assignments_queries) 
        find_assignments_queries = cursor.fetchone()  

        find_livelectures_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_livelectures_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_livelectures_queries) 
        find_livelectures_queries = cursor.fetchone() 

        find_certificate_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_certificate_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_certificate_queries) 
        find_certificate_queries = cursor.fetchone() 
                
        utter_find_course_query_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_course_query_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_course_query_2) 
        utter_find_course_query_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_courseaccess_queries, "payload": "/find_courseaccess_queries"},{"title": find_courseeval_queries, "payload": "/find_courseeval_queries"},
                   {"title": find_tutorials_queries, "payload": "/find_tutorials_queries"},{"title": find_coursecontent_queries, "payload": "/find_coursecontent_queries"},
                   {"title": find_livelectures_queries, "payload": "/find_livelectures_queries"},{"title": find_assignments_queries, "payload": "/find_assignments_queries"},
                   {"title": find_certificate_queries, "payload": "/find_certificate_queries"},{"title": find_rollback, "payload": "/back_action_find_greet_3"}]
        dispatcher.utter_message(str(utter_find_course_query_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindFinalExamQuery1(Action):

    def name(self) -> Text:
        return "action_find_finalexam_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_finalexam_query":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_finalexam_query_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindFinalExamQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_finalexam_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_deadline_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_deadline_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_deadline_queries) 
        find_deadline_queries = cursor.fetchone()

        find_access_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_access_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_access_queries) 
        find_access_queries = cursor.fetchone()
        
        find_gradeappeal_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_gradeappeal_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_gradeappeal_queries) 
        find_gradeappeal_queries = cursor.fetchone()        

        find_rulesreg_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rulesreg_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rulesreg_queries) 
        find_rulesreg_queries = cursor.fetchone()  

        find_deferrals_queries = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_deferrals_queries'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_deferrals_queries) 
        find_deferrals_queries = cursor.fetchone()  
                
        utter_find_finalexam_query_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_finalexam_query_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_finalexam_query_2) 
        utter_find_finalexam_query_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone()

        buttons = []

        buttons = [{"title": find_deadline_queries, "payload": "/find_deadline_queries"},{"title": find_access_queries, "payload": "/find_access_queries"},
                   {"title": find_gradeappeal_queries, "payload": "/find_gradeappeal_queries"},{"title": find_rulesreg_queries, "payload": "/find_rulesreg_queries"},
                   {"title": find_deferrals_queries, "payload": "/find_deferrals_queries"},{"title": find_rollback, "payload": "/back_action_find_greet_3"}]
        dispatcher.utter_message(str(utter_find_finalexam_query_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindCourseAccessQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_courseaccess_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_courseaccess_queries_1 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_courseaccess_queries_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_courseaccess_queries_1) 
        find_courseaccess_queries_1 = cursor.fetchone()      

        find_courseaccess_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_courseaccess_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_courseaccess_queries_2) 
        find_courseaccess_queries_2 = cursor.fetchone()      

        find_courseaccess_queries_3 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_courseaccess_queries_3'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_courseaccess_queries_3) 
        find_courseaccess_queries_3 = cursor.fetchone()      

        utter_find_courseaccess_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_courseaccess_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_courseaccess_query_1) 
        utter_find_courseaccess_query_1 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_courseaccess_queries_1, "payload": "/find_courseaccess_queries_1"},{"title": find_courseaccess_queries_2, "payload": "/find_courseaccess_queries_2"},
                   {"title": find_courseaccess_queries_3, "payload": "/find_courseaccess_queries_3"},{"title": find_rollback, "payload": "/back_action_find_coursequery_query_buttons"}]
        dispatcher.utter_message(str(utter_find_courseaccess_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindCourseEvalQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_courseeval_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_courseeval_queries_1 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_courseeval_queries_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_courseeval_queries_1) 
        find_courseeval_queries_1 = cursor.fetchone()      

        find_courseeval_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_courseeval_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_courseeval_queries_2) 
        find_courseeval_queries_2 = cursor.fetchone()          

        utter_find_courseeval_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_courseeval_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_courseeval_query_1) 
        utter_find_courseeval_query_1 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_courseeval_queries_1, "payload": "/find_courseeval_queries_1"},{"title": find_courseeval_queries_2, "payload": "/find_courseeval_queries_2"},
                   {"title": find_rollback, "payload": "/back_action_find_coursequery_query_buttons"}]
        dispatcher.utter_message(str(utter_find_courseeval_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindCourseContentQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_coursecontent_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_coursecontent_queries_1 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_coursecontent_queries_1) 
        find_coursecontent_queries_1 = cursor.fetchone()      

        find_coursecontent_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_coursecontent_queries_2) 
        find_coursecontent_queries_2 = cursor.fetchone()      

        find_coursecontent_queries_3 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_3'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_coursecontent_queries_3) 
        find_coursecontent_queries_3 = cursor.fetchone()      

        utter_find_coursecontent_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_coursecontent_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_coursecontent_query_1) 
        utter_find_coursecontent_query_1 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_coursecontent_queries_1, "payload": "/find_coursecontent_queries_1"},{"title": find_coursecontent_queries_2, "payload": "/find_coursecontent_queries_2"},
                   {"title": find_coursecontent_queries_3, "payload": "/find_coursecontent_queries_3"},{"title": find_rollback, "payload": "/back_action_find_coursequery_query_buttons"}]
        dispatcher.utter_message(str(utter_find_coursecontent_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return [] 

class ActionFindTutorialsQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_tutorials_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_tutorials_queries_1 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_tutorials_queries_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_tutorials_queries_1) 
        find_tutorials_queries_1 = cursor.fetchone()      

        find_tutorials_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_tutorials_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_tutorials_queries_2) 
        find_tutorials_queries_2 = cursor.fetchone()      

        find_tutorials_queries_3 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_tutorials_queries_3'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_tutorials_queries_3) 
        find_tutorials_queries_3 = cursor.fetchone()      

        utter_find_tutorials_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_tutorials_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_tutorials_query_1) 
        utter_find_tutorials_query_1 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone()  

        buttons = []

        buttons = [{"title": find_tutorials_queries_1, "payload": "/find_tutorials_queries_1"},{"title": find_tutorials_queries_2, "payload": "/find_tutorials_queries_2"},
                   {"title": find_tutorials_queries_3, "payload": "/find_tutorials_queries_3"},{"title": find_rollback, "payload": "/back_action_find_coursequery_query_buttons"}]
        dispatcher.utter_message(str(utter_find_tutorials_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []  

class ActionFindAssignmentsQueryButtonsIntro(Action):

    def name(self) -> Text:
        return "action_find_assignments_query_buttons_intro"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:
     
        utter_find_assignments_query_intro = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_assignments_query_intro'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_assignments_query_intro) 
        utter_find_assignments_query_intro = cursor.fetchone()  
 
        dispatcher.utter_message(str(utter_find_assignments_query_intro).strip('("",)').strip("'").replace('\',', ''))

        return [] 

class ActionFindAssignmentsQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_assignments_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_assignments_queries_1 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_assignments_queries_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_assignments_queries_1) 
        find_assignments_queries_1 = cursor.fetchone()      

        find_assignments_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_assignments_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_assignments_queries_2) 
        find_assignments_queries_2 = cursor.fetchone()      

        find_assignments_queries_3 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_assignments_queries_3'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_assignments_queries_3) 
        find_assignments_queries_3 = cursor.fetchone()      

        utter_find_assignments_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_assignments_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_assignments_query_1) 
        utter_find_assignments_query_1 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_assignments_queries_1, "payload": "/find_assignments_queries_1"},{"title": find_assignments_queries_2, "payload": "/find_assignments_queries_2"},
                   {"title": find_assignments_queries_3, "payload": "/find_assignments_queries_3"},{"title": find_rollback, "payload": "/back_action_find_coursequery_query_buttons"}]
        dispatcher.utter_message(str(utter_find_assignments_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return [] 

class ActionFindLiveLecturesQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_livelectures_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_livelectures_queries_1 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_livelectures_queries_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_livelectures_queries_1) 
        find_livelectures_queries_1 = cursor.fetchone()      

        find_livelectures_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_livelectures_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_livelectures_queries_2) 
        find_livelectures_queries_2 = cursor.fetchone()      

        find_livelectures_queries_3 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_livelectures_queries_3'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_livelectures_queries_3) 
        find_livelectures_queries_3 = cursor.fetchone()      

        utter_find_livelectures_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_livelectures_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_livelectures_query_1) 
        utter_find_livelectures_query_1 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_livelectures_queries_1, "payload": "/find_livelectures_queries_1"},{"title": find_livelectures_queries_2, "payload": "/find_livelectures_queries_2"},
                   {"title": find_livelectures_queries_3, "payload": "/find_livelectures_queries_3"},{"title": find_rollback, "payload": "/back_action_find_coursequery_query_buttons"}]
        dispatcher.utter_message(str(utter_find_livelectures_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []  

class ActionFindCertificateQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_certificate_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_certificate_queries_1 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_certificate_queries_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_certificate_queries_1) 
        find_certificate_queries_1 = cursor.fetchone()      

        find_certificate_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_certificate_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_certificate_queries_2) 
        find_certificate_queries_2 = cursor.fetchone()      

        find_certificate_queries_3 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_certificate_queries_3'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_certificate_queries_3) 
        find_certificate_queries_3 = cursor.fetchone()      

        utter_find_certificate_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_certificate_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_certificate_query_1) 
        utter_find_certificate_query_1 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_certificate_queries_1, "payload": "/find_certificate_queries_1"},{"title": find_certificate_queries_2, "payload": "/find_certificate_queries_2"},
                   {"title": find_certificate_queries_3, "payload": "/find_certificate_queries_3"},{"title": find_rollback, "payload": "/back_action_find_coursequery_query_buttons"}]
        dispatcher.utter_message(str(utter_find_certificate_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []  

class ActionFindDeadlineQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_deadline_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_deadline_queries_1 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_deadline_queries_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_deadline_queries_1) 
        find_deadline_queries_1 = cursor.fetchone()      

        find_deadline_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_deadline_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_deadline_queries_2) 
        find_deadline_queries_2 = cursor.fetchone()      

        find_deadline_queries_3 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_deadline_queries_3'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_deadline_queries_3) 
        find_deadline_queries_3 = cursor.fetchone()      

        utter_find_deadline_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_deadline_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_deadline_query_1) 
        utter_find_deadline_query_1 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_deadline_queries_1, "payload": "/find_deadline_queries_1"},{"title": find_deadline_queries_2, "payload": "/find_deadline_queries_2"},
                   {"title": find_deadline_queries_3, "payload": "/find_deadline_queries_3"},{"title": find_rollback, "payload": "/back_action_find_finalexam_query_buttons"}]
        dispatcher.utter_message(str(utter_find_deadline_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []   

class ActionFindAccessQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_access_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_access_queries_1 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_access_queries_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_access_queries_1) 
        find_access_queries_1 = cursor.fetchone()      

        find_access_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_access_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_access_queries_2) 
        find_access_queries_2 = cursor.fetchone()      

        find_access_queries_3 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_access_queries_3'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_access_queries_3) 
        find_access_queries_3 = cursor.fetchone()      

        utter_find_access_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_access_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_access_query_1) 
        utter_find_access_query_1 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_access_queries_1, "payload": "/find_access_queries_1"},{"title": find_access_queries_2, "payload": "/find_access_queries_2"},
                   {"title": find_access_queries_3, "payload": "/find_access_queries_3"},{"title": find_rollback, "payload": "/back_action_find_finalexam_query_buttons"}]
        dispatcher.utter_message(str(utter_find_access_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []    

class ActionFindGradeAppealQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_gradeappeal_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_gradeappeal_queries_1 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_gradeappeal_queries_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_gradeappeal_queries_1) 
        find_gradeappeal_queries_1 = cursor.fetchone()      

        find_gradeappeal_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_gradeappeal_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_gradeappeal_queries_2) 
        find_gradeappeal_queries_2 = cursor.fetchone()      

        find_gradeappeal_queries_3 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_gradeappeal_queries_3'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_gradeappeal_queries_3) 
        find_gradeappeal_queries_3 = cursor.fetchone()      

        utter_find_gradeappeal_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_gradeappeal_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_gradeappeal_query_1) 
        utter_find_gradeappeal_query_1 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_gradeappeal_queries_1, "payload": "/find_gradeappeal_queries_1"},{"title": find_gradeappeal_queries_2, "payload": "/find_gradeappeal_queries_2"},
                   {"title": find_gradeappeal_queries_3, "payload": "/find_gradeappeal_queries_3"},{"title": find_rollback, "payload": "/back_action_find_finalexam_query_buttons"}]
        dispatcher.utter_message(str(utter_find_gradeappeal_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return [] 

class ActionFindRulesRegQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_rulesreg_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_rulesreg_queries_1 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_rulesreg_queries_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rulesreg_queries_1) 
        find_rulesreg_queries_1 = cursor.fetchone()      

        find_rulesreg_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_rulesreg_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rulesreg_queries_2) 
        find_rulesreg_queries_2 = cursor.fetchone()      

        find_rulesreg_queries_3 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_rulesreg_queries_3'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rulesreg_queries_3) 
        find_rulesreg_queries_3 = cursor.fetchone()      

        utter_find_rulesreg_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_rulesreg_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_rulesreg_query_1) 
        utter_find_rulesreg_query_1 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_rulesreg_queries_1, "payload": "/find_rulesreg_queries_1"},{"title": find_rulesreg_queries_2, "payload": "/find_rulesreg_queries_2"},
                   {"title": find_rulesreg_queries_3, "payload": "/find_rulesreg_queries_3"},{"title": find_rollback, "payload": "/back_action_find_finalexam_query_buttons"}]
        dispatcher.utter_message(str(utter_find_rulesreg_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []                                                                

class ActionFindDeferralsQueryButtons(Action):

    def name(self) -> Text:
        return "action_find_deferrals_query_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_deferrals_queries_1 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_deferrals_queries_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_deferrals_queries_1) 
        find_deferrals_queries_1 = cursor.fetchone()      

        find_deferrals_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_deferrals_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_deferrals_queries_2) 
        find_deferrals_queries_2 = cursor.fetchone()         

        utter_find_deferrals_query_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_deferrals_query_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_deferrals_query_1) 
        utter_find_deferrals_query_1 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_deferrals_queries_1, "payload": "/find_deferrals_queries_1"},{"title": find_deferrals_queries_2, "payload": "/find_deferrals_queries_2"},
                   {"title": find_rollback, "payload": "/back_action_find_finalexam_query_buttons"}]
        dispatcher.utter_message(str(utter_find_deferrals_query_1).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindLoginReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_login_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_genlogin_queries_1" or intent=="find_genlogin_queries_2" or intent=="find_genlogin_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_login_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindLoginReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_login_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_ask = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_ask'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_ask) 
        find_login_query_ask = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone() 

        utter_login_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_login_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_login_reverse_2) 
        utter_login_reverse_2 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_login_query_ask, "payload": "/find_login_query"},{"title": find_reg_query_goto, "payload": "/find_reg_query"},
                   {"title": find_course_type_goto, "payload": "/find_course_type"},{"title": find_course_query_goto, "payload": "/find_course_query"},
                   {"title": find_finalexam_goto, "payload": "/find_finalexam_query"},{"title": find_rollback, "payload": "/back_action_find_genlogin_buttons"}]
        dispatcher.utter_message(str(utter_login_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindGenRegReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_genreg_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_genreg_queries_1" or intent=="find_genreg_queries_2" or intent=="find_genreg_queries_3" or intent=="find_genreg_queries_4" or intent=="find_genreg_queries_5" or intent=="find_genreg_queries_6" or intent=="find_genreg_queries_7" or intent=="find_genreg_queries_8" or intent=="find_genreg_queries_9":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_genreg_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindGenRegReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_genreg_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_askgenreg_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_askgenreg_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askgenreg_question) 
        find_askgenreg_question = cursor.fetchone() 

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone() 

        utter_genreg_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_genreg_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_genreg_reverse_2) 
        utter_genreg_reverse_2 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"}, {"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_genreg_queries"}]
        dispatcher.utter_message(str(utter_genreg_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindAltRegReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_altreg_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_altreg_queries_1" or intent=="find_altreg_queries_2" or intent=="find_altreg_queries_3" or intent=="find_altreg_queries_4" or intent=="find_altreg_queries_5" or intent=="find_altreg_queries_6" or intent=="find_altreg_queries_7" or intent=="find_altreg_queries_8" or intent=="find_altreg_queries_9":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_altreg_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindAltRegReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_altreg_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_askaltreg_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_askaltreg_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askaltreg_question) 
        find_askaltreg_question = cursor.fetchone() 

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone() 

        utter_altreg_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_altreg_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_altreg_reverse_2) 
        utter_altreg_reverse_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_altreg_queries"}]
        dispatcher.utter_message(str(utter_altreg_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindUnenrollReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_unenroll_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_unenroll_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_unenroll_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindUnenrollReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_unenroll_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_askunenroll_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_askunenroll_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askunenroll_question) 
        find_askunenroll_question = cursor.fetchone()  

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone() 

        utter_unenroll_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_unenroll_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_unenroll_reverse_2) 
        utter_unenroll_reverse_2 = cursor.fetchone()  
 
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_unenroll_queries"}]

        dispatcher.utter_message(str(utter_unenroll_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindSecReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_sec_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_sec_queries_1" or intent=="find_sec_queries_2" or intent=="find_sec_queries_3" or intent=="find_sec_queries_4" or intent=="find_sec_queries_5" or intent=="find_sec_queries_6" or intent=="find_sec_queries_7" or intent=="find_sec_queries_8" or intent=="find_sec_queries_9" or intent=="find_sec_queries_10":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_sec_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindSecReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_sec_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_asksec_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_asksec_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_asksec_question) 
        find_asksec_question = cursor.fetchone()   

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone() 

        utter_sec_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_sec_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_sec_reverse_2) 
        utter_sec_reverse_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_sec_queries"}]
                   
        dispatcher.utter_message(str(utter_sec_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindPaymReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_paym_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_paym_queries_1" or intent=="find_paym_queries_2" or intent=="find_paym_queries_3" or intent=="find_paym_queries_4" or intent=="find_paym_queries_5" or intent=="find_paym_queries_6" or intent=="find_paym_queries_7" or intent=="find_paym_queries_8" or intent=="find_paym_queries_9" or intent=="find_paym_queries_10" or intent=="find_paym_queries_11" or intent=="find_paym_queries_12" or intent=="find_paym_queries_13" or intent=="find_paym_queries_14" or intent=="find_paym_queries_15" or intent=="find_paym_queries_16" or intent=="find_paym_queries_17" or intent=="find_paym_queries_18" or intent=="find_paym_queries_19" or intent=="find_paym_queries_20":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_paym_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindPaymReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_paym_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_askpaym_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_askpaym_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askpaym_question) 
        find_askpaym_question = cursor.fetchone()  

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone() 

        utter_paym_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_paym_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_paym_reverse_2) 
        utter_paym_reverse_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_paym_queries"}]
                   
        dispatcher.utter_message(str(utter_paym_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindCourseAccessReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_courseaccess_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_courseaccess_queries_1" or intent=="find_courseaccess_queries_2" or intent=="find_courseaccess_queries_3" or intent=="find_courseaccess_queries_4" or intent=="find_courseaccess_queries_5" or intent=="find_courseaccess_queries_6" or intent=="find_courseaccess_queries_7" or intent=="find_courseaccess_queries_8":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_courseaccess_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindCourseAccessReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_courseaccess_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_askcourseaccess_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_askcourseaccess_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askcourseaccess_question) 
        find_askcourseaccess_question = cursor.fetchone()  

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone()            

        utter_courseaccess_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_courseaccess_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_courseaccess_reverse_2) 
        utter_courseaccess_reverse_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_courseaccess_queries"}]

        dispatcher.utter_message(str(utter_courseaccess_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindCourseEvalReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_courseeval_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_courseeval_queries_1" or intent=="find_courseeval_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_courseeval_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindCourseEvalReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_courseeval_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_askcourseeval_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_askcourseeval_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askcourseeval_question) 
        find_askcourseeval_question = cursor.fetchone()  

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone()            

        utter_courseeval_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_courseeval_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_courseeval_reverse_2) 
        utter_courseeval_reverse_2 = cursor.fetchone()   

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone()

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_courseeval_queries"}]

        dispatcher.utter_message(str(utter_courseeval_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindCourseContentReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_coursecontent_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_coursecontent_queries_1" or intent=="find_coursecontent_queries_2" or intent=="find_coursecontent_queries_3" or intent=="find_coursecontent_queries_4" or intent=="find_coursecontent_queries_5" or intent=="find_coursecontent_queries_6" or intent=="find_coursecontent_queries_7" or intent=="find_coursecontent_queries_8" or intent=="find_coursecontent_queries_9" or intent=="find_coursecontent_queries_10" or intent=="find_coursecontent_queries_11" or intent=="find_coursecontent_queries_12" or intent=="find_coursecontent_queries_13":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_coursecontent_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindCourseContentReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_coursecontent_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_askcoursecontent_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_askcoursecontent_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askcoursecontent_question) 
        find_askcoursecontent_question = cursor.fetchone()  

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone()            

        utter_coursecontent_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_coursecontent_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_coursecontent_reverse_2) 
        utter_coursecontent_reverse_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone()

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_coursecontent_queries"}]

        dispatcher.utter_message(str(utter_coursecontent_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindTutorialsReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_tutorials_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_tutorials_queries_1" or intent=="find_tutorials_queries_2" or intent=="find_tutorials_queries_3" or intent=="find_tutorials_queries_4" or intent=="find_tutorials_queries_5" or intent=="find_tutorials_queries_6" or intent=="find_tutorials_queries_7" or intent=="find_tutorials_queries_8" or intent=="find_tutorials_queries_9" or intent=="find_tutorials_queries_10":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_tutorials_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindTutorialsReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_tutorials_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_asktutorials_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_asktutorials_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_asktutorials_question) 
        find_asktutorials_question = cursor.fetchone()  

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone()            

        utter_tutorials_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_tutorials_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_tutorials_reverse_2) 
        utter_tutorials_reverse_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone()

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_tutorials_queries"}]

        dispatcher.utter_message(str(utter_tutorials_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindAssignmentsReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_assignments_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_assignments_queries_1" or intent=="find_assignments_queries_2" or intent=="find_assignments_queries_3" or intent=="find_assignments_queries_4" or intent=="find_assignments_queries_5" or intent=="find_assignments_queries_6" or intent=="find_assignments_queries_7" or intent=="find_assignments_queries_8":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_assignments_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindAssignmentsReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_assignments_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_askassignments_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_askassignments_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askassignments_question) 
        find_askassignments_question = cursor.fetchone()  

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone()            

        utter_assignments_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_assignments_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_assignments_reverse_2) 
        utter_assignments_reverse_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone()

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_assignments_queries"}]

        dispatcher.utter_message(str(utter_assignments_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindLiveLecturesReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_livelectures_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_livelectures_queries_1" or intent=="find_livelectures_queries_2" or intent=="find_livelectures_queries_3" or intent=="find_livelectures_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_livelectures_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindLiveLecturesReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_livelectures_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_asklivelectures_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_asklivelectures_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_asklivelectures_question) 
        find_asklivelectures_question = cursor.fetchone()  

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone()            

        utter_livelectures_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_livelectures_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_livelectures_reverse_2) 
        utter_livelectures_reverse_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone()

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_livelectures_queries"}]

        dispatcher.utter_message(str(utter_livelectures_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindCertificateReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_certificate_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_certificate_queries_1" or intent=="find_certificate_queries_2" or intent=="find_certificate_queries_3" or intent=="find_certificate_queries_4" or intent=="find_certificate_queries_5" or intent=="find_certificate_queries_6" or intent=="find_certificate_queries_7" or intent=="find_certificate_queries_8" or intent=="find_certificate_queries_9":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_certificate_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindCertificateReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_certificate_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_askcertificate_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_askcertificate_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askcertificate_question) 
        find_askcertificate_question = cursor.fetchone()  

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone()            

        utter_certificate_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_certificate_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_certificate_reverse_2) 
        utter_certificate_reverse_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone()

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_certificate_queries"}]

        dispatcher.utter_message(str(utter_certificate_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindDeadlineReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_deadline_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_deadline_queries_1" or intent=="find_deadline_queries_2" or intent=="find_deadline_queries_3" or intent=="find_deadline_queries_4" or intent=="find_deadline_queries_5":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_deadline_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindDeadlineReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_deadline_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_askdeadline_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_askdeadline_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askdeadline_question) 
        find_askdeadline_question = cursor.fetchone()  

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone()            

        utter_deadline_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_deadline_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_deadline_reverse_2) 
        utter_deadline_reverse_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone()

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_deadline_queries"}]

        dispatcher.utter_message(str(utter_deadline_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindAccessReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_access_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_access_queries_1" or intent=="find_access_queries_2" or intent=="find_access_queries_3" or intent=="find_access_queries_4" or intent=="find_access_queries_5" or intent=="find_access_queries_6":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_access_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindAccessReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_access_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_askaccess_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_askaccess_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askaccess_question) 
        find_askaccess_question = cursor.fetchone()  

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone()            

        utter_access_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_access_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_access_reverse_2) 
        utter_access_reverse_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone()

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_access_queries"}]

        dispatcher.utter_message(str(utter_access_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindGradeAppealReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_gradeappeal_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_gradeappeal_queries_1" or intent=="find_gradeappeal_queries_2" or intent=="find_gradeappeal_queries_3" or intent=="find_gradeappeal_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_gradeappeal_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindGradeAppealReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_gradeappeal_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_askgradeappeal_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_askgradeappeal_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askgradeappeal_question) 
        find_askgradeappeal_question = cursor.fetchone()  

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone()            

        utter_gradeappeal_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_gradeappeal_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_gradeappeal_reverse_2) 
        utter_gradeappeal_reverse_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone()

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_gradeappeal_queries"}]

        dispatcher.utter_message(str(utter_gradeappeal_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindRulesRegReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_rulesreg_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_rulesreg_queries_1" or intent=="find_rulesreg_queries_2" or intent=="find_rulesreg_queries_3" or intent=="find_rulesreg_queries_4" or intent=="find_rulesreg_queries_5" or intent=="find_rulesreg_queries_6" or intent=="find_rulesreg_queries_7" or intent=="find_rulesreg_queries_8" or intent=="find_rulesreg_queries_9" or intent=="find_rulesreg_queries_10" or intent=="find_rulesreg_queries_11":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_rulesreg_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindRulesRegReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_rulesreg_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_askrulesreg_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_askrulesreg_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askrulesreg_question) 
        find_askrulesreg_question = cursor.fetchone()  

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone()            

        utter_rulesreg_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_rulesreg_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_rulesreg_reverse_2) 
        utter_rulesreg_reverse_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone()

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_rulesreg_queries"}]

        dispatcher.utter_message(str(utter_rulesreg_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindDeferralsReverseQuery1(Action):

    def name(self) -> Text:
        return "action_find_deferrals_reverse_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_deferrals_queries_1" or intent=="find_deferrals_queries_2" :
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_deferrals_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindDeferralsReverseQuery2(Action):

    def name(self) -> Text:
        return "action_find_deferrals_reverse_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        find_askdeferrals_question = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_askdeferrals_question'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_askdeferrals_question) 
        find_askdeferrals_question = cursor.fetchone()  

        find_course_type_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_goto) 
        find_course_type_goto = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone()            

        utter_deferrals_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_deferrals_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_deferrals_reverse_2) 
        utter_deferrals_reverse_2 = cursor.fetchone()  

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone()

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},
                   {"title": find_reg_query_goto, "payload": "/find_reg_query"},{"title": find_course_type_goto, "payload": "/find_course_type"},
                   {"title": find_course_query_goto, "payload": "/find_course_query"},{"title": find_finalexam_goto, "payload": "/find_finalexam_query"},
                   {"title": find_rollback, "payload": "/find_deferrals_queries"}]

        dispatcher.utter_message(str(utter_deferrals_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindCourseInfoQuery1(Action):

    def name(self) -> Text:
        return "action_find_courseinfo_query_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_course_type":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_courseinfo_query_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindCourseInfoQuery2(Action):

    def name(self) -> Text:
        return "action_find_courseinfo_query_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:    
 
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        utter_find_courseinfo_query_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_courseinfo_query_2'")  
        cursor.execute(utter_find_courseinfo_query_2)       
        for (response) in cursor:
            dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindCourseInfoQuery3(Action):

    def name(self) -> Text:
        return "action_find_courseinfo_query_3"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:    
 
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        utter_find_courseinfo_query_3 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_courseinfo_query_3'")  
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_courseinfo_query_3) 
        utter_find_courseinfo_query_3 = cursor.fetchone() 

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_rollback, "payload": "/back_action_find_greet_3"}]
                   
        dispatcher.utter_message(str(utter_find_courseinfo_query_3).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindCourseReverse1(Action):

    def name(self) -> Text:
        return "action_find_course_reverse_1"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_DL001_description" or intent=="find_DL001_content" or intent=="find_DL001_learningoutcomes" or intent=="find_DL001_teaching" or intent=="find_DL001_finalexam" or intent=="find_DL001_cert" or intent=="find_DL001_dur" or intent=="find_DL001_tuitionfees" or intent=="find_DL001_elig" or intent=="find_DL001_reg" or intent=="find_DL001_lang" or intent=="find_DL001_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl001_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101_description" or intent=="find_DL101_content" or intent=="find_DL101_learningoutcomes" or intent=="find_DL101_teaching" or intent=="find_DL101_finalexam" or intent=="find_DL101_cert" or intent=="find_DL101_dur" or intent=="find_DL101_tuitionfees" or intent=="find_DL101_elig" or intent=="find_DL101_reg" or intent=="find_DL101_lang" or intent=="find_DL101_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl101_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101PCT_description" or intent=="find_DL101PCT_content" or intent=="find_DL101PCT_learningoutcomes" or intent=="find_DL101PCT_teaching" or intent=="find_DL101PCT_finalexam" or intent=="find_DL101PCT_cert" or intent=="find_DL101PCT_dur" or intent=="find_DL101PCT_tuitionfees" or intent=="find_DL101PCT_elig" or intent=="find_DL101PCT_reg" or intent=="find_DL101PCT_lang" or intent=="find_DL101PCT_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl101pct_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL170_description" or intent=="find_DL170_content" or intent=="find_DL170_learningoutcomes" or intent=="find_DL170_teaching" or intent=="find_DL170_finalexam" or intent=="find_DL170_cert" or intent=="find_DL170_dur" or intent=="find_DL170_tuitionfees" or intent=="find_DL170_elig" or intent=="find_DL170_reg" or intent=="find_DL170_lang" or intent=="find_DL170_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl170_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL177_description" or intent=="find_DL177_content" or intent=="find_DL177_learningoutcomes" or intent=="find_DL177_teaching" or intent=="find_DL177_finalexam" or intent=="find_DL177_cert" or intent=="find_DL177_dur" or intent=="find_DL177_tuitionfees" or intent=="find_DL177_elig" or intent=="find_DL177_reg" or intent=="find_DL177_lang" or intent=="find_DL177_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl177_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPPAN_description" or intent=="find_DLIPPAN_content" or intent=="find_DLIPPAN_learningoutcomes" or intent=="find_DLIPPAN_teaching" or intent=="find_DLIPPAN_finalexam" or intent=="find_DLIPPAN_cert" or intent=="find_DLIPPAN_dur" or intent=="find_DLIPPAN_tuitionfees" or intent=="find_DLIPPAN_elig" or intent=="find_DLIPPAN_reg" or intent=="find_DLIPPAN_lang" or intent=="find_DLIPPAN_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dlippan_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL201_description" or intent=="find_DL201_content" or intent=="find_DL201_learningoutcomes" or intent=="find_DL201_teaching" or intent=="find_DL201_finalexam" or intent=="find_DL201_cert" or intent=="find_DL201_dur" or intent=="find_DL201_tuitionfees" or intent=="find_DL201_elig" or intent=="find_DL201_reg" or intent=="find_DL201_lang" or intent=="find_DL201_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl201_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL203_description" or intent=="find_DL203_content" or intent=="find_DL203_learningoutcomes" or intent=="find_DL203_teaching" or intent=="find_DL203_finalexam" or intent=="find_DL203_cert" or intent=="find_DL203_dur" or intent=="find_DL203_tuitionfees" or intent=="find_DL203_elig" or intent=="find_DL203_reg" or intent=="find_DL203_lang" or intent=="find_DL203_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl203_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL205UPOV_description" or intent=="find_DL205UPOV_content" or intent=="find_DL205UPOV_learningoutcomes" or intent=="find_DL205UPOV_teaching" or intent=="find_DL205UPOV_finalexam" or intent=="find_DL205UPOV_cert" or intent=="find_DL205UPOV_dur" or intent=="find_DL205UPOV_tuitionfees" or intent=="find_DL205UPOV_elig" or intent=="find_DL205UPOV_reg" or intent=="find_DL205UPOV_lang" or intent=="find_DL205UPOV_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl205upov_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL301_description" or intent=="find_DL301_content" or intent=="find_DL301_learningoutcomes" or intent=="find_DL301_teaching" or intent=="find_DL301_finalexam" or intent=="find_DL301_cert" or intent=="find_DL301_dur" or intent=="find_DL301_tuitionfees" or intent=="find_DL301_elig" or intent=="find_DL301_reg" or intent=="find_DL301_lang" or intent=="find_DL301_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl301_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL302_description" or intent=="find_DL302_content" or intent=="find_DL302_learningoutcomes" or intent=="find_DL302_teaching" or intent=="find_DL302_finalexam" or intent=="find_DL302_cert" or intent=="find_DL302_dur" or intent=="find_DL302_tuitionfees" or intent=="find_DL302_elig" or intent=="find_DL302_reg" or intent=="find_DL302_lang" or intent=="find_DL302_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl302_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL303_description" or intent=="find_DL303_content" or intent=="find_DL303_learningoutcomes" or intent=="find_DL303_teaching" or intent=="find_DL303_finalexam" or intent=="find_DL303_cert" or intent=="find_DL303_dur" or intent=="find_DL303_tuitionfees" or intent=="find_DL303_elig" or intent=="find_DL303_reg" or intent=="find_DL303_lang" or intent=="find_DL303_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl303_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL305UPOV_description" or intent=="find_DL305UPOV_content" or intent=="find_DL305UPOV_learningoutcomes" or intent=="find_DL305UPOV_teaching" or intent=="find_DL305UPOV_finalexam" or intent=="find_DL305UPOV_cert" or intent=="find_DL305UPOV_dur" or intent=="find_DL305UPOV_tuitionfees" or intent=="find_DL305UPOV_elig" or intent=="find_DL305UPOV_reg" or intent=="find_DL305UPOV_lang" or intent=="find_DL305UPOV_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl305upov_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL317_description" or intent=="find_DL317_content" or intent=="find_DL317_learningoutcomes" or intent=="find_DL317_teaching" or intent=="find_DL317_finalexam" or intent=="find_DL317_cert" or intent=="find_DL317_dur" or intent=="find_DL317_tuitionfees" or intent=="find_DL317_elig" or intent=="find_DL317_reg" or intent=="find_DL317_lang" or intent=="find_DL317_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl317_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL318_description" or intent=="find_DL318_content" or intent=="find_DL318_learningoutcomes" or intent=="find_DL318_teaching" or intent=="find_DL318_finalexam" or intent=="find_DL318_cert" or intent=="find_DL318_dur" or intent=="find_DL318_tuitionfees" or intent=="find_DL318_elig" or intent=="find_DL318_reg" or intent=="find_DL318_lang" or intent=="find_DL318_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl318_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL320_description" or intent=="find_DL320_content" or intent=="find_DL320_learningoutcomes" or intent=="find_DL320_teaching" or intent=="find_DL320_finalexam" or intent=="find_DL320_cert" or intent=="find_DL320_dur" or intent=="find_DL320_tuitionfees" or intent=="find_DL320_elig" or intent=="find_DL320_reg" or intent=="find_DL320_lang" or intent=="find_DL320_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl320_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL427_description" or intent=="find_DL427_content" or intent=="find_DL427_learningoutcomes" or intent=="find_DL427_teaching" or intent=="find_DL427_finalexam" or intent=="find_DL427_cert" or intent=="find_DL427_dur" or intent=="find_DL427_tuitionfees" or intent=="find_DL427_elig" or intent=="find_DL427_reg" or intent=="find_DL427_lang" or intent=="find_DL427_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl427_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL450_description" or intent=="find_DL450_content" or intent=="find_DL450_learningoutcomes" or intent=="find_DL450_teaching" or intent=="find_DL450_finalexam" or intent=="find_DL450_cert" or intent=="find_DL450_dur" or intent=="find_DL450_tuitionfees" or intent=="find_DL450_elig" or intent=="find_DL450_reg" or intent=="find_DL450_lang" or intent=="find_DL450_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl450_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL501_description" or intent=="find_DL501_content" or intent=="find_DL501_learningoutcomes" or intent=="find_DL501_teaching" or intent=="find_DL501_finalexam" or intent=="find_DL501_cert" or intent=="find_DL501_dur" or intent=="find_DL501_tuitionfees" or intent=="find_DL501_elig" or intent=="find_DL501_reg" or intent=="find_DL501_lang" or intent=="find_DL501_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl501_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL502_description" or intent=="find_DL502_content" or intent=="find_DL502_learningoutcomes" or intent=="find_DL502_teaching" or intent=="find_DL502_finalexam" or intent=="find_DL502_cert" or intent=="find_DL502_dur" or intent=="find_DL502_tuitionfees" or intent=="find_DL502_elig" or intent=="find_DL502_reg" or intent=="find_DL502_lang" or intent=="find_DL502_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl502_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL503_description" or intent=="find_DL503_content" or intent=="find_DL503_learningoutcomes" or intent=="find_DL503_teaching" or intent=="find_DL503_finalexam" or intent=="find_DL503_cert" or intent=="find_DL503_dur" or intent=="find_DL503_tuitionfees" or intent=="find_DL503_elig" or intent=="find_DL503_reg" or intent=="find_DL503_lang" or intent=="find_DL503_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl503_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL506_description" or intent=="find_DL506_content" or intent=="find_DL506_learningoutcomes" or intent=="find_DL506_teaching" or intent=="find_DL506_finalexam" or intent=="find_DL506_cert" or intent=="find_DL506_dur" or intent=="find_DL506_tuitionfees" or intent=="find_DL506_elig" or intent=="find_DL506_reg" or intent=="find_DL506_lang" or intent=="find_DL506_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl506_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL511_description" or intent=="find_DL511_content" or intent=="find_DL511_learningoutcomes" or intent=="find_DL511_teaching" or intent=="find_DL511_finalexam" or intent=="find_DL511_cert" or intent=="find_DL511_dur" or intent=="find_DL511_tuitionfees" or intent=="find_DL511_elig" or intent=="find_DL511_reg" or intent=="find_DL511_lang" or intent=="find_DL511_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl511_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL701_description" or intent=="find_DL701_content" or intent=="find_DL701_learningoutcomes" or intent=="find_DL701_teaching" or intent=="find_DL701_finalexam" or intent=="find_DL701_cert" or intent=="find_DL701_dur" or intent=="find_DL701_tuitionfees" or intent=="find_DL701_elig" or intent=="find_DL701_reg" or intent=="find_DL701_lang" or intent=="find_DL701_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl701_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL730_description" or intent=="find_DL730_content" or intent=="find_DL730_learningoutcomes" or intent=="find_DL730_teaching" or intent=="find_DL730_finalexam" or intent=="find_DL730_cert" or intent=="find_DL730_dur" or intent=="find_DL730_tuitionfees" or intent=="find_DL730_elig" or intent=="find_DL730_reg" or intent=="find_DL730_lang" or intent=="find_DL730_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dl730_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IP4TEACH_description" or intent=="find_IP4TEACH_content" or intent=="find_IP4TEACH_learningoutcomes" or intent=="find_IP4TEACH_teaching" or intent=="find_IP4TEACH_finalexam" or intent=="find_IP4TEACH_cert" or intent=="find_IP4TEACH_dur" or intent=="find_IP4TEACH_tuitionfees" or intent=="find_IP4TEACH_elig" or intent=="find_IP4TEACH_reg" or intent=="find_IP4TEACH_lang" or intent=="find_IP4TEACH_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_IP4TEACH_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_AICC_description" or intent=="find_AICC_content" or intent=="find_AICC_mode" or intent=="find_AICC_learningoutcomes" or intent=="find_AICC_teaching" or intent=="find_AICC_finalexam" or intent=="find_AICC_cert" or intent=="find_AICC_dur" or intent=="find_AICC_tuitionfees" or intent=="find_AICC_elig" or intent=="find_AICC_reg" or intent=="find_AICC_lang" or intent=="find_AICC_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_aicc_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPCC_description" or intent=="find_IPCC_content" or intent=="find_IPCC_mode" or intent=="find_IPCC_learningoutcomes" or intent=="find_IPCC_teaching" or intent=="find_IPCC_finalexam" or intent=="find_IPCC_cert" or intent=="find_IPCC_dur" or intent=="find_IPCC_tuitionfees" or intent=="find_IPCC_elig" or intent=="find_IPCC_reg" or intent=="find_IPCC_lang" or intent=="find_IPCC_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_ipcc_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_UNESCO_description" or intent=="find_UNESCO_content" or intent=="find_UNESCO_mode" or intent=="find_UNESCO_learningoutcomes" or intent=="find_UNESCO_teaching" or intent=="find_UNESCO_finalexam" or intent=="find_UNESCO_cert" or intent=="find_UNESCO_dur" or intent=="find_UNESCO_tuitionfees" or intent=="find_UNESCO_elig" or intent=="find_UNESCO_reg" or intent=="find_UNESCO_lang" or intent=="find_UNESCO_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_unesco_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTP_description" or intent=="find_IPDTP_content" or intent=="find_IPDTP_mode" or intent=="find_IPDTP_learningoutcomes" or intent=="find_IPDTP_teaching" or intent=="find_IPDTP_finalexam" or intent=="find_IPDTP_cert" or intent=="find_IPDTP_dur" or intent=="find_IPDTP_tuitionfees" or intent=="find_IPDTP_elig" or intent=="find_IPDTP_reg" or intent=="find_IPDTP_lang" or intent=="find_IPDTP_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_ipdtp_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLJTIP_description" or intent=="find_DLJTIP_content" or intent=="find_DLJTIP_mode" or intent=="find_DLJTIP_learningoutcomes" or intent=="find_DLJTIP_teaching" or intent=="find_DLJTIP_finalexam" or intent=="find_DLJTIP_cert" or intent=="find_DLJTIP_dur" or intent=="find_DLJTIP_tuitionfees" or intent=="find_DLJTIP_elig" or intent=="find_DLJTIP_reg" or intent=="find_DLJTIP_lang" or intent=="find_DLJTIP_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dljtip_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPE_description" or intent=="find_DLIPE_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_dlipe_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_TISCS_description" or intent=="find_TISCS_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_tiscs_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_EXP_description" or intent=="find_EXP_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_exp_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_WDAP_description" or intent=="find_WDAP_content" or intent=="find_WDAP_elig" or intent=="find_WDAP_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_wdap_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_WIPOConnect_description" or intent=="find_WIPOConnect_content" or intent=="find_WIPOConnect_elig" or intent=="find_WIPOConnect_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_WIPOConnect_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_ABC_description" or intent=="find_ABC_content" or intent=="find_ABC_elig" or intent=="find_ABC_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_abc_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTO_description" or intent=="find_IPDTO_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_ipdto_reverse_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))                                
        return []

class ActionFindCourseReverse2(Action):

    def name(self) -> Text:
        return "action_find_course_reverse_2"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:    

        find_course_type_ask = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type_ask'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type_ask) 
        find_course_type_ask = cursor.fetchone()      

        find_login_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query_goto) 
        find_login_query_goto = cursor.fetchone()      

        find_reg_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query_goto) 
        find_reg_query_goto = cursor.fetchone()      

        find_course_query_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query_goto) 
        find_course_query_goto = cursor.fetchone()    

        find_finalexam_goto = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_goto'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_goto) 
        find_finalexam_goto = cursor.fetchone()  

        utter_course_reverse_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_course_reverse_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_course_reverse_2) 
        utter_course_reverse_2 = cursor.fetchone()   

        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone()

        buttons = []

        buttons = [{"title": find_login_query_goto, "payload": "/find_login_query"},{"title": find_reg_query_goto, "payload": "/find_reg_query"},
                   {"title": find_course_type_ask, "payload": "/find_course_type"},{"title": find_course_query_goto, "payload": "/find_course_query"},
                   {"title": find_finalexam_goto, "payload": "/find_finalexam_query"},{"title": find_rollback, "payload": "/find_course_type"}]
                   
        dispatcher.utter_message(str(utter_course_reverse_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindGenLoginButtons(Action):

    def name(self) -> Text:
        return "action_find_genlogin_buttons"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:

        # intent = tracker.latest_message['intent'].get('name')
        
        find_genlogin_queries_1 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_genlogin_queries_1'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_genlogin_queries_1) 
        find_genlogin_queries_1 = cursor.fetchone()

        find_genlogin_queries_2 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_genlogin_queries_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_genlogin_queries_2) 
        find_genlogin_queries_2 = cursor.fetchone()
        
        find_genlogin_queries_3 = ("SELECT question FROM digital_admin_chatbot WHERE intent = 'find_genlogin_queries_3'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_genlogin_queries_3) 
        find_genlogin_queries_3 = cursor.fetchone()        
        
        utter_find_login_query_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_find_login_query_2'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_find_login_query_2) 
        utter_find_login_query_2 = cursor.fetchone()  
        
        find_rollback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rollback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_rollback) 
        find_rollback = cursor.fetchone() 

        buttons = []

        buttons = [{"title": find_genlogin_queries_1, "payload": "/find_genlogin_queries_1"},{"title": find_genlogin_queries_2, "payload": "/find_genlogin_queries_2"},
                   {"title": find_genlogin_queries_3, "payload": "/find_genlogin_queries_3"},{"title": find_rollback, "payload": "/back_action_find_greet_3"}]
        dispatcher.utter_message(str(utter_find_login_query_2).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []
        

class ActionFindGenLoginQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_genlogin_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_genlogin_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_genlogin_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_genlogin_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_genlogin_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_genlogin_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_genlogin_queries_3'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        return []

class ActionFindGenRegQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_genreg_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_genreg_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_genreg_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_genreg_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_genreg_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_genreg_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_genreg_queries_3'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_genreg_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_genreg_queries_4'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_genreg_queries_5":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_genreg_queries_5'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_genreg_queries_6":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_genreg_queries_6'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_genreg_queries_7":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_genreg_queries_7'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_genreg_queries_8":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_genreg_queries_8'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_genreg_queries_9":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_genreg_queries_9'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindAltRegQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_altreg_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_altreg_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_altreg_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_altreg_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_altreg_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_altreg_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_altreg_queries_3'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))           
        elif intent=="find_altreg_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_altreg_queries_4'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_altreg_queries_5":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_altreg_queries_5'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))           
        elif intent=="find_altreg_queries_6":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_altreg_queries_6'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_altreg_queries_7":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_altreg_queries_7'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))           
        elif intent=="find_altreg_queries_8":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_altreg_queries_8'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_altreg_queries_9":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_altreg_queries_9'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        return []     

class ActionFindUnenrollQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_unenroll_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_unenroll_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_unenroll_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []         

class ActionFindSecQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_sec_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_sec_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_sec_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_sec_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_sec_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_sec_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_sec_queries_3'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_sec_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_sec_queries_4'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_sec_queries_5":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_sec_queries_5'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_sec_queries_6":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_sec_queries_6'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_sec_queries_7":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_sec_queries_7'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_sec_queries_8":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_sec_queries_8'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_sec_queries_9":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_sec_queries_9'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_sec_queries_10":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_sec_queries_10'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindPaymQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_paym_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_paym_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_3'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_4'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_5":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_5'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_6":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_6'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_7":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_7'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_8":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_8'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_9":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_9'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_10":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_10'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_11":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_11'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_12":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_12'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_13":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_13'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_14":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_14'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_15":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_15'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_16":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_16'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_17":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_17'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_18":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_18'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_19":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_19'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_paym_queries_20":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_paym_queries_20'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []        

class ActionFindCourseAccessQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_courseaccess_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_courseaccess_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_courseaccess_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_courseaccess_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_courseaccess_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_courseaccess_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_courseaccess_queries_3'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_courseaccess_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_courseaccess_queries_4'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_courseaccess_queries_5":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_courseaccess_queries_5'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_courseaccess_queries_6":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_courseaccess_queries_6'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_courseaccess_queries_7":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_courseaccess_queries_7'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_courseaccess_queries_8":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_courseaccess_queries_8'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindCourseEvalQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_courseeval_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_courseeval_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_courseeval_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_courseeval_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_courseeval_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindCourseContentQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_coursecontent_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_coursecontent_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_coursecontent_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_coursecontent_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_3'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_coursecontent_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_4'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_coursecontent_queries_5":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_5'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_coursecontent_queries_6":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_6'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_coursecontent_queries_7":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_7'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_coursecontent_queries_8":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_8'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_coursecontent_queries_9":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_9'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_coursecontent_queries_10":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_10'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_coursecontent_queries_11":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_11'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_coursecontent_queries_12":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_12'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_coursecontent_queries_13":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_coursecontent_queries_13'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindTutorialsQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_tutorials_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_tutorials_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_tutorials_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_tutorials_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_tutorials_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_tutorials_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_tutorials_queries_3'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_tutorials_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_tutorials_queries_4'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_tutorials_queries_5":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_tutorials_queries_5'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_tutorials_queries_6":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_tutorials_queries_6'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_tutorials_queries_7":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_tutorials_queries_7'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_tutorials_queries_8":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_tutorials_queries_8'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_tutorials_queries_9":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_tutorials_queries_9'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_tutorials_queries_10":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_tutorials_queries_10'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindAssignmentsQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_assignments_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_assignments_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_assignments_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_assignments_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_assignments_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_assignments_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_assignments_queries_3'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_assignments_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_assignments_queries_4'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_assignments_queries_5":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_assignments_queries_5'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_assignments_queries_6":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_assignments_queries_6'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_assignments_queries_7":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_assignments_queries_7'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_assignments_queries_8":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_assignments_queries_8'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindLiveLecturesQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_livelectures_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_livelectures_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_livelectures_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_livelectures_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_livelectures_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_livelectures_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_livelectures_queries_3'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_livelectures_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_livelectures_queries_4'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindCertificateQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_certificate_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_certificate_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_certificate_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_certificate_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_certificate_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_certificate_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_certificate_queries_3'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_certificate_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_certificate_queries_4'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_certificate_queries_5":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_certificate_queries_5'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_certificate_queries_6":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_certificate_queries_6'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_certificate_queries_7":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_certificate_queries_7'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_certificate_queries_8":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_certificate_queries_8'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_certificate_queries_9":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_certificate_queries_9'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindDeadlineQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_deadline_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_deadline_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_deadline_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_deadline_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_deadline_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_deadline_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_deadline_queries_3'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_deadline_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_deadline_queries_4'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_deadline_queries_5":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_deadline_queries_5'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindAccessQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_access_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_access_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_access_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_access_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_access_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_access_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_access_queries_3'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_access_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_access_queries_4'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_access_queries_5":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_access_queries_5'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_access_queries_6":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_access_queries_6'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindGradeAppealQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_gradeappeal_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_gradeappeal_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_gradeappeal_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_gradeappeal_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_gradeappeal_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_gradeappeal_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_gradeappeal_queries_3'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_gradeappeal_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_gradeappeal_queries_4'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_gradeappeal_queries_5":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_gradeappeal_queries_5'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindRulesRegQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_rulesreg_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_rulesreg_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rulesreg_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_rulesreg_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rulesreg_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_rulesreg_queries_3":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rulesreg_queries_3'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_rulesreg_queries_4":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rulesreg_queries_4'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_rulesreg_queries_5":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rulesreg_queries_5'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_rulesreg_queries_6":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rulesreg_queries_6'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_rulesreg_queries_7":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rulesreg_queries_7'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_rulesreg_queries_8":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rulesreg_queries_8'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_rulesreg_queries_9":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rulesreg_queries_9'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_rulesreg_queries_10":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rulesreg_queries_10'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_rulesreg_queries_11":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_rulesreg_queries_11'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindDeferralsQueriesInfo(Action):

    def name(self) -> Text:
        return "action_find_deferrals_queries_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_deferrals_queries_1":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_deferrals_queries_1'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_deferrals_queries_2":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_deferrals_queries_2'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindNLUFullbackResponse(Action):

    def name(self) -> Text:
        return "action_find_nlu_fallback_response"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="nlu_fallback":
            nlu_fallback_1 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'nlu_fallback_1'")  
            cursor.execute(nlu_fallback_1)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

            nlu_fallback_2 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'nlu_fallback_2'")  
            cursor.execute(nlu_fallback_2)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionShareFeedbackRating(Action):

    def name(self) -> Text:
        return "action_share_feedback_rating"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the text
        if intent=="Feedback":

            share_rating_feedback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'share_rating_feedback'")  
            cursor = connection.cursor(buffered=True)
            cursor.execute(share_rating_feedback) 
            share_rating_feedback = cursor.fetchone()      

            one_star_feedback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'one_star_feedback'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(one_star_feedback) 
            one_star_feedback = cursor.fetchone()      

            two_star_feedback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'two_star_feedback'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(two_star_feedback) 
            two_star_feedback = cursor.fetchone()      

            three_star_feedback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'three_star_feedback'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(three_star_feedback) 
            three_star_feedback = cursor.fetchone()      

            four_star_feedback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'four_star_feedback'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(four_star_feedback) 
            four_star_feedback = cursor.fetchone()      

            five_star_feedback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'five_star_feedback'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(five_star_feedback) 
            five_star_feedback = cursor.fetchone()      

            buttons = []

            buttons = [{"title": five_star_feedback, "payload": "/five_star_feedback"},{"title": four_star_feedback, "payload": "/four_star_feedback"},
                    {"title": three_star_feedback, "payload": "/three_star_feedback"},{"title": two_star_feedback, "payload": "/two_star_feedback"},
                    {"title": one_star_feedback, "payload": "/one_star_feedback"}]
                    
            dispatcher.utter_message(str(share_rating_feedback).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)


        return []

class ActionShareFeedbackComment(Action):

    def name(self) -> Text:
        return "action_share_feedback_comment"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the text

        share_comment_feedback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'share_comment_feedback'")  
        cursor = connection.cursor(buffered=True)
        cursor.execute(share_comment_feedback) 
        share_comment_feedback = cursor.fetchone()      

        share_comment_feedback_yes = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'share_comment_feedback_yes'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(share_comment_feedback_yes) 
        share_comment_feedback_yes = cursor.fetchone()           

        exit_feedback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'exit_feedback'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(exit_feedback) 
        exit_feedback = cursor.fetchone()  

        buttons = []

        buttons = [{"title": share_comment_feedback_yes, "payload": "/share_comment_feedback_yes"},{"title": exit_feedback, "payload": "/exit_feedback_with_rating"},]
                    
        dispatcher.utter_message(str(share_comment_feedback).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionShareFeedbackCommentResult(Action):

    def name(self) -> Text:
        return "action_share_feedback_comment_result"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the text
        if intent=="share_comment_feedback_yes":

            give_comment_feedback = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'give_comment_feedback'")  
            cursor = connection.cursor(buffered=True)
            cursor.execute(give_comment_feedback) 
            give_comment_feedback = cursor.fetchone()      
            dispatcher.utter_message(str(give_comment_feedback).strip('("",)').strip("'").replace('\',', ''))

        elif intent=="exit_feedback_with_rating":

            exit_feedback_with_rating = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'exit_feedback_with_rating'")  
            cursor = connection.cursor(buffered=True)
            cursor.execute(exit_feedback_with_rating) 
            exit_feedback_with_rating = cursor.fetchone()      
            dispatcher.utter_message(str(exit_feedback_with_rating).strip('("",)').strip("'").replace('\',', ''))

            find_course_type = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_course_type) 
            find_course_type = cursor.fetchone()

            find_login_query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_login_query) 
            find_login_query = cursor.fetchone()
            
            find_reg_query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_reg_query) 
            find_reg_query = cursor.fetchone()        

            find_course_query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_course_query) 
            find_course_query = cursor.fetchone()  

            find_finalexam_query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_query'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(find_finalexam_query) 
            find_finalexam_query = cursor.fetchone()          

            utter_greet_3 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_greet_3'")
            cursor = connection.cursor(buffered=True)
            cursor.execute(utter_greet_3) 
            utter_greet_3 = cursor.fetchone()        

            buttons = []

            buttons = [{"title": find_course_type, "payload": "/find_course_type"},{"title": find_login_query, "payload": "/find_login_query"},
                    {"title": find_reg_query, "payload": "/find_reg_query"},{"title": find_course_query, "payload": "/find_course_query"},
                    {"title": find_finalexam_query, "payload": "/find_finalexam_query"}]
            
            dispatcher.utter_message(str(utter_greet_3).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ValidateSurveyForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_survey_form"

    def validate_open_feedback(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List:
        """Validate `open_feedback` value."""

        # If the name is super short, it might be wrong.
        print(f"Open Feedback given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 3:
            dispatcher.utter_message(text=f"That's a very short feedback. I'm assuming you mis-spelled. Please try again by leaving your feedback comment below.")
            return {"open_feedback": None}
        else:
            return {"open_feedback": slot_value}

class ActionSubmitFeedback(Action): 

    def name(self) -> Text: 
        return "action_submit_feedback"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:                                 
            
        FeedbackUpdate(tracker.get_slot("open_rating"),tracker.get_slot("open_feedback")) 
                                           
        return []

class ActionShareFeedbackFinal(Action):

    def name(self) -> Text:
        return "action_share_feedback_final"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        cursor = connection.cursor(buffered=True)

        exit_feedback_with_rating_comment = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'exit_feedback_with_rating_comment'")  
        cursor = connection.cursor(buffered=True)
        cursor.execute(exit_feedback_with_rating_comment) 
        exit_feedback_with_rating_comment = cursor.fetchone()      
        dispatcher.utter_message(str(exit_feedback_with_rating_comment).strip('("",)').strip("'").replace('\',', ''))

        find_course_type = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_type'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_type) 
        find_course_type = cursor.fetchone()

        find_login_query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_login_query'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_login_query) 
        find_login_query = cursor.fetchone()
            
        find_reg_query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_reg_query'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_reg_query) 
        find_reg_query = cursor.fetchone()        

        find_course_query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_course_query'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_course_query) 
        find_course_query = cursor.fetchone()  

        find_finalexam_query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_finalexam_query'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(find_finalexam_query) 
        find_finalexam_query = cursor.fetchone()          

        utter_greet_3 = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'utter_greet_3'")
        cursor = connection.cursor(buffered=True)
        cursor.execute(utter_greet_3) 
        utter_greet_3 = cursor.fetchone()        

        buttons = []

        buttons = [{"title": find_course_type, "payload": "/find_course_type"},{"title": find_login_query, "payload": "/find_login_query"},
                  {"title": find_reg_query, "payload": "/find_reg_query"},{"title": find_course_query, "payload": "/find_course_query"},
                   {"title": find_finalexam_query, "payload": "/find_finalexam_query"}]
            
        dispatcher.utter_message(str(utter_greet_3).strip('("",)').strip("'").replace('\',', ''), buttons=buttons)

        return []

class ActionFindGoodbyeResponse(Action):

    def name(self) -> Text:
        return "action_find_goodbye_response"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="nlu_goodbye":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'nlu_goodbye'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))

        return []

class ActionFindAllCourseInfo(Action):

    def name(self) -> Text:
        return "action_find_all_course_info"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')
        cursor = connection.cursor(buffered=True)

        # retrieve the correct genlogin utterance dependent on the intent
        if intent=="find_DL001_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL001_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL001_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL001_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL001_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL001_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL001_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL001_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL001_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL001_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL001_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL001_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL001_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL001_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL001_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL001_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL001_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL001_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL001_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL001_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL001_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL001_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL001_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL001_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101PCT_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101PCT_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101PCT_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101PCT_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101PCT_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101PCT_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101PCT_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101PCT_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101PCT_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101PCT_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101PCT_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101PCT_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101PCT_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101PCT_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101PCT_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101PCT_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101PCT_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101PCT_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101PCT_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101PCT_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101PCT_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101PCT_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL101PCT_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL101PCT_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL170_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL170_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL170_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL170_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL170_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL170_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL170_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL170_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL170_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL170_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL170_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL170_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL170_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL170_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL170_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL170_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL170_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL170_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL170_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL170_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL170_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL170_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL170_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL170_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL177_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL177_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL177_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL177_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL177_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL177_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL177_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL177_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL177_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL177_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL177_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL177_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL177_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL177_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL177_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL177_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL177_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL177_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL177_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL177_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL177_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL177_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL177_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL177_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPPAN_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLIPPAN_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPPAN_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLIPPAN_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPPAN_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLIPPAN_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPPAN_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLIPPAN_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPPAN_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLIPPAN_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPPAN_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLIPPAN_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPPAN_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLIPPAN_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPPAN_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLIPPAN_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPPAN_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLIPPAN_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPPAN_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLIPPAN_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPPAN_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLIPPAN_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPPAN_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLIPPAN_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL201_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL201_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL201_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL201_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL201_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL201_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL201_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL201_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL201_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL201_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL201_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL201_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL201_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL201_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL201_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL201_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL201_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL201_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL201_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL201_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL201_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL201_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL201_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL201_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL203_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL203_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL203_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL203_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL203_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL203_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL203_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL203_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL203_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL203_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL203_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL203_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL203_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL203_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL203_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL203_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL203_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL203_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL203_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL203_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL203_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL203_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL203_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL203_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL205UPOV_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL205UPOV_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL205UPOV_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL205UPOV_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL205UPOV_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL205UPOV_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL205UPOV_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL205UPOV_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL205UPOV_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL205UPOV_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL205UPOV_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL205UPOV_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL205UPOV_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL205UPOV_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL205UPOV_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL205UPOV_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL205UPOV_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL205UPOV_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL205UPOV_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL205UPOV_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL205UPOV_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL205UPOV_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL205UPOV_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL205UPOV_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL301_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL301_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL301_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL301_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL301_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL301_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL301_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL301_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL301_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL301_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL301_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL301_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL301_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL301_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL301_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL301_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL301_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL301_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL301_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL301_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL301_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL301_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL301_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL301_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL302_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL302_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL302_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL302_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL302_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL302_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL302_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL302_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL302_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL302_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL302_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL302_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL302_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL302_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL302_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL302_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL302_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL302_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL302_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL302_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL302_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL302_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL302_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL302_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL303_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL303_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL303_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL303_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL303_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL303_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL303_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL303_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL303_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL303_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL303_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL303_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL303_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL303_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL303_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL303_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL303_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL303_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL303_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL303_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL303_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL303_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL303_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL303_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL305UPOV_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL305UPOV_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL305UPOV_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL305UPOV_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL305UPOV_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL305UPOV_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL305UPOV_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL305UPOV_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL305UPOV_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL305UPOV_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL305UPOV_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL305UPOV_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL305UPOV_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL305UPOV_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL305UPOV_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL305UPOV_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL305UPOV_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL305UPOV_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL305UPOV_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL305UPOV_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL305UPOV_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL305UPOV_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL305UPOV_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL305UPOV_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL317_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL317_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL317_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL317_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL317_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL317_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL317_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL317_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL317_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL317_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL317_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL317_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL317_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL317_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL317_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL317_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL317_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL317_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL317_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL317_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL317_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL317_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL317_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL317_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL318_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL308_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL318_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL318_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL318_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL318_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL318_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL318_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL318_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL318_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL318_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL318_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL318_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL318_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL318_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL318_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL318_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL318_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL318_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL318_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL318_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL318_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL318_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL318_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL320_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL320_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL320_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL320_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL320_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL320_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL320_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL320_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL320_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL320_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL320_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL320_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL320_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL320_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL320_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL320_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL320_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL320_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL320_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL320_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL320_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL320_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL320_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL320_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL427_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL427_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL427_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL427_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL427_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL427_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL427_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL427_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL427_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL427_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL427_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL427_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL427_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL427_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL427_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL427_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL427_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL427_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL427_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL427_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL427_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL427_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL427_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL427_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL450_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL450_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL450_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL450_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL450_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL450_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL450_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL450_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL450_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL450_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL450_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL450_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL450_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL450_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL450_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL450_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL450_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL450_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL450_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL450_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL450_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL450_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL450_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL450_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL501_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL501_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL501_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL501_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL501_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL501_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL501_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL501_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL501_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL501_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL501_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL501_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL501_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL501_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL501_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL501_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL501_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL501_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL501_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL501_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL501_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL501_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL501_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL501_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL502_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL502_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL502_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL502_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL502_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL502_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL502_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL502_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL502_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL502_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL502_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL502_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL502_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL502_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL502_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL502_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL502_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL502_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL502_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL502_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL502_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL502_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL502_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL502_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL503_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL503_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL503_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL503_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL503_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL503_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL503_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL503_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL503_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL503_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL503_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL503_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL503_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL503_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL503_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL503_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL503_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL503_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL503_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL503_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL503_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL503_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL503_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL503_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL506_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL506_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL506_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL506_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL506_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL506_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL506_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL506_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL506_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL506_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL506_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL506_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL506_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL506_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL506_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL506_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL506_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL506_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL506_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL506_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL506_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL506_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL506_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL506_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL511_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL511_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL511_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL511_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL511_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL511_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL511_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL511_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL511_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL511_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL511_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL511_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL511_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL511_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL511_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL511_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL511_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL511_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL511_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL511_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL511_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL511_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL511_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL511_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL701_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL701_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL701_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL701_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL701_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL701_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL701_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL701_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL701_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL701_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL701_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL701_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL701_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL701_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL701_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL701_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL701_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL701_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL701_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL701_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL701_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL701_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL701_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL701_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL730_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL730_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL730_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL730_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL730_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL730_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL730_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL730_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL730_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL730_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL730_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL730_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL730_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL730_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL730_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL730_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL730_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL730_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL730_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL730_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL730_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL730_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DL730_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DL730_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IP4TEACH_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IP4TEACH_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IP4TEACH_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IP4TEACH_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IP4TEACH_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IP4TEACH_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IP4TEACH_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IP4TEACH_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IP4TEACH_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IP4TEACH_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IP4TEACHcert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IP4TEACHcert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IP4TEACH_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IP4TEACH_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IP4TEACH_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IP4TEACH_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IP4TEACH_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IP4TEACH_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IP4TEACH_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IP4TEACH_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IP4TEACH_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IP4TEACH_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IP4TEACH_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IP4TEACH_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_AICC_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_AICC_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_AICC_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_AICC_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_AICC_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_AICC_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_AICC_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_AICC_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_AICC_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_AICC_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_AICC_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_AICC_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_AICC_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_AICC_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_AICC_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_AICC_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_AICC_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_AICC_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_AICC_mode":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_AICC_mode'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_AICC_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_AICC_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_AICC_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_AICC_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_AICC_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_AICC_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPCC_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPCC_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPCC_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPCC_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPCC_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPCC_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPCC_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPCC_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPCC_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPCC_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPCC_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPCC_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPCC_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPCC_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPCC_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPCC_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPCC_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPCC_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPCC_mode":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPCC_mode'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPCC_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPCC_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPCC_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPCC_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPCC_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPCC_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_UNESCO_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_UNESCO_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_UNESCO_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_UNESCO_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_UNESCO_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_UNESCO_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_UNESCO_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_UNESCO_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_UNESCO_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_UNESCO_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_UNESCO_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_UNESCO_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_UNESCO_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_UNESCO_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_UNESCO_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_UNESCO_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_UNESCO_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_UNESCO_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_UNESCO_mode":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_UNESCO_mode'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_UNESCO_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_UNESCO_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_UNESCO_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_UNESCO_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_UNESCO_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_UNESCO_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTP_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPDTP_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTP_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPDTP_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTP_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPDTP_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTP_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPDTP_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTP_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPDTP_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTP_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPDTP_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTP_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPDTP_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTP_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPDTP_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTP_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPDTP_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTP_mode":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPDTP_mode'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTP_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPDTP_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTP_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPDTP_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTP_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPDTP_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLJTIP_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLJTIP_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLJTIP_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLJTIP_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLJTIP_learningoutcomes":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLJTIP_learningoutcomes'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLJTIP_teaching":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLJTIP_teaching'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLJTIP_finalexam":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLJTIP_finalexam'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLJTIP_cert":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLJTIP_cert'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLJTIP_dur":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLJTIP_dur'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLJTIP_tuitionfees":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLJTIP_tuitionfees'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLJTIP_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLJTIP_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLJTIP_mode":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLJTIP_mode'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLJTIP_reg":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLJTIP_reg'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLJTIP_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLJTIP_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLJTIP_nextsess":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLJTIP_nextsess'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPE_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLIPE_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_DLIPE_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_DLIPE_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_TISCS_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_TISCS_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_TISCS_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_TISCS_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_EXP_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_EXP_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_EXP_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_EXP_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_WDAP_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_WDAP_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_WDAP_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_WDAP_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_WDAP_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_WDAP_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_WDAP_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_WDAP_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_WIPOConnect_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_WIPOConnect_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_WIPOConnect_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_WIPOConnect_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_WIPOConnect_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_WIPOConnect_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_WIPOConnect_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_WIPOConnect_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_ABC_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_ABC_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_ABC_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_ABC_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_ABC_elig":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_ABC_elig'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_ABC_lang":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_ABC_lang'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTO_description":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPDTO_description'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        elif intent=="find_IPDTO_content":
            query = ("SELECT response FROM digital_admin_chatbot WHERE intent = 'find_IPDTO_content'")  
            cursor.execute(query)       
            for (response) in cursor:
                dispatcher.utter_message(str(response).strip('("",)').strip("'").replace('\',', ''))
        return []
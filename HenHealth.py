from twilio.rest import Client
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import sqlite3
from sqlite3 import Error
# import mysql.connector
from kivy.properties import StringProperty
import pandas as pd

class Welcome(Screen):
    pass

class Create(Screen):
    firstname = ObjectProperty(None)
    lastname = ObjectProperty(None)
    phone = ObjectProperty(None)
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    passwordCheck = ObjectProperty(None)

    def submit(self):
        """make this def check password congruency, ensure password meets at least word count,
        and username/phone number isn't already in use"""
        firstname = self.firstname.text
        lastname = self.lastname.text
        phoneNum = self.phone.text
        username = self.username.text
        password = self.password.text
        passwordCheck = self.passwordCheck.text

        """
        if (phoneNum != "") and (username != "") and (password != ""):
            if (username not in <db.username>)
                if (phoneNum not in <db.phoneNumber>) and (len(phoneNum) == 10): 
                    if (password == passwordCheck):
                        db.add_user(firstname, lastname, phoneNum, email, username, password)

                        self.reset()
                        sm.current = "login"
                    else:
                        pass_match()
                else:
                    num_invalid()
            else:
                user_taken()
        else:
            empty_Input()

    def reset(self):
        self.firstname.text = ""
        self.lastname.text = ""
        self.phone.text = ""
        self.username.text = ""
        self.password.text = ""
        self.passwordCheck.text = ""
        """
    
        pass


class Login(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    pass
    def logbtn(self):
        username = self.username.text
        password = self.password.text
        """
        if db.validate(username, password):
            self.reset()
            sm.current = "main"
        else:
            show_invalid()

    def reset(self):
        self.username.text = ""
        self.password.text = ""
        """
        pass

class Menu(Screen):
    pass

class Interaction(Screen):
    def btn(self):
        show_success()
        """logs all users inputted into database of 
        users listed in the last two weeks with date
        of submit"""
    pass

class Evaluation(Screen):

    def submit(self):
        show_covid_message()

class Alert(Screen):
    def redbtn(self):
        show_success()
        """
        
        """
    pass

class WindowManager(ScreenManager):
    pass

class Invalid(FloatLayout):
    pass

class Success(FloatLayout):
    pass

class UserTaken(FloatLayout):
    pass

class NumInvalid(FloatLayout):
    pass

class PassMatch(FloatLayout):
    pass

class EmptyInput(FloatLayout):
    pass

class ConfirmPopup(GridLayout):
	text = StringProperty()
	
	def __init__(self,**kwargs):
		self.register_event_type('on_answer')
		super(ConfirmPopup,self).__init__(**kwargs)
		
	def on_answer(self, *args):
		pass
    	
class covidEval(FloatLayout):
    pass

def show_invalid():
    """
    Pop-up shown if the login information is incorrect.
    """
    show = Invalid()
    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400,400))
    popupWindow.open()

def show_success():
    """
    Pop-up shown if action successfully completed.
    """
    show = Success()
    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400,400))
    popupWindow.open()

def user_taken():
    """
    Pop-up shown if the username inputted in the 
    create account window is already in use.
    """
    show = UserTaken()
    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400,400))
    popupWindow.open()

def num_invalid():
    """
    Pop-up shown if the number inputted in the 
    create account window is already in use.
    """
    show = NumInvalid()
    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400,400))
    popupWindow.open()

def pass_match():
    """
    Pop-up shown if the passwords inputted in the 
    create account window do not match.
    """
    show = PassMatch()
    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400,400))
    popupWindow.open()

def empty_input():
    """
    Pop-up shown if the passwords inputted in the 
    create account window do not match.
    """
    show = EmptyInput()
    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400,400))
    popupWindow.open()

def show_covid_message():
    """
    Pop-up shown if the user clicks yes to any symptom to say they shoud get tested for covid
    """
    show = covidEval()
    popupWindow = Popup(title="Covid Notification", content=show, size_hint=(None, None), size=(400,400))
    popupWindow.open()

kv = Builder.load_file("mymain.kv")

class MyMainApp(App):
    def build(self):
        return kv

def send_text(phoneNum):
    # Your Account SID from twilio.com/console
    account_sid = "ACef3d4d9489ac114d6accb66f2caf6b4b"
    # Your Auth Token from twilio.com/console
    auth_token  = "e1e88d59195de5334fcbfefb398e6657"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+12408559357",      # replace number with number from database
        from_="+14157994032",   # free trial number
        body="Someone you've been in contact with has contracted COVID-19. Please take the necessary health precautions to prevent the spread.")

    print(message.sid)

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_connection(r"C:\Users\chris\OneDrive\Desktop\sqlite\db\main.db")
    create_connection(r"C:\Users\chris\OneDrive\Desktop\sqlite\db\user.db")
    MyMainApp().run()

    # row = cursor.fetchone()
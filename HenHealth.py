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

class Welcome(Screen):
    pass

class Login(Screen):
    def btn(self):
        show_popup()

class Menu(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class P(FloatLayout):
    pass

def show_popup():
    show = P()
    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400,400))
    popupWindow.open()

class MyGrid(Widget):
    firstname = ObjectProperty(None)
    lastname = ObjectProperty(None)
    phone = ObjectProperty(None)
    email = ObjectProperty(None)
    username = ObjectProperty(None)

    def btn(self):
        firstname = self.firstname.text
        lastname = self.lastname.text
        phoneNum = self.phone.text
        email = self.email.text
        username = self.username.text

        #if statement to go through database and ensure username is available and number is unused

        #load data into database
    pass

kv = Builder.load_file("my.kv")

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
    create_connection(r"C:\Users\chris\OneDrive\Desktop\sqlite\db\HenHealth.db")
    MyMainApp().run()
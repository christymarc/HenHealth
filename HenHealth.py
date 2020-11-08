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
from kivy.uix.boxlayout import BoxLayout
import sqlite3
from sqlite3 import Error
#from kivy.uix.video import VideoPlayer
# import mysql.connector
from kivy.properties import StringProperty
import pandas as pd
import numpy as np
from database import *

# image of cecil and colors of blue and orange
# https://ih1.redbubble.net/image.752005083.1066/st,small,507x507-pad,600x600,f8f8f8.u4.jpg
# ripped cecil  
# aimg = AsyncImage(source='http://mywebsite.com/logo.png')

class Welcome(Screen):
    def img(self):
        welcome = Welcome(direction='right')
        img = AsyncImage(source = 'https://ih1.redbubble.net/image.752005083.1066/st,small,507x507-pad,600x600,f8f8f8.u4.jpg')
        img.pos = (300,300)
        welcome.add_widget(img)
        return img

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

        if (phoneNum != "") and (username != "") and (password != ""):
            for index, row in df_main.iterrows():
                if (username not in row['username']):
                    if (phoneNum not in row['phonenumber']) and (len(phoneNum) == 10) and phoneNum.isdigit(): 
                        if (password == passwordCheck):
                            df = pd.DataFrame([username, password, firstname, lastname, phoneNum], columns = ['username','password','firstname','lastname','phonenumber'])
                            df_main.append(df, ignore_index=True)
                            print(df_main)
                            self.reset()
                        else:
                            pass_match()
                    else:
                        num_invalid()
                else:
                    user_taken()
        else:
            empty_input()
    
    def reset(self):
        self.firstname.text = ""
        self.lastname.text = ""
        self.phone.text = ""
        self.username.text = ""
        self.password.text = ""
        self.passwordCheck.text = ""


class Login(Screen):
    
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        username = self.username.text
        password = self.password.text
        for index, row in df_main.iterrows():
            if username == row['username']:
                if df_main.loc[index, 'password']:
                    #lets you go to menu
                    self.reset()
                else:
                    show_invalid()
            else:
                show_invalid()
    
    def reset(self):
        self.username.text = ""
        self.password.text = ""

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
    username = ObjectProperty(None)
    def redbtn(self):
        show_success()
        username = self.username.text
        for index, row in df_user.iterrows():
            if username == row['username'] and row['time'] <= 14:
                contact = df_user.loc[index, 'contact']
                for index, row in df_main.iterrows():
                    if contact == row['username']:
                        send_text(df_main.loc[index, 'phonenumber'])


class WindowManager(ScreenManager):
    pass

def show_invalid():
    """
    Pop-up shown if the login information is incorrect.
    """
    box = BoxLayout(orientation = 'vertical', padding = (10))
    box.add_widget(Label(text = "The username you inputted either does \nnot exist in out database or the pass\n word you inputted is incorrect."))
    btn1 = Button(text = "Ok")
    box.add_widget(btn1)
    popup = Popup(title="Invalid Login", title_size= (30), title_align = 'center', content = box,size_hint=(None, None), size=(430, 200), auto_dismiss = True)
    btn1.bind(on_press = popup.dismiss)
    popup.open()

def show_success():
    """
    Pop-up shown if action successfully completed.
    """
    box = BoxLayout(orientation = 'vertical', padding = (10))
    box.add_widget(Label(text = ""))
    btn1 = Button(text = "Ok")
    box.add_widget(btn1)
    popup = Popup(title="Action Successful", title_size= (30), title_align = 'center', content = box,size_hint=(None, None), size=(430, 200), auto_dismiss = True)
    btn1.bind(on_press = popup.dismiss)
    popup.open()

def user_taken():
    """
    Pop-up shown if the username inputted in the 
    create account window is already in use.
    """
    box = BoxLayout(orientation = 'vertical', padding = (10))
    box.add_widget(Label(text = "That username is already in use.\nPlease try another."))
    btn1 = Button(text = "Ok")
    box.add_widget(btn1)
    popup = Popup(title="Username Error", title_size= (30), title_align = 'center', content = box,size_hint=(None, None), size=(430, 200), auto_dismiss = True)
    btn1.bind(on_press = popup.dismiss)
    popup.open()

def num_invalid():
    """
    Pop-up shown if the number inputted in the 
    create account window is already in use.
    """
    box = BoxLayout(orientation = 'vertical', padding = (10))
    box.add_widget(Label(text = "The phone number you inputted is either already in use or\nit is invalid. Do you already have an account?\nIf not please ensure the number inputted is correct."))
    btn1 = Button(text = "Ok")
    box.add_widget(btn1)
    popup = Popup(title="Phone Number Input Invalid", title_size= (30), title_align = 'center', content = box,size_hint=(None, None), size=(430, 200), auto_dismiss = True)
    btn1.bind(on_press = popup.dismiss)
    popup.open()

def pass_match():
    """
    Pop-up shown if the passwords inputted in the 
    create account window do not match.
    """
    box = BoxLayout(orientation = 'vertical', padding = (10))
    box.add_widget(Label(text = "The passwords inputted do not match.\nPlease ensure that they match."))
    btn1 = Button(text = "Ok")
    box.add_widget(btn1)
    popup = Popup(title="Password Error", title_size= (30), title_align = 'center', content = box,size_hint=(None, None), size=(430, 200), auto_dismiss = True)
    btn1.bind(on_press = popup.dismiss)
    popup.open()

def empty_input():
    """
    Pop-up shown if the passwords inputted in the 
    create account window do not match.
    """
    box = BoxLayout(orientation = 'vertical', padding = (10))
    box.add_widget(Label(text = "You left required spaces blank. Please make\nsure to input a username, phone number, and\npassword."))
    btn1 = Button(text = "Ok")
    box.add_widget(btn1)
    popup = Popup(title="Empty Input Error", title_size= (30), title_align = 'center', content = box,size_hint=(None, None), size=(430, 200), auto_dismiss = True)
    btn1.bind(on_press = popup.dismiss)
    popup.open()

def show_covid_message():
    """
    Pop-up shown if the user clicks yes to any symptom to say they shoud get tested for covid
    """
    box = BoxLayout(orientation = 'vertical', padding = (10))
    box.add_widget(Label(text = "You should get tested for Covid-19"))
    btn1 = Button(text = "Ok")
    box.add_widget(btn1)
    popup = Popup(title="Covid Notification", title_size= (30), title_align = 'center', content = box,size_hint=(None, None), size=(430, 200), auto_dismiss = True)
    btn1.bind(on_press = popup.dismiss)
    popup.open()

def buttonClose(self):
    self.popup.dismiss

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
        to="+1" + phoneNum,     # replace number with number from database
        from_="+14157994032",   # free trial number
        body="Someone you've been in contact with has contracted COVID-19. Please take the necessary health precautions to prevent the spread.")

    print(message.sid)

if __name__ == "__main__":
    MyMainApp().run()
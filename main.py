from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from datetime import datetime
import json

        

Builder.load_file('design.kv')
class HomeScreen(Screen):
    def loginpress(self):
        self.manager.current = "loginscreen"
    def signuppress(self):
        self.manager.current = "signupscreen"    
class LoginScreen(Screen):
    def go_back_to_welcome(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'homescreen'
    def login(self, uname, pword):
        with open("users.json", "r") as file:
            users = json.load(file)
            if uname in users and users[uname]['password'] == pword:
                self.manager.current = "dicscreen"
            else:
                self.ids.login_wrong.text = "Incorrect username or password"
class SignUpScreen(Screen):
     def add_user(self,uname,pword):
        with open("users.json") as file:
            users = json.load(file)  
                
            users[uname] = {'username':uname,'password':pword,'created':datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        with open("users.json", "w") as file:
            json.dump(users,file)     
            self.manager.transition.direction = 'right'
            self.manager.current = "sign_up_screen_success"     
     def go_back_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current="loginscreen"           
class SignUpScreenSuccess(Screen):
    def go_back_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current="loginscreen"                        
class DicScreen(Screen):
    def log_out(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "loginscreen"
    def translate(self):
     data = json.load(open('data.json'))   
     self.ids.word.text = self.ids.word.text.lower() 
     if self.ids.word.text in data:
         
        
      self.ids.translated.text = str(data[self.ids.word.text])
    
     else:
      self.ids.translated.text = "No such word found"
class ImageButton(ButtonBehavior,HoverBehavior,Image):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
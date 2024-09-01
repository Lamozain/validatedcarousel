import os
from kivy.app import App  
from kivy.uix.boxlayout import BoxLayout  
from kivy.uix.screenmanager import ScreenManager, Screen  
from kivy.uix.label import Label  
from kivy.uix.textinput import TextInput  
from kivy.uix.button import Button  
from kivy.uix.carousel import Carousel 
from kivy.uix.image import Image 

class LoginScreen(Screen):  
    def __init__(self, **kwargs):  
        super(LoginScreen, self).__init__(**kwargs)  
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10) 

        self.intro_text = Label(text='Welcome to the Nuptial Viewer App. \nEnter your password and username to proceed.\nHappy Viewing!', font_size=25,halign="center",color="teal")
        self.username_input = TextInput(hint_text='Enter your username here', multiline=False)  
        self.password_input = TextInput(hint_text='Enter your password here', multiline=False, password=True)  
        login_button = Button(text='Login')  
        login_button.bind(on_press=self.validate_login)  

        layout.add_widget(self.intro_text)
        layout.add_widget(self.username_input)  
        layout.add_widget(self.password_input)  
        layout.add_widget(login_button)  
        
        self.add_widget(layout)  

    def validate_login(self, instance):  
        username = self.username_input.text  
        password = self.password_input.text  
        
        # Simple validation (replace with actual validation logic)  
        if username == "Theomofaiyes" and password == "justamo":  
            self.manager.current = 'carousel'  # switch to carousel screen  
        else:  
            self.manager.get_screen('login').add_widget(Label(text='Invalid credentials', color=(1, 0, 0, 1), font_size=40))  

class CarouselScreen(Screen):  
    def __init__(self, **kwargs):  
        super(CarouselScreen, self).__init__(**kwargs)  
        layout = Carousel()  
# Assuming you have images in "carousel/" directory  
        image_dir = "images/"  
        for filename in os.listdir(image_dir):  
            if filename.endswith(".png") or filename.endswith(".jpg"):  
                img = Image(source=os.path.join(image_dir, filename))
                img.allow_stretch=True
                img.keep_ratio = True
                layout.add_widget(img)   

        self.add_widget(layout)  

class NuptialViewerApp(App):  
    def build(self):  
        sm = ScreenManager()  
        sm.add_widget(LoginScreen(name='login'))  
        sm.add_widget(CarouselScreen(name='carousel'))  

        return sm  

if __name__ == '__main__':  
    NuptialViewerApp().run()
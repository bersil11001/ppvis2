from USER import *
from homelibrary import *
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.widget import MDWidget
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.imagelist import imagelist
class textIN(MDTextField):
    def __init__(self, **kwargs):
        super(textIN,self).__init__( **kwargs)
        self.halign = "center"
        self.valign = "center"
        
class MyButton(MDFlatButton):
    def __init__(self,**kwargs):
        super(MyButton,self).__init__(**kwargs)
     


class Home(MDBoxLayout):
    def __init__(self,**kwargs) -> None:
        super(Home,self).__init__(**kwargs)
        self.orientation ='vertical'
        self.halign = 'center'
        self.add_widget(MyButton(text="Home Page"))
        self.signIn = MyButton(text="Вход")
        self.signIn.bind(on_press =self.enter)
        self.add_widget(self.signIn)
        self.registr=MyButton(text ="Регистрация")
        self.registr.bind(on_press= self.registration)
        self.add_widget(self.registr)
        
    def home_page(self,instance):
        self.clear_widgets()
        self.add_widget(MyButton(text="Home Page"))
        self.signIn = MyButton(text="Вход")
        self.signIn.bind(on_press =self.enter)
        self.add_widget(self.signIn)
        self.registr=MyButton(text ="Регистрация")
        self.registr.bind(on_press= self.registration)
        self.add_widget(self.registr)

        
    def registration(self,instance):
        self.clear_widgets()
        self.email=textIN(text="Email")
        self.name =textIN(text ="Name")
        self.password=textIN(text ="password")
        self.add_widget(self.email)
        self.add_widget(self.name)
        self.add_widget(self.password)
        self.entry=MyButton(text = "Войти")
        self.entry.bind(on_press= self.give_data)
        self.add_widget(self.entry)


    def profile(self,instance):
        self.clear_widgets()
        self.add_widget(MDLabel(text="егор"))
        self.movie=MyButton(text="movie")
        self.add_widget(self.movie)
        self.audio= MyButton(text="Audio")
        self.add_widget(self.audio)
        self.coll=MyButton(text="Collection")
        self.coll.bind(on_press=self.collection)
        self.add_widget(self.coll)

    def collection(self,instance):
        self.clear_widgets()
        self.hom= MyButton(text= "home")
        self.hom.bind(on_press=self.home_page)
        self.add_widget(self.hom)
        self.medias=MyButton(size_hint_x=200,size_hint_y=200,text="image")
        self.add_widget(self.medias)
        self.medias1=MyButton(size_hint_x=200,size_hint_y=200,text="image")
        self.add_widget(self.medias1)

    def enter(self,instance):
        self.clear_widgets()
        self.email=textIN(text="email")
        self.add_widget(self.email)
        self.password=textIN(text="password")
        self.add_widget(self.password)
        self.entry=MyButton(text = "Войти")
        self.entry.bind(on_press= self.profile)
        self.add_widget(self.entry)
        
        
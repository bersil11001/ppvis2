import kivymd
from kivymd.app import MDApp
from View import Home
class bookLibraryApp(MDApp):
    def build(self):
        self.load_kv("View.kv")
        return Home()

        
if __name__=="__main__":
    bookLibraryApp().run()
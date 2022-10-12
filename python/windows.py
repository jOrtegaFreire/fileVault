from tkinter import Menu, Tk, Toplevel
from sys import exit

from widgets import MenuBar

class RootWindow(Tk):

    def __init__(self,title):
        super().__init__()
        self.main_window=MainWindow(self,title)
        self.main_window.overrideredirect(1)
        self.attributes("-alpha",0.0)

        def onRootIconify(event):self.main_window.withdraw()
        self.bind("<Unmap>",onRootIconify)
        def onRootDeiconify(event):
            self.main_window.deiconify()
            self.main_window.lift()
        self.bind("<Map>",onRootDeiconify)
        self.bind("<FocusIn>",onRootDeiconify)

        self.main_window.lift()





class MainWindow(Toplevel):

    def __init__(self,parent,title):
        #llamada al constructor de la clase Tk e inicializacion de la ventana
        super().__init__(parent)
        self.parent=parent
        self.title(title)
        self.width=1280
        self.height=720
        self.geometry("{}x{}+{}+{}".format(self.width,self.height,int((self.winfo_screenwidth()-self.width)/2),int((self.winfo_screenheight()-self.height)/2)))
        self.resizable(False,False)
        self.menubar_bg="#2b2b2b"
        self.sidebars_bg="#373737"
        self.window_bg="#1b1b1b"
        self.configure(background=self.window_bg)

        #menubar
        self.menubar=MenuBar(self,self.width,30,self.menubar_bg)
        self.menubar.place(x=0,y=0)
        #file menu
        self.menubar.add_menu(label="File")
        #Settings menu
        self.menubar.add_menu(label="Settings")
        #Help menu
        self.menubar.add_menu(label="Help")
        
        self.bind('<Control-d>',exit)

        
    def add_file(self):pass
    def exit(self):exit()
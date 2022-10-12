from tkinter import Menu, Tk, Toplevel
from sys import exit
from widgets import CustomMenuBar,CustomFileFrame,CustomMenu,LockScreen,ChangeKeyFrame
from aes import password_verify,generate_key
from os import system
from pathlib import Path
import json

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
        self.sidebars_bg="#303030"
        self.window_bg="#1b1b1b"
        self.configure(background=self.window_bg)

        #load settings
        with open("settings.json","r") as f:
            self.settings=json.load(f)

        #lockscreen
        self.lock_screen=LockScreen(self,self.width,self.height,self.window_bg,self.settings)

        #menubar
        self.menubar=CustomMenuBar(self,self.width,30,self.menubar_bg)
        self.menubar.place(x=0,y=0)

        #file menu
        self.file_menu=CustomMenu(self,bg=self.menubar_bg)
        self.file_menu.add_menu_item(label="Add File")
        self.file_menu.add_menu_item(label="Extract File")
        self.file_menu.add_menu_item(label="Open Encrypted Folder",command=lambda:system('start '+self.settings['encrypted']))
        # self.file_menu.add_menu_item(label="Open Encrypted Folder",command=lambda:system('start '+str(Path(__file__).parent.parent.resolve())))
        self.file_menu.add_menu_item(label="Open Decrypted Folder",command=lambda:system('start '+self.settings['decrypted']))
        self.file_menu.add_menu_item(label="Clear Session")
        self.file_menu.add_menu_item(label="Exit",command=self.exit)
        self.menubar.add_menu(label="File",menu=self.file_menu)

        #Settings menu
        self.settings_menu=CustomMenu(self,bg=self.menubar_bg)
        self.settings_menu.add_menu_item(label="Change key",command=self.change_key)
        self.settings_menu.add_menu_item(label="Export Key")
        self.settings_menu.add_menu_item(label="Import Key")
        self.settings_menu.add_menu_item(label="Destroy vault")
        self.settings_menu.add_menu_item(label="Export vault")
        self.settings_menu.add_menu_item(label="Import vault")
        self.menubar.add_menu(label="Settings",menu=self.settings_menu)
        #Help menu
        # self.menubar.add_menu(label="Help")

        #file panel
        self.file_panel=CustomFileFrame(self,width=240,height=self.height-30,bg=self.sidebars_bg)
        self.file_panel.place(x=0,y=30)

        self.bind('<Control-q>',self.lock)
        self.bind('<Control-d>',exit)
        self.lock()

        
    def add_file(self):pass
    def lock(self,*args):
        self.lock_screen.place(x=0,y=0)
        self.lock_screen.tkraise()
    def change_key(self):
        tmp=ChangeKeyFrame(self,self.width,height=self.height,bg=self.window_bg,settings=self.settings)
        tmp.place(x=0,y=0)
        tmp.tkraise()
    def exit(self):exit()

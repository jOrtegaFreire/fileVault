from tkinter import Button, Frame
from PIL.ImageTk import PhotoImage
from PIL.Image import open

class MenuBar(Frame):

    def __init__(self,container,width=1,height=1,bg="Black"):
        self.container=container
        self.width=width
        self.height=height
        self.bg=bg
        self.menus=[]
        self.x=0
        super().__init__(self.container,width=self.width,height=self.height)
        self.configure(background=self.bg)
        self.minimizeBtn=ControlBtn(self,"minimizeBtn",command=container.parent.iconify)
        self.maximizeBtn=ControlBtn(self,"maximizeBtn")
        self.closeBtn=ControlBtn(self,"closeBtn",command=container.exit)

        self.minimizeBtn.place(x=self.width-90,y=0)
        self.maximizeBtn.place(x=self.width-60,y=0)
        self.closeBtn.place(x=self.width-30,y=0)


    def add_menu(self,label="Menu Item",width=1,height=1):
        self.menus.append(MenuButton(self,label=label))
        self.menus[-1].place(x=self.x,y=0,height=self.height)
        self.x+=self.menus[-1].winfo_reqwidth()

class ControlBtn(Button):

    def __init__(self,container,image_name,command=None):
        self.container=container
        super().__init__(container,bd=0,highlightthickness=0,activebackground=container.bg,command=command)
        self.img1=PhotoImage(open("images/"+image_name+"1.png"))
        self.img2=PhotoImage(open("images/"+image_name+"2.png"))
        self.configure(image=self.img1)

        self.bind("<Enter>",self.on_enter)
        self.bind("<Leave>",self.on_leave)

    def on_enter(self,event):self.configure(image=self.img2)
    def on_leave(self,event):self.configure(image=self.img1)

class MenuButton(Button):

    def __init__(self,container,label="Menu Button"):
        self.container=container
        super().__init__(container,text=label,font=("System",12),bg=container.bg,fg="#c4c4c4",
                        bd=0,activebackground="#9a9a9a",activeforeground="#c4c4c4",highlightbackground="#9a9a9a")

        self.bind("<Enter>",self.on_enter)
        self.bind("<Leave>",self.on_leave)

    def on_enter(self,event):self.configure(bg="#4e4e4e")
    def on_leave(self,event):self.configure(bg=self.container.bg)

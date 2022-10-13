import json
from tkinter import END, W, Button, Entry, Frame,Label
from PIL.ImageTk import PhotoImage
from PIL import Image
from aes import password_verify,generate_key

class LockScreen(Frame):

    def __init__(self,container,width=1,height=1,bg="Black",settings=None):
        self.container=container
        self.width=width
        self.height=height
        self.bg=bg
        self.settings=settings
        super().__init__(container,width=width,height=height)
        self.configure(background=bg)
        self.password_entry=Entry(self,width=32,font=("System",26),show='•')
        self.password_entry.place(x=int((self.width-self.password_entry.winfo_reqwidth())/2),y=300)
        self.unlockImg=PhotoImage(Image.open("images/unlockBtn.png").resize((50,50)))
        self.loginBtn=Button(self,image=self.unlockImg,bg=self.bg,bd=0,activebackground=self.bg)
        self.loginBtn.place(x=int((self.width-self.loginBtn.winfo_reqwidth())/2),y=400)
        self.exitImg=PhotoImage(Image.open("images/exitBtn.png").resize((50,50)))
        self.exitBtn=Button(self,image=self.exitImg,bg=self.bg,bd=0,activebackground=self.bg,command=self.container.exit)
        self.exitBtn.place(x=self.width-60,y=self.height-60)
        self.errorMsg=Label(self,text="Invalid password",font=("System",16),bg=self.bg,fg="#A01111")

        self.password_entry.bind("<Return>",self.unlock)
        self.loginBtn.bind("<Return>",self.unlock)
        self.loginBtn.bind("<Button-1>",self.unlock)

    def unlock(self,*args):
        buffer=self.password_entry.get()
        if password_verify(buffer,self.settings['key']):
            self.password_entry.delete(0,END)
            self.place_forget()
        else:
            self.errorMsg.place(x=int((self.width-self.errorMsg.winfo_reqwidth())/2),y=350)
            self.after(500,self.clear)

    def clear(self):
        self.password_entry.delete(0,END)
        self.errorMsg.place_forget()

class ChangeKeyFrame(Frame):
    def __init__(self,container,width=1,height=1,bg="Black",settings=None):
        self.container=container
        self.width=width
        self.height=height
        self.bg=bg
        self.settings=settings
        super().__init__(container,width=width,height=height)
        self.configure(background=bg)
        self.password_entry=Entry(self,width=32,font=("System",26),show='•')
        self.password_entry.place(x=int((self.width-self.password_entry.winfo_reqwidth())/2),y=300)
        self.unlockImg=PhotoImage(Image.open("images/unlockBtn.png").resize((50,50)))
        self.loginBtn=Button(self,image=self.unlockImg,bg=self.bg,bd=0,activebackground=self.bg)
        self.loginBtn.place(x=int((self.width-self.loginBtn.winfo_reqwidth())/2),y=400)
        self.exitImg=PhotoImage(Image.open("images/exitBtn.png").resize((50,50)))
        self.exitBtn=Button(self,image=self.exitImg,bg=self.bg,bd=0,activebackground=self.bg,command=self.destroy)
        self.exitBtn.place(x=self.width-60,y=self.height-60)
        self.errorMsg=Label(self,text="Invalid password",font=("System",16),bg=self.bg,fg="#A01111")

        self.password1=Entry(self,width=32,font=("System",26),show='•')
        self.password2=Entry(self,width=32,font=("System",26),show='•')
        self.changeImg=PhotoImage(Image.open("images/changepassBtn.png").resize((50,50)))
        self.changeBtn=Button(self,image=self.changeImg,bg=self.bg,bd=0,activebackground=self.bg)

        self.password_entry.bind("<Return>",self.unlock)
        self.loginBtn.bind("<Return>",self.unlock)
        self.loginBtn.bind("<Button-1>",self.unlock)

    def unlock(self,event):
        buffer=self.password_entry.get()
        if password_verify(buffer,self.settings['key']):self.clear_login()
        else:
            self.errorMsg.place(x=int((self.width-self.errorMsg.winfo_reqwidth())/2),y=350)
            self.after(500,self.clear)

    def clear(self):
        self.password_entry.delete(0,END)
        self.errorMsg.place_forget()
    
    def clear_login(self):
        self.password_entry.place_forget()
        self.loginBtn.place_forget()
        self.errorMsg.place_forget()
        self.password_entry.destroy()
        self.loginBtn.destroy()
        self.draw_inputs()

    def draw_inputs(self):
        self.password1.place(x=int((self.width-self.password1.winfo_reqwidth())/2),y=300)
        self.password2.place(x=int((self.width-self.password2.winfo_reqwidth())/2),y=400)
        self.changeBtn.place(x=int((self.width-self.changeBtn.winfo_reqwidth())/2),y=500)

        self.password2.bind("<Return>",self.change_password)
        self.changeBtn.bind("<Button-1>",self.change_password)

    def change_password(self,event):
        if self.password1.get()!=self.password2.get() or self.password1.get=='':
            self.errorMsg.configure(text="Password mismatch",fg="#A01111")
            self.errorMsg.place(x=int((self.width-self.errorMsg.winfo_reqwidth())/2),y=450)
            self.after(500,self.clear2)
        else:
            _hash=generate_key(self.password1.get())
            self.settings['key']=_hash
            self.errorMsg.configure(text="Password changed")
            self.errorMsg.place(x=int((self.width-self.errorMsg.winfo_reqwidth())/2),y=450)
            json_object=json.dumps(self.settings,indent=4)
            with open("settings.json","w") as f:
                f.write(json_object)
            self.after(500,self.destroy)

    def clear2(self):
        self.errorMsg.place_forget()
        self.password1.delete(0,END)
        self.password2.delete(0,END)



class CustomMenuBar(Frame):

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


    def add_menu(self,label="Menu Item",width=1,height=1,menu=None,command=None):
        self.menus.append(CustomMenuButton(self,label=label,menu=menu,command=command,x=self.x))
        self.menus[-1].place(x=self.x,y=0,height=self.height)
        self.x+=self.menus[-1].winfo_reqwidth()

#custom button class for minimize,maximize and close window buttons
class ControlBtn(Button):

    def __init__(self,container,image_name,command=None):
        self.container=container
        super().__init__(container,bd=0,highlightthickness=0,activebackground=container.bg,command=command)
        self.img1=PhotoImage(Image.open("images/"+image_name+"1.png"))
        self.img2=PhotoImage(Image.open("images/"+image_name+"2.png"))
        self.configure(image=self.img1)

        self.bind("<Enter>",self.on_enter)
        self.bind("<Leave>",self.on_leave)

    def on_enter(self,event):self.configure(image=self.img2)
    def on_leave(self,event):self.configure(image=self.img1)

#custom class for menu bar item
class CustomMenuButton(Button):

    def __init__(self,container,label="Menu Button",menu=None,command=None,x=0):
        self.container=container
        self.menu=menu
        self.x=x
        self.active=False
        super().__init__(container,text=label,font=("System",12),bg=container.bg,fg="#c4c4c4",
                        bd=0,activebackground="#9a9a9a",activeforeground="#c4c4c4",highlightbackground="#9a9a9a")

        self.bind("<Button-1>",self.on_click)
        self.bind("<Enter>",self.on_enter)
        self.bind("<Leave>",self.on_leave)

    def on_click(self,event):
        for menu in self.container.menus:
            if menu!=self and menu.active:
                menu.active=False
                menu.toggle()
        self.active=not self.active
        self.toggle()
    def on_enter(self,event):self.configure(bg="#4e4e4e")
    def on_leave(self,event):self.configure(bg=self.container.bg)
    def toggle(self):self.menu.toggle(self.x)

#custom class for menu bar menu
class CustomMenu(Frame):
    def __init__(self,container,height=30,bg="Black"):
        super().__init__(container,height=height,bg=bg)
        self.container=container
        self.bg=bg
        self.width=0
        self.menu_items=[]
        self.y=0
        self.visible=False

    def add_menu_item(self,label="menu item",command=None):
        self.menu_items.append(CustomMenuItem(self,label=label,y=self.y,command=command))
        self.y+=self.menu_items[-1].winfo_reqheight()
        self.configure(height=self.y)
        if self.menu_items[-1].winfo_reqwidth()>self.width:
            self.width=self.menu_items[-1].winfo_reqwidth()
            self.configure(width=self.width)
        for menu_item in self.menu_items:
            menu_item.place(x=0,y=menu_item.y,width=self.width)
    
    def toggle(self,x):
        if self.visible:
            self.place_forget()
            self.visible=False
        else:
            self.place(x=x,y=30)
            self.tkraise()
            self.visible=True


class CustomMenuItem(Button):

    def __init__(self,container,label="menu item",y=0,command=None):
        self.container=container
        self.y=y
        super().__init__(container,text=label,font=("System",12),bg=container.bg,fg="#c4c4c4",anchor=W,
                        bd=0,activebackground="#9a9a9a",activeforeground="#c4c4c4",highlightbackground="#9a9a9a",
                        command=command)

        self.bind("<Enter>",self.on_enter)
        self.bind("<Leave>",self.on_leave)

    def on_enter(self,event):self.configure(bg="#4e4e4e")
    def on_leave(self,event):self.configure(bg=self.container.bg)


class CustomFileFrame(Frame):

    def __init__(self,container,width=1,height=1,bg="Black"):
        super().__init__(container,width=width,height=height,bg=bg)

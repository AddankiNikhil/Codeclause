from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("1200x660")
root.title("TEXT EDITOR")
root.resizable(False,False)
my_frame=Frame(root)
my_frame.pack()

global open_status
open_status =False

#functions

#methods for shortcuts

def newfile(e):
    my_text.delete("1.0", END)
    my_text.title = ("New File")
    status_bar.config(text="NEW")
    root.title("New File")
    status_bar.config(text="New File")

def save_file(e):
    global open_status
    if open_status:
        # saving the file
        text_file = open(open_status, 'w')
        text_file.write(my_text.get(1.0, END))
        # closing the file
        text_file.close()
    else:
        save_as()
    # status bar updation
    try:
        status_bar.config(text="Saved  " + open_status)
    except:
        pass

def open_file(e=None):
    # delete prev text
    my_text.delete("1.0", END)

    # opening file
    text_file = filedialog.askopenfilename(initialdir="D:", title="Open File", filetypes=(
    ("Text files", "*.txt"), ("Python files", "*.py"), ("HTML Files", "*.html"), ("Java files", "*.java"),
    ("ALL files", "*.*")))
    name = text_file
    if text_file:
        global open_status
        open_status = name
        print("open_status:" + open_status)

    # status setting
    status_bar.config(text=name)
    root.title(name.split("/")[-1])

    # open file
    text_file = open(text_file, 'r')
    data = text_file.read()
    my_text.insert(END, data)

    # closing the file

    text_file.close()


# functions for menu options

def new_file():
    my_text.delete("1.0",END)
    my_text.title=("New File")
    status_bar.config(text="NEW")
    root.title("New File")
    status_bar.config(text="New File")

def openfile():
    #delete prev text
    my_text.delete("1.0",END)

    #opening file
    text_file=filedialog.askopenfilename(initialdir="D:",title="Open File",filetypes=(("Text files","*.txt"),("Python files","*.py"),("HTML Files","*.html"),("Java files","*.java"),("ALL files","*.*")))
    name = text_file
    if text_file:
      global open_status
      open_status=name
      print("open_status:"+open_status)

    #status setting
    status_bar.config(text=name)
    root.title(name.split("/")[-1])

    #open file
    text_file = open(text_file,'r')
    data=text_file.read()
    my_text.insert(END,data)

    #closing the file

    text_file.close()

def save_as():
    text_file=filedialog.asksaveasfilename(defaultextension="*.*",initialdir="D:",title="Save File",filetypes= (("Text files","*.txt"),("Python files","*.py"),("HTML Files","*.html"),("java files","*.java"),("ALL files","*.*")))
    name=text_file

    #status bar updation
    root.title(name.split("/")[-1])
    status_bar.config(text="Saved" + name)

    #saving the file
    text_file=open(text_file,'w')
    text_file.write(my_text.get(1.0,END))
    text_file.close()

def savefile():
    global open_status
    if open_status:
         # saving the file
         text_file = open(open_status, 'w')
         text_file.write(my_text.get(1.0, END))
         #closing the file
         text_file.close()
    else:
        save_as()
    #status bar updation
    try:
       status_bar.config(text="Saved  "+open_status)
    except :
        pass
#Scroll bar
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)

#Text field
my_text=Text(my_frame,width=150,height=40,selectbackground="cyan",selectforeground="black",undo=True,yscrollcommand=text_scroll.set)
my_text.pack()

#configure the scroll bar

text_scroll.config(command=my_text.yview)

#menu creation
my_menu=Menu(root)
root.config(menu=my_menu)

#add items to menu
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=openfile)
file_menu.add_command(label="Save",command=savefile)
file_menu.add_command(label="Save as",command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

#Status bar
status_bar=Label(text="ready    ",anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=5)


root.bind('<Control-n>',newfile)
root.bind('<Control-s>',save_file)
root.bind('<Control-o>',open_file)
root.mainloop()


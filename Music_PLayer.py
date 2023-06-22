from tkinter import *
import os
from tkinter import ttk,filedialog
from pygame import mixer


#main body decleration
master=Tk()
master.title("Music Palyer")
master.geometry("920x670+290+85")
#master.config(bg="CYAN")
#master.geometry("750x500")
master.resizable(False,False)


#functions
def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir()
        ##print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)
def play():
    song=playlist.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()

#mixer initialization

mixer.init()

# photos
"""
BG=PhotoImage("D:\internships\techno_hacks\background.png")
Label(master,image=BG).place(x=0,y=0,relheight=1)
"""
#Buttons Decleration

play=Button(master,text="Play" ,command=play).place(x=100,y=400,width=70,height=50)

stop=Button(master,text="Stop",command=mixer.music.stop).place(x=100,y=500,width=70,height=50)

resume=Button(master,text="Resume",command=mixer.music.unpause).place(x=200,y=500,width=70,height=50)

pause=Button(master,text="Pause",command=mixer.music.pause).place(x=200,y=400,width=70,height=50)


#music
music_frame=Frame(master,bd=2,relief=RIDGE)
music_frame.place(x=330,y=250,width=560,height=350)

Button(master,text="Open Folder",width=15,height=2,font=("Cosmic Sans",10,"bold"),command=open_folder,bg="GRAY").place(x=330,y=200)

scroll=Scrollbar(music_frame)

playlist=Listbox(music_frame,width=550,font=("Cosmic Sans",10),fg="GRAY",selectbackground="lightblue",
                 cursor="hand2",yscrollcommand=scroll.set)
         
scroll.config(command=playlist.yview)

playlist.pack(side=LEFT,fill=BOTH)

scroll.pack(side=RIGHT,fill=Y)

master.mainloop()
import pygame
from pygame import mixer
from tkinter import *
import os
def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()
def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()
def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()
def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()    
root=Tk()
root.title('Learninstudy Music Player')
mixer.init()
songstatus=StringVar()
songstatus.set("choosing")
#playlist---------------
playlist=Listbox(root,selectmode=SINGLE,bg="Black",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)
#add the path of your folder which contains the musics files.
os.chdir(r'C:/Users/MAYANK/AppData/Local/Programs/Python/Python37-32/New folder')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)
playbtn=Button(root,text="Play",command=playsong)
playbtn.config(font=('Verdana',20),bg="black",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)
pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('Verdana',20),bg="Black",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)
stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('Verdana',20),bg="Black",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)
Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('Verdana',20),bg="Black",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)
mainloop()
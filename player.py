import os
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title("MP3 Player")
root.geometry("485x700+290+10")
root.configure(background='#333333')
mixer.init()

# Global variables to track the playlist and the currently playing song
playlist = []
current_song_index = 0

# Create a function to open a file
def AddMusic():
    global playlist
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                playlist.append(song)
                Playlist.insert(END, song)

def PlayMusic():
    global current_song_index
    if len(playlist) > 0:
        Music_Name = Playlist.get(ACTIVE)
        print(Music_Name)
        mixer.music.load(playlist[current_song_index])
        mixer.music.play()

def NextMusic():
    global current_song_index
    if playlist:
        current_song_index = (current_song_index + 1) % len(playlist)
        PlayMusic()

def PreviousMusic():
    global current_song_index
    if playlist:
        current_song_index = (current_song_index - 1) % len(playlist)
        PlayMusic()

# icon
lower_frame = Frame(root , bg = "#FFFFFF", width = 485 , height = 180 )
lower_frame.place ( x = 0 , y = 400)

image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

# Load a single-frame GIF for your animation
animation_image = PhotoImage(file='music.gif')
label = Label(root, image=animation_image)
label.pack()
label.place(x=0, y=0)

# Button
ButtonPlay = PhotoImage(file="play.png")
Button(root, image=ButtonPlay, bg="#FFFFFF", bd=0, height=60, width=60, command=PlayMusic).place(x=195, y=487)

ButtonStop = PhotoImage(file="stop.png")
Button(root, image=ButtonStop, bg="#FFFFFF", bd=0, height=60, width=60, command=mixer.music.stop).place(x=120, y=487)

ButtonNext = PhotoImage(file="next.png")
Button(root, image=ButtonNext, bg="#FFFFFF", bd=0, height=60, width=60, command=NextMusic).place(x=360, y=487)

ButtonPrevious = PhotoImage(file="previous.png")
Button(root, image=ButtonPrevious, bg="#FFFFFF", bd=0, height=60, width=60, command=PreviousMusic).place(x=40, y=487)

ButtonPause = PhotoImage(file="pause.png")
Button(root, image=ButtonPause, bg="#FFFFFF", bd=0, height=60, width=60, command=mixer.music.pause).place(x=270, y=487)

# Label       
Menu = PhotoImage(file="menu.png")
Label(root, image=Menu).place(x=0, y=580, width=485, height=120)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=585, width=485, height=100)

Button(root, text="Browse Music", width=59, height=1, font=("calibri", 12, "bold"), fg="#8B008B", bg="#FFFFFF", command=AddMusic).place(x=0, y=550)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#FFFFFF", fg="#ee0a61", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

# Execute Tkinter
root.mainloop()
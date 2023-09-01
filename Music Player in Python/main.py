from tkinter import *
from tkinter import filedialog

import pygame
import os

root = Tk()
root.title("Music Player")
root.geometry("500x300")

pygame.mixer.init()
menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song = ""
paused = False

def load_music():
    global current_song
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        root.directory = os.path.dirname(file_path)
        songs.append(os.path.basename(file_path))
        songList.insert("end", os.path.basename(file_path))
        songList.selection_set(0)
        current_song = os.path.basename(file_path)

organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='Select Folder',command=load_music)
menubar.add_cascade(label = "Organise", menu = organise_menu)

def play_music():
      global current_song, paused

      if not paused:
          pygame.mixer.music.load(os.path.join(root.directory, current_song))
          pygame.mixer.music.play()
      else:
            pygame.mixer.music.unpause()
            paused = False

def pause_music():
      global paused
      pygame.mixer.music.pause()
      paused = True

def next_music():
      global current_song, paused
      try:
          songList.selection_clear(0, END)
          songList.selection_set(songs.index(current_song) + 1)
          current_song = songs[songList.curselection()[0]]
          play_music()
      except:
          pass

def prev_music():
      global current_song, paused
      try:
          songList.selection_clear(0, END)
          songList.selection_set(songs.index(current_song) - 1)
          current_song = songs[songList.curselection()[0]]
          play_music()
      except:
          pass

songList = Listbox(root, bg="black", fg="white", width=100, height=15)
songList.pack()

play_btn_image = PhotoImage(file='play.png')
pause_btn_image = PhotoImage(file='pause.png')
next_btn_image = PhotoImage(file='next.png')
prev_btn_image = PhotoImage(file='prev.png')

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_image, borderwidth=0, command=play_music)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0, command=pause_music)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0, command=next_music)
prev_btn = Button(control_frame, image=prev_btn_image, borderwidth=0, command=prev_music)

play_btn.grid(row=0, column=3, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=1, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()

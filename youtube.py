from tkinter import *
from pytube import YouTube
from PIL import ImageTk, Image  


root = Tk()
root.geometry("500x500")
root.resizable(0,0)
root.configure(bg="white")
root.title("youtube downloader")



def download():
    url = YouTube(str(link.get())) #This captures the link(url) and locates it from YouTube.
    video = url.streams.filter(only_audio=True).first() # This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
    video.download(filename="song.mp3") # This is the method with the instruction to download the video.
    Label(root, text="Downloaded", font="arial 15",highlightcolor="red").place(x=212, y=85)  #Once the video is downloaded, this label `downloaded` is displayed to show dowload completion.
image1 = ImageTk.PhotoImage(Image.open("image2.png"))
Label(root,image= image1).place(x=0,y=0)

download_text = Label(root, text="TRANSFER YOUTUBE VIDEO TO AUDIO FOR FREE", font='san-serif 14 bold', bg="red").pack()
link = StringVar() # Specifying the variable type
link_text = Label(root, text="Paste your link here", font='san-serif 15 bold').place(x=180,y=30)

#link_input
link_input_area = Entry(root, width=40, textvariable=link).place(x=67, y=55)

#button 
Button(root, text="Download", font = 'san-serif 16 bold', bg = "yellow", padx=2,command= download).place(x=200,y=110)

root.mainloop()


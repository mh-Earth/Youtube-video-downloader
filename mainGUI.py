from tkinter import *
import pytube
import os,sys
from pydub import AudioSegment
from time import sleep,time
import string
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import asksaveasfile 

def updateStatus(text):
    global status
    sleep(2)
    status.set(text)
    sbar.update()

def download():


    global fileName,url,PATH,videoType
    url=url.get()
    videoType=combo.get()
    fileInfo=asksaveasfile(filetypes=[("all", ".mp3 .mp4")],mode='w', title="Save the file", defaultextension=f".{videoType}")
    fileName=fileInfo.name


    for i in range(len(fileName)):
        letter=fileName[len(fileName)-i:len(fileName)]
        if "/" in letter:
            file_Name=fileName[len(fileName)-i+1:len(fileName)]
            PATH=fileName[:len(fileName)-i]
            break


    def history(text):
        global fill_Name
        f=open(f"{file_Name}.log","a")
        f.write(f"{text}\n")
        f.close()




    t1=time()
    updateStatus("[+]Connecting to youtube")
    history("[+]Connecting to youtube")
    try:
        youtube = pytube.YouTube(url)
        videoLength = youtube.length
    except Exception as e:
        updateStatus("[-]Unable to connect youtube")
        messagebox.showerror("Connection Problem","Unable to connect youtube")
        history(e)
        history("[-]Unable to connect youtube")
        history("[-]Make sure your device is connected to internet")
        sleep(5)
        sys.exit()



    if videoType=="mp3":
        video = youtube.streams.last()
    elif videoType=="mp4":
        video = youtube.streams.first()



    updateStatus(f'[+]Saving as {fileName}.{videoType}')
    updateStatus(f"[+]Saving at {PATH}")

    history(f'[+]Saving as {fileName}.{videoType}')
    history(f"[+]Saving at {PATH}")
    history(f"[+]Type: mp3")
    history("\n")
    history("######################################### Description ####################################")
    history("\n")
    history(youtube.description)
    history("##########################################################################################")
    history("\n")
    file_Name=file_Name[:-4]




    try:
        updateStatus("[+]Downloading please wait.......")
        history("[+]Downloading please wait.......")
        video.download(PATH,file_Name)
        file_Name=fileName[len(fileName)-i+1:len(fileName)]
    except Exception as e:
        history(e)
        file_Name=fileName[len(fileName)-i+1:len(fileName)]
        updateStatus("[-]Falied to download")
        messagebox.showerror("Connection Problem","Falied to download")
        history("[-]Falied to download")
        sys.exit()



    fileName=fileName[:-4]+'.webm'
    sleep(5)
    if videoType=="mp3" or videoType=="audio":
        updateStatus("[+]Converting.......")

        flac_audio = AudioSegment.from_file(fileName[:-5]+".webm")
        flac_audio.export(fileName[:-5]+".mp3", format="mp3")



    t2=time()
    updateStatus(f"[+]Download completed | [+]Finished in {t2-t1}s")
    history("[+]Download completed")
    history(f"[+]Finished in {t2-t1}s")



if __name__=="__main__":
    root=Tk()
    root.geometry(("500x250"))
    root.title("MainGUI")
    root.resizable(0,0)
    url=StringVar()
    Label(root,text="Enter the youtube video url:",padx=10).pack(side=TOP,anchor=NW)
    Entry(root,textvariable=url).pack(side=TOP,anchor=W,ipadx=160,padx=10)

    Label(root,text="Set download video format",padx=10,pady=20).pack(side=TOP,anchor=W)
    combo = ttk.Combobox(root, values=["mp3","mp4"], font="None 10", width=6,state="readonly")
    combo.pack(side=TOP,anchor=W,padx=10,pady=0)
    combo.set("mp4")

    Button(root,text="Download",command=download).pack(side=TOP,fill=X,anchor=W,padx=8,pady=20)
    status=StringVar()
    status.set("Ready")
    sbar=Label(root,textvariable=status,borderwidth=5,anchor=SW,relief=RAISED)
    sbar.pack(side=BOTTOM,fill=X,anchor=W)
    root.mainloop() 
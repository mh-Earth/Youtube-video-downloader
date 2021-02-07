import pytube
import os,sys
from pydub import AudioSegment
from time import sleep,time


url=input("Enter the video url:")
t1=time()

# ____________________________________
print("[+]Connecting to youtube")
try:
    youtube = pytube.YouTube(url)
    videoLength = youtube.length
    print("[+]connected")
    print(f"[+]Title: {youtube.title}")
    print(f"[+]Length: {videoLength/60}")
except Exception as e:
    # print(e)
    print("[-]Unable to connect youtube")
    sys.exit()

# ____________________________________
while True:
    videoType=input("Enter the download video type (--h for help):")
    try:
        if videoType=="mp3" or videoType=="audio":
            video = youtube.streams.last()
            print(f"[+]Type: mp3")
            print("\n")
            print("######################################### Description ####################################")
            print("\n")
            print(youtube.description)
            break
            
        elif videoType=="mp4" or videoType=="video":
            video = youtube.streams.first()
            print(f"[+]Type: mp4")
            print("\n")
            print("######################################### Description ################################################")
            print("\n")
            print(youtube.description)
            break
        elif videoType=="--h" :
            print(f"[+]Video types: mp3 or mp4")
        else:
            print("[-]Invalied video type")
            print("[-]--h for help")
            
    except Exception as TypeError:
        print("[-]Invalied video type")
        break
        sys.exit()
# ____________________________________ 
print("#########################################################################################")
print("\n")
fileName=input("Enter the fill name:")
print(f'[+]Saving as {fileName}.{videoType}')


PATH=input("Enter saving path:")
# ____________________________________
if PATH=="":
    print(f"[+]Saving at {os.getcwd()}")
    PATH=os.getcwd()
else:
    print(f"[+]Saving at {PATH}")
# ____________________________________

try:
    print("[+]Downloading please wait.......")
    video.download(PATH,fileName)
except Exception as e:
    print(e)
    print("[-]Falied to download")
    sys.exit()
# ____________________________________

fileName=fileName+'.webm'
print("[+]Converting.......")
sleep(3)
# ____________________________________
if videoType=="mp3" or videoType=="audio":

    flac_audio = AudioSegment.from_file(f"{PATH}/{fileName}")
    flac_audio.export(f"{PATH}/{fileName[:-5]}"+".mp3", format="mp3")
# ____________________________________
print("[+]Download completed")
t2=time()
print(f"[+]Finished in {t2-t1}s")
sys.exit()
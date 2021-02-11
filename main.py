import pytube
import os,sys
from pydub import AudioSegment
from time import sleep,time
import colorama
from colorama import Fore, Style
import random
# print(Fore.RED + "Hello World")

if __name__=="__main__":
    if not os.geteuid() == 0:
        sys.exit("""\033[1;91m\n[!] This srcipt must be run as root or administrator. ¯\_(ツ)_/¯\n\033[1;m""")

    colors=[Fore.RED,Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.BLUE,Fore.MAGENTA,Fore.CYAN]
    c=random.choice(colors)
    print(c+ '''
__   __             _           _                    _      _              
\ \ / /___   _   _ | |_  _   _ | |__   _ __  __   __(_)  __| |  ___   ___  
 \ V // _ \ | | | || __|| | | || '_ \ | '__| \ \ / /| | / _` | / _ \ / _ \ 
  | || (_) || |_| || |_ | |_| || |_) || |     \ V / | || (_| ||  __/| (_) |
  |_| \___/  \__,_| \__| \__,_||_.__/ |_|      \_/  |_| \__,_| \___| \___/ 
                                                                           
     _                         _                    _             
  __| |  ___ __      __ _ __  | |  ___    __ _   __| |  ___  _ __ 
 / _` | / _ \\\\ \ /\ / /| '_ \ | | / _ \  / _` | / _` | / _ \| '__|
| (_| || (_) |\ V  V / | | | || || (_) || (_| || (_| ||  __/| |   
 \__,_| \___/  \_/\_/  |_| |_||_| \___/  \__,_| \__,_| \___||_|   
                                                                  

''')

    url=input("Enter the video url:")
    t1=time()

    # ____________________________________
    print("\033[92m[+]Connecting to youtube\033[92m")
    try:
        youtube = pytube.YouTube(url)
        videoLength = youtube.length
        print("\033[92m[+]connected")
        print(f"\033[92m[+]Title: {youtube.title}")
        print(f"\033[92m[+]Length: {videoLength/60}\033[92m")
    except Exception as e:
        print(f"\033[91m[-]{e}")
        print("\033[91m[-]Unable to connect youtube")
        sys.exit()

    # ____________________________________
    while True:
        videoType=input("\033[92mEnter the download video type (--h for help):\033[92m")
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
                print(f"\033[92m[+]Type: mp4")
                print("\n")
                print("######################################### Description ################################################")
                print("\n")
                print(youtube.description)
                break
            elif videoType=="--h" :
                print(f"\033[93m[+]Video types: mp3 or mp4\033[92m")
            else:
                print("\033[91m[-]Invalied video type\033[91m")
                print("\033[91m[-]--h for help\033[91m")
                
        except Exception as TypeError:
            print(f"\033[91m[-]{TypeError}\033[91m")
            print("\033[91m[-]Invalied video type\033[91m")
            
    # ____________________________________ 
    print("#########################################################################################")
    print("\n")
    fileName=input("\033[92mEnter the fill name:\033[92m")
    print(f'\033[93m[+]Saving as {fileName}.{videoType}\033[92m')

    while True:
        PATH=input("\033[92mEnter saving path:\033[92m")
        if PATH=="":
            PATH=os.getcwd()
            print(f"\033[93m[+]Saving at {PATH}\033[92m")
            break
        elif os.path.isabs(PATH):
            print(f"\033[93m[+]Saving at {PATH}\033[92m")
            break
        else:
            print("\033[91m[-]Invalide path\033[91m")
            continue
    
    # ____________________________________

    try:
        print("\033[92m[+]Downloading please wait.......\033[92m")
        video.download(PATH,fileName)
    except Exception as e:
        print(f"\033[91m[-]{e}\033[91m")
        print(e)
        print("\033[91m[-]Falied to download\033[91m")
        sys.exit()
    # ____________________________________

    fileName=fileName+'.webm'
    print("\033[92m[+]Converting.......\033[92m")
    sleep(3)
    # ____________________________________
    if videoType=="mp3" or videoType=="audio":

        flac_audio = AudioSegment.from_file(f"{PATH}/{fileName}")
        flac_audio.export(f"{PATH}/{fileName[:-5]}"+".mp3", format="mp3")
        os.system(f"del /f {PATH}/{fileName}") if sys.platform == "win32" else os.system(f"rm -r {PATH}/{fileName}")

    # ____________________________________
    print("\033[92m[+]Download completed\033[92m")
    t2=time()
    print(f"\033[92m[+]Finished in {t2-t1}s\033[92m")
    sys.exit()
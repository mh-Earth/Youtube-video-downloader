import pytube
import os,sys
import argparse
from pydub import AudioSegment
from time import sleep,time
def main(args):
    global fileName,url,PATH,videoType,youtube
    url=args.u
    videoType=args.f
    PATH=args.P
    fileName=args.o
    t1=time()

    # ____________________________________
    print("[+]Connecting to youtube")
    try:
        youtube = pytube.YouTube(url)
        videoLength = youtube.length
        print("[+]connected")
        print(f"[+]Title: {youtube.title}")
        print(f"[+]Length: {videoLength/60}m")
    except Exception as e:
        print("[-]Unable to connect youtube")
        sys.exit()

    if fileName=="untitle":
        fileName=youtube.title
    # ____________________________________

    try:
        if videoType=="mp3" or videoType=="audio":
            video = youtube.streams.last()
            print(f"[+]Type: mp3")
            print("\n")
            print("######################################### Description ####################################")
            print("\n")
            print(youtube.description)
                
        elif videoType=="mp4" or videoType=="video":
            video = youtube.streams.first()
            print(f"[+]Type: mp4")
            print("\n")
            print("######################################### Description ################################################")
            print("\n")
            print(youtube.description)
    

        elif videoType=="-h" :
            print(f"[+]Video types: mp3 or mp4")
            quit()
        else:
            print("[-]Invalied video type")
            print("[-]-h for help")
            quit()            

    except Exception as TypeError:
        print("[-]Invalied video type")
        sys.exit()
    # ____________________________________ 
    print("#########################################################################################")
    print("\n")
    print(f'[+]Saving as {fileName}.{videoType}')


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
    # ____________________________________
    if videoType=="mp3" or videoType=="audio":

        print("[+]Converting.......")
        sleep(3)

        flac_audio = AudioSegment.from_file(f"{PATH}/{fileName}")
        flac_audio.export(f"{PATH}/{fileName[:-5]}"+".mp3", format="mp3")
    # ____________________________________
    print("[+]Download completed")
    t2=time()
    print(f"[+]Finished in {t2-t1}s")
    sys.exit()

if __name__=="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--u','--url', type=str,
                        help="Enter youtube video link")

    parser.add_argument('--f','--format', type=str,default="mp4",
                        help="Enter downloaded file format (mp3 or mp4) default is mp4")

    parser.add_argument('--P','--path', type=str, default=os.getcwd(),
                        help="Enter saving path default is present working directory")

    parser.add_argument('--o', type=str, default='untitle',
                        help="save file name,default is videoTitle.mp4")


    args = parser.parse_args()
    sys.stdout.write(str(main(args)))
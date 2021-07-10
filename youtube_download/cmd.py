# download youtube video
from pytube import YouTube
from link import get_links
import time
import os
import sys
"""
User input 
"""
link = input("Enter the link: ")

"""
path
"""
current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
download_dir = os.path.join(current_dir,'download2')

def download():
    for link in get_links()[0:100]:
        yt = YouTube(link[0])
        if yt.title not in download_dir:
            ys = yt.streams.get_highest_resolution()
            try:
                ys.download('download')
                print(yt.title," is downloaded")
            except:
                print(yt.title," is failed")
        else:
            print(yt.title," is already downloaded") 
        #time.sleep(5)
if __name__ == '__main__':
    # for file in os.listdir(download_dir):
    #     print(file)
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    ys.download('download2')
    #download()
"""
number of links
"""
#print(len(get_links()))
    #print(YouTube("https://www.youtube.com/watch?v=L60TyYBy7eU").title)

"""
Details of video
"""
#print("Title: ",yt.title) # Title of video
#print("Number of views: ",yt.views) # Number of views of video
#print("Length of video: ",yt.length,"seconds") # Length of video
#print("Description: ",yt.description) # Description of video
#print("Ratings: ",yt.rating) # Rating
#print(yt.streams.filter(only_audio=True))


# download youtube video
from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)
print("Title: ",yt.title) # Title of video
print("Number of views: ",yt.views) # Number of views of video
print("Length of video: ",yt.length,"seconds") # Length of video
#print("Description: ",yt.description) # Description of video
print("Ratings: ",yt.rating) # Rating
#print(yt.streams.filter(only_audio=True))
ys = yt.streams.get_highest_resolution()
ys.download('download')

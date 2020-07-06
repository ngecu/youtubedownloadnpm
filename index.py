import pytube
link = "https://youtu.be/8zSRkr1nQNw"
yt = pytube.YouTube(link)
print(yt.title)
stream = yt.streams.first()
stream.download()

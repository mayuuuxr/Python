import yt_dlp as youtube_dl

url = input("enter url for the video :")
ydl_opts = {
    'format': 'best',  
    'outtmpl': '%(title)s.%(ext)s',  # Save the file with the video's title as the filename
    'noplaylist': True,
     }


try:
    ydl= youtube_dl.YoutubeDL(ydl_opts)
    ydl.download([url])
    print("Download completed successfully.")
except Exception as e:
        print(f"An error occurred: {e}")
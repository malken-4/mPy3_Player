from pathlib import Path
from PIL import Image
import subprocess

url = input("Enter a YouTube Music URL: ")

#Get title

#Download audio
result = subprocess.run(
    [
        "yt-dlp",
        "-x"
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "--write-thumbnail",
        "--convert-thumbnails", "jpg",
        "-o", "./music/%(title)s.%(ext)s",
        "-o", "thumbnail:./assets/covers/%(title)s Cover.%(ext)s",
        url
    ],
    capture_output=True,
    text=True
)
                         
if result.returncode != 0:
    print("Error downloading audio or cover art.")
    print(result.stderr)
else:
    print("Download successful!")   

# # Find cover art file
# filename = ""
# search_dir = Path("./assets/covers")

# file_path = next(search_dir.rglob(filename), None)

# if file_path is None:
#     print("File not found")
# else:
#     img = Image.open(file_path)

#     width, height = img.size
#     square_size = min(width, height)

#     left = (width - square_size) // 2
#     top = (height - square_size) // 2

#     cropped = img.crop(
#         (
#             left, 
#             top,
#             left + square_size,
#             top + square_size
#         )
#     )

#     cropped.save(file_path)
#     print("Square crop complete")
    

#Grab and process cover art
#search in ./assets/covers for same "Title" + "Cover" image
#then crop it into a square (find smallest dimension and then change other dimension to be that size)


# Uset the smaller dimension


#Update song library
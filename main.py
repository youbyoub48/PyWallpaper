import os

from wallpaper import Wallpaper
from time import sleep

while True:
    wallpaper = Wallpaper(dirrectory="/home/youbyoub/Wallpaper")
    os.system(f"gsettings set org.gnome.desktop.background picture-uri file:///{wallpaper.choose_wallpaper()}")
    sleep(30)

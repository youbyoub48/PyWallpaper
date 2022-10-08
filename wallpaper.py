import random, os

from glob import glob
from pathlib import Path

class Wallpaper :
    def __init__(self, dirrectory):
        self.directory = dirrectory
        self.get_wallpaper()
        self.choose_wallpaper()


    def get_wallpaper(self):
        self.fichier = glob(os.path.join(self.directory, "*"))


    def choose_wallpaper(self):
        self.wallpaper = random.choice(self.fichier)
        return self.wallpaper




if __name__ == "__main__":
    wallpaper_path = os.path.join(Path.home(), "Wallpaper")
    wallpaper = Wallpaper(dirrectory=wallpaper)
    print(wallpaper.choose_wallpaper())

import random, os

from glob import glob

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
    a = Wallpaper(dirrectory="/home/youbyoub/Wallpaper")
    print(a.choose_wallpaper())
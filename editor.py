from PIL import Image
from config import Config
import os


class Editor:

    def convert_to_jpg(self, pic):
        if pic.endswith('.jpg'):
            pass
        else:
            start_pic, end_pic = os.path.splitext(pic)
            i = Image.open(f"media/{pic}")
            i.convert('RGB').save(f"media/{start_pic}.jpg")

    def convert_to_png(self, pic):
        if pic.endswith('.png'):
            pass
        else:
            i = Image.open(f"media/{pic}")
            i.save(f"media/{start_pic}.png")

    def make_thumbail(self, pic, i):
        size = (128, 128)
        i.thumbnail(size)
        i.save(f"media/{pic}")

    def right_rotate(self, pic, i, rot):
        i.rotate(rot).save(f"media/{pic}")

    def left_rotate(self, pic, i, rot):
        rott = 360 - rot
        i.rotate(rott).save(f"media/{pic}")

    def side_mirror(self, pic, i):
        i = i.transpose(Image.FLIP_LEFT_RIGHT)
        i.save(f"media/{pic}")

    def bottom_mirror(self, pic, i):
        i = i.transpose(Image.FLIP_TOP_BOTTOM)
        i.save(f"media/{pic}")

    def change_height(self, pic, i, height):
        iwidth, iheight = i.size
        new_size = (iwidth, height)
        new = i.resize(new_size)
        new.save(f"media/{pic}")

    def change_width(self, pic, i, width):
        iwidth, iheight = i.size
        new_size = (width, iheight)
        new = i.resize(new_size)
        new.save(f"media/{pic}")

    def run(self):

        try:
            for pic in os.listdir('media/'):
                i = Image.open(f"media/{pic}")

                if Config.convert_to_jpg != 0:
                    self.convert_to_jpg(pic)

                if Config.convert_to_png != 0:
                    self.convert_to_png(pic)

                if Config.make_thumbail != 0:
                    self.make_thumbail(pic, i)

                if Config.right_rotate != 0:
                    self.right_rotate(pic, i, Config.right_rotate)

                if Config.left_rotate != 0:
                    self.left_rotate(pic, i, Config.left_rotate)

                if Config.side_mirror != 0:
                    self.side_mirror(pic, i)

                if Config.bottom_mirror != 0:
                    self.bottom_mirror(pic, i)

                if Config.change_height != 0:
                    self.change_height(pic, i, Config.change_height)

                if Config.change_width != 0:
                    self.change_width(pic, i, Config.change_width)

        except OSError:
            pass

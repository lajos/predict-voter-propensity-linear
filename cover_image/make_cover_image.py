#
#  create cover image of random crowd
#

from PIL import Image
from glob import glob
import random
import numpy as np

from matplotlib.pyplot import hsv

def read_images(glob_path):
    images = []
    for i in glob(glob_path):
        print('read image:',i)
        img = Image.open(i)
        images.append(img)
    return images

def rgba2hsva(image):
    return image.convert('HSV')

def hsva2rgba(image):
    return image.convert('RGB')

def main():
    img_scale = 5
    img = Image.new("RGBA", (int(1500*img_scale), int(750*img_scale)), (255, 255, 255, 255))

    color_images = read_images('cover_image/color/*.png')
    line_images = read_images('cover_image/line/*.png')

    x_offset = 600
    y_offset = 250

    x_jiggle = 80
    y_jiggle = 50

    color_chance = 0.3

    h_jiggle = 0.05
    s_jiggle = 0.1
    v_jiggle = 0.07

    for o in range (-2, 15):
        for i in range(15):
            x = (-x_offset / 2 * (o%2)) + i*x_offset + random.randint(0, x_jiggle)
            y= o * y_offset + random.randint(0, y_jiggle)

            c_img = None
            if random.random()<color_chance:
                c_img = random.choice(color_images).copy()
                alpha = c_img.getchannel('A')
                c_img = rgba2hsva(c_img)
                np_img = np.array(c_img).astype(np.float64)
                np_img = np.moveaxis(np_img, 2, 0)
                np_img[0,:] *= random.uniform(1-h_jiggle, 1)
                np_img[1,:] *= random.uniform(1-s_jiggle, 1)
                np_img[2,:] *= random.uniform(1-v_jiggle, 1)
                np_img = np.moveaxis(np_img, 0, 2)
                c_img = Image.fromarray(np.uint8(np_img), mode='HSV')
                c_img = hsva2rgba(c_img)
                c_img.putalpha(alpha)
            else:
                c_img = random.choice(line_images)

            img.alpha_composite(c_img, (int(x),int(y)))

    img = img.convert('RGB')
    img = img.resize((1500,750))
    img.save('cover_image.jpg', 'JPEG')

if __name__=='__main__':
    main()
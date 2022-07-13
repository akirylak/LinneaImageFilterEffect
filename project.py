"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Final Project"""

'''
pseudo code:
1.  execute program in sys.argv
    1.  sys.argv[0] - name of the program
    2.  sys.argv[1] - name of the input
    3.  sys.argv[2] - name of the export
    2.  sys.argv[3] - name of the filter.
2.  sys.argv[2] and sys.argv[3] - cannot be the same file name and check if valid image input.
3.  Name of the filter must be valid according to a dictionary if key:values.  Key being the name of the filter, value being the function.
4.  Output image must be in a square 1:1 Ratio, 600x600 pixel to ensure consistency in masks and filters

Used PIL documentation to create filters: https://pillow.readthedocs.io/en/stable/

'''
#required libraries
import os
import sys
import argparse
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageOps
from random import choice

#function to check if the file format is valid and is in the same format and is not the same names
def valid_file(before, after):
    if before.lower().endswith(('.png', '.jpg', '.jpeg')):
        if after.lower().endswith(('.png', '.jpg', '.jpeg')):
            before = os.path.splitext(before)
            after = os.path.splitext(after)
            if before[0] == after[0]:
                sys.exit("File names cannot be the same")
            if before[1] == after[1]:
                return(before, after)
            else:
                sys.exit("Input and Output have different extensions")
        else:
            sys.exit("Invalid Output")
    else:
            sys.exit("Invalid Input")

#function to check if the filter inputted in sys.argv[3] is a valid filter type
def valid_dict(img):
    #dictionary of key:values as filter name and function
    image_filter_type = {"bw": bw, "rd_color": rd_color, "inst_a": inst_a, "inst_b": inst_b, "inst_c": inst_c, "inst_d": inst_d, "pol": pol, "cs50": cs50}
    if img in image_filter_type:
        for i in image_filter_type:
            if img in i:
                check_type = image_filter_type[i](img)
                return check_type
    else:
        sys.exit("Invalid Filter")

#black and white filter
def bw (img):
    img = Image.open(sys.argv[1], mode="r")
    img = img.convert("L")
    img = ImageOps.fit(img, (600, 600),Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    contrast = ImageEnhance.Contrast(img)
    factor = 1.5
    img_out = contrast.enhance(factor)
    img_out = img_out.filter(ImageFilter.UnsharpMask(radius=0.8, percent=100, threshold=0))
    img_out.save(sys.argv[2])

#random color filter
def rd_color(img):
    img = Image.open(sys.argv[1], mode="r")
    img = img.convert("L")
    img = ImageOps.fit(img, (600, 600),Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

    img_bw = img.point(lambda x: 0 if x <110 else 255, '1')

    img = img_bw.convert("RGB")

    img_data = img.getdata()

    new_image = []
    colors = choice([(204, 0, 0), (0, 204, 0), (0, 0, 204), (0, 204, 204), (204, 0 , 204), (204, 204, 0)])
    for item in img_data:
        if item[0] in list(range(250, 256)):
            new_image.append((colors))
        else:
            new_image.append(item)
    img.putdata(new_image)
    img.save(sys.argv[2])

#Instagram-ish filter 1
def inst_a(img):
    img = Image.open(sys.argv[1], mode="r")
    img = img.convert("RGB")
    img = ImageOps.fit(img, (600, 600),Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    layers = list(img.split())

    enhance = ImageEnhance.Brightness(layers[0])
    layers[0] = enhance.enhance(0.94)
    enhance = ImageEnhance.Contrast(layers[0])
    layers[0] = enhance.enhance(1.1)

    enhance = ImageEnhance.Brightness(layers[1])
    layers[1] = enhance.enhance(1.21)
    enhance = ImageEnhance.Contrast(layers[1])
    layers[1] = enhance.enhance(0.75)

    enhance = ImageEnhance.Brightness(layers[2])
    layers[2] = enhance.enhance(1.48)
    enhance = ImageEnhance.Contrast(layers[2])
    layers[2] = enhance.enhance(1.2)


    img = Image.merge("RGB", layers)

    img_out = img.filter(ImageFilter.UnsharpMask(radius=0.8, percent=100, threshold=0))
    img_out.save(sys.argv[2])

#Instagram-ish filter 2
def inst_b(img):
    img = Image.open(sys.argv[1], mode="r")
    img = img.convert("RGB")
    img = ImageOps.fit(img, (600, 600),Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    layers = list(img.split())

    enhance = ImageEnhance.Brightness(layers[0])
    layers[0] = enhance.enhance(1.21)
    enhance = ImageEnhance.Contrast(layers[0])
    layers[0] = enhance.enhance(0.85)

    enhance = ImageEnhance.Brightness(layers[1])
    layers[1] = enhance.enhance(1.15)
    enhance = ImageEnhance.Contrast(layers[1])
    layers[1] = enhance.enhance(0.75)

    enhance = ImageEnhance.Brightness(layers[2])
    layers[2] = enhance.enhance(1.0)
    enhance = ImageEnhance.Contrast(layers[2])
    layers[2] = enhance.enhance(0.5)

    img = Image.merge("RGB", layers)
    contrast = ImageEnhance.Contrast(img)
    factor = 1.5
    img = contrast.enhance(factor)
    img_out = img.filter(ImageFilter.UnsharpMask(radius=0.8, percent=100, threshold=0))
    img_out.save(sys.argv[2])

#Instagram-ish filter 3 with a vingette blur
def inst_c(img):
    img = Image.open(sys.argv[1], mode="r")
    img = img.convert("RGB")
    img = ImageOps.fit(img, (600, 600),Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    layers = list(img.split())

    enhance = ImageEnhance.Brightness(layers[0])
    layers[0] = enhance.enhance(0.8)
    enhance = ImageEnhance.Contrast(layers[0])
    layers[0] = enhance.enhance(2.5)

    enhance = ImageEnhance.Brightness(layers[1])
    layers[1] = enhance.enhance(1.1)
    enhance = ImageEnhance.Contrast(layers[1])
    layers[1] = enhance.enhance(0.60)

    enhance = ImageEnhance.Brightness(layers[2])
    layers[2] = enhance.enhance(1.2)
    enhance = ImageEnhance.Contrast(layers[2])
    layers[2] = enhance.enhance(1.0)

    img = Image.merge("RGB", layers)
    contrast = ImageEnhance.Contrast(img)
    factor = 1.5
    img = contrast.enhance(factor)

    top_layer = img.filter(ImageFilter.BoxBlur(5))
    top_bright = ImageEnhance.Brightness(top_layer)
    factor = 0.58
    top_layer = top_bright.enhance(factor)
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((50, 50, 500, 500), fill = 255)
    mask_blur = mask.filter(ImageFilter.GaussianBlur(50))
    img = Image.composite(img, top_layer, mask_blur)


    img_out = img.filter(ImageFilter.UnsharpMask(radius=0.8, percent=100, threshold=0))
    img_out.save(sys.argv[2])


#Instagram-ish filter with a grunge mask
def inst_d(img):
    img = Image.open(sys.argv[1], mode="r")
    img = img.convert("RGB")
    img = ImageOps.fit(img, (600, 600),Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    layers = list(img.split())

    enhance = ImageEnhance.Brightness(layers[0])
    layers[0] = enhance.enhance(1.21)
    enhance = ImageEnhance.Contrast(layers[0])
    layers[0] = enhance.enhance(1.0)

    enhance = ImageEnhance.Brightness(layers[1])
    layers[1] = enhance.enhance(1.01)
    enhance = ImageEnhance.Contrast(layers[1])
    layers[1] = enhance.enhance(0.75)

    enhance = ImageEnhance.Brightness(layers[2])
    layers[2] = enhance.enhance(0.8)
    enhance = ImageEnhance.Contrast(layers[2])
    layers[2] = enhance.enhance(0.25)

    img = Image.merge("RGB", layers)
    texture = Image.open("templates/texture01.png", mode="r")
    mask = Image.new("L", img.size, 128)
    #img_out = Image.composite(img, texture, mask)
    img = Image.blend(img, texture, 0.15)

    contrast = ImageEnhance.Contrast(img)
    factor = 1.5
    img = contrast.enhance(factor)

    img_out = img.filter(ImageFilter.UnsharpMask(radius=0.8, percent=100, threshold=0))
    img_out.save(sys.argv[2])

# Polaroid style filter
def pol(img):
    img = Image.open(sys.argv[1], mode="r")
    img = img.convert("RGB")
    img = ImageOps.fit(img, (600, 600),Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    layers = list(img.split())

    enhance = ImageEnhance.Brightness(layers[0])
    layers[0] = enhance.enhance(0.8)
    enhance = ImageEnhance.Contrast(layers[0])
    layers[0] = enhance.enhance(0.75)

    enhance = ImageEnhance.Brightness(layers[1])
    layers[1] = enhance.enhance(1.02)
    enhance = ImageEnhance.Contrast(layers[1])
    layers[1] = enhance.enhance(0.5)

    enhance = ImageEnhance.Brightness(layers[2])
    layers[2] = enhance.enhance(0.89)
    enhance = ImageEnhance.Contrast(layers[2])
    layers[2] = enhance.enhance(0.5)

    img = Image.merge("RGB", layers)
    contrast = ImageEnhance.Contrast(img)
    factor = 1.65
    img = contrast.enhance(factor)
    bright = ImageEnhance.Brightness(img)
    factor = 1.3
    img = bright.enhance(factor)

    texture = Image.open("templates/texture02.png", mode="r")
    img.paste(texture, (0,0), mask=texture)

    img_out = img.filter(ImageFilter.UnsharpMask(radius=0.8, percent=100, threshold=0))
    img_out.save(sys.argv[2])

#handwritten CS50 Polaroid
def cs50(img):
    img = Image.open(sys.argv[1], mode="r")
    img = img.convert("RGB")
    img = ImageOps.fit(img, (600, 600),Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

    texture = Image.open("templates/texture03.png", mode="r")
    img.paste(texture, (0,0), mask=texture)

    img_out = img.filter(ImageFilter.UnsharpMask(radius=0.8, percent=100, threshold=0))
    img_out.save(sys.argv[2])


#argparse of command-line arguments
def create_parse():
    parser = argparse.ArgumentParser(description="Linnea's Image Filter Effects")
    parser.add_argument('before', type=str, metavar="", help="Original File to Edit")
    parser.add_argument('after', type=str, metavar="", help="New File with Filter")
    parser.add_argument('img', type=str, metavar="", help="Type of Filter")

    parser.add_argument('list', action="store_true", help="Filters to use: bw, cs50, inst_a, inst_b, inst_c, inst_d, pol, rd_color")

    return parser


#main function
def main():
    parser = create_parse()
    args = parser.parse_args()
    file = sys.argv[0]
    before = sys.argv[1]
    after = sys.argv[2]
    img = sys.argv[3]
    valid_file(args.before, args.after)
    valid_dict(sys.argv[3])

if __name__ == "__main__":
    main()
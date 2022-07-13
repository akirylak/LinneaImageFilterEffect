# Linnea Image Filter Effects
#### Video DEMO: https://youtu.be/R4YMv_tARG8c
#### Desciption:  This program is an image procesor, saving photos with assigned filters.  The filters were built utilizing the Pillow Libaray available for Python 3.0.

***
This Python Program was created as a Final Project for the HarvardX CS50P: Introduction to Python 2022 course via edx.org.  This code has been created by Amber Linnea Kirylak, EdX user: Kirylak_A, Github user: akirylak.
Submission Period:  July 2022.
***

**Goal of the Final Project**
To create a program that would accept a JPG/PNG/JPEG file and export a copy of a photo with a filter from the custom Linnea Image Filter Library.  These image filters are to emulate photo filter applications or instagram(TM) photo effects.

I wanted to create a program that utilized the skills I have in Post Production and Image processing to create a fun product.  This program can be used with a UX/UI design to create a user friendly application for the average user.

For the future, I would like to build more filters and create a HTML webpage for users to input and upload their own photos and output a saved manipulated image.

***Pseudocode used for creating the program***
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



**Getting Started**
To use this software, the following libraries must be installed in terminal.

```
os
Installed as part of Python Standard Library

sys
Installed as part of Python Standard Library

argparse
Python Argument Parse Library
pip install argparse

PIL
Python Pillow Library
pip install PIL

random
Installed as part of Python Standard Library
```

**To Use**
This Python code requires the use of command-line arguments.  A total of 4 command line arguements are required for this software to properly work.

Example:
python project.py before.jpg after.jpg bw

python project.py --- required to run the program
before.jpg --- image file you would like to have the photo filter applied to
after.jpg --- name of the file you would like the filtered image to save as
bw --- name of the filter in the custom library

Example 2:
python project.py john.jpg john2.jpg inst_a

python project.py --- required to run the program
john.png --- image file you would like to have the photo filter applied to
john2.png --- name of the file you would like the filtered image to save as
bw --- name of the filter in the custom library

***Rules for Command-Line Arguements***
1.  File names shall not be identical.  You may add digits after alphanumeric numbers to signify copies.
Example:  john.jpg, john2.jpg, mary_01.jpeg, mary_02.jpeg, joseph_before.png, joseph_after.png
2.  Filetypes must be the same as the input.
Example that will return an error:  john.jpg, john2.png
3.  Filetypes must be in the format of .JPG/.jpg, .PNG/.png or .JPEG/jpeg
4.  Filters are required and must be a Valid Filter available in the program (see filter options below).
5.  Missing command-line arguments will return an error
6.  Too many command-line arguments will return an error


***Filters Available for Version 1.0***
Filters are case sensitive.

bw        --- creates a black and white filter with unsharp mask
cs50      --- creates a Polaroid with a handwritten message by the creator
inst_a    --- filter that has a cross-processed blue effect
inst_b    --- filter that had a cross-processed yellow effect
inst_c    --- filter that has film distoration with a blurred vignette.
Inst_d    --- filter that has a grunge yellowing filter
pol       --- filter that has a Polaroid frame with distortion
rd_color  --- creates a monochrome image with a random color in the RGBCMY.  No two executions are the same

**Other Information**
python project.py -h

Reveals help guide along with available filters

Linnea's Image Filter Effects

positional arguments:
              Original File to Edit
              New File with Filter
              Type of Filter
  list        Filters to use: bw, cs50, inst_a, inst_b, inst_c, inst_d, pol, rd_color

options:
  -h, --help  show this help message and exit


**What is in the folder**
after.jpg       --- for testing purposes, it is the output file I used to test if the filter saves a file
amber.jpg       --- for testing purposes, it is the input file I used to test if the filter opens a file, applies and then saves the file as after.jpg
project.py      --- Python Program MAIN
README.md       --- This File you are reading right now
requirements.txt--- Required Libraries needing to be installed that are not included in the python standard library
test_project.py --- Test File for ensuring selected functions work


"""Code Created by Amber Linnea Kirylak for Harvard CS50P class Final Project"""

#testing code for project.py
import pytest
import warnings
from PIL import Image
from project import valid_file, valid_dict, bw, rd_color

def test_valid_file():
    assert valid_file('before.jpg', 'after.jpg')
    with pytest.raises(SystemExit):
        assert valid_file('before.png', 'after.jpg')
        assert valid_file('before.jpg', 'after.png')
        assert valid_file('before.jpg', 'after')
        assert valid_file('before', 'after.jpg')
        assert valid_file('before.pdf', 'after.jpg')
        assert valid_file('before.jpg', 'after.pdf')
    with pytest.raises(TypeError):
        assert valid_file('before.png')

def test_valid_dict():
    #image_filter_type = ("mod_bw","mod_color")
    try:
        valid_dict()
    except:
        NameError

def test_mod_bw():
    try:
        bw(Image.open("before.jpg"))
    except:
        SystemExit
    with pytest.raises(NameError):
        assert bw(Image.open(test))


def test_mod_color():
    try:
        rd_color(Image.open("before.jpg"))
    except:
        SystemExit
    with pytest.raises(NameError):
        assert bw(Image.open(test))
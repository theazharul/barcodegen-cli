#!/usr/bin/env python3
from distutils.core import setup
import py2exe
import click
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import textwrap

setup(console=['barcoder.py'])

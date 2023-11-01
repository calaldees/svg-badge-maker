"""
Open SVG as xml document
Find group 
Commendline
    Input
        svg template
        csv file
        Ask user for number of cols rows? or number of badges
        id="badge-template" (hopefully top left)
    Output
        svg filename (with number appended for multiple svg file for each A4 page)
            (print all pages from the commandline? maybe combine as giant pdf?)
         Pandoc filter to create PDF files from SVG  https://gist.github.com/jeromerobert/3996eca3acd12e4c3d40
    Process
        Possible 1: (a bit shit) x and y + badge x,y + text replacement (text in box == csv headings)
        Possible 2: (sounds more reusable) find width+height of badge and duplicate as many badges as possible in the rest of the document space
    Future Additions?
        QR code replacement and generation?
"""

from __future__ import annotations

from pathlib import Path
import csv

def open_csv_dict(path):
    if not isinstance(path, Path):
        path = Path(path)
    with path.open() as f:
        return tuple(csv.DictReader(f))
rr = open_csv_dict("test.csv")


FILENAME_SVG = 'a4-blank-test.svg'


from xml.dom.minidom import parse
dom = parse(FILENAME_SVG)

from xml.etree import ElementTree
root = ElementTree.parse(FILENAME_SVG).getroot()

id = "g3"

from typing import NamedTuple

class Rectangle(NamedTuple):
    x1: float
    y1: float
    x2: float
    y2: float
    @staticmethod
    def fromNode(node:ElementTree.Element):
        x1, y1, width, height = (float(node.get(k)) for k in ("x","y","width","height"))
        return Rectangle(x1, y1, x1+width, y1+height)
    def __add__(self, other:Rectangle):
        return Rectangle(
            min(self.x1, other.x1),
            min(self.y1, other.y1),
            max(self.x2, other.x2),
            max(self.y2, other.y2),
        )
    @property
    def width(self):
        return self.x2-self.x1
    @property
    def height(self):
        return self.y2-self.y1

width = float(root.get('width').strip('mm'))
height = float(root.get('height').strip('mm'))

#root.findall(".//{http://www.w3.org/2000/svg}g")
#root.find(".//{http://www.w3.org/2000/svg}g[@id='g3']").attrib


# https://stackoverflow.com/a/1954382/3356840
# ElementTree is a broken POS because every element-tag has a namespace appended to it.

# minidom is broken because getElementById does not work on all children (so why bother) ... why is xml so broken in python standard librarys

from functools import reduce
import operator

bb = reduce(operator.add, (Rectangle.fromNode(node) for node in root.findall(f".//*[@x]")))

breakpoint()

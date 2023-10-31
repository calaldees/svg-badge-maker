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
    Process
        Possible 1: (a bit shit) x and y + badge x,y + text replacement (text in box == csv headings)
        Possible 2: (sounds more reusable) find width+height of badge and duplicate as many badges as possible in the rest of the document space
    Future Additions?
        QR code replacement and generation?
"""

import numpy as np


#Find the fonts (move to style guide)
import matplotlib
matplotlib.font_manager._rebuild()

from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('font',**{'family':'sans-serif','sans-serif':['Verdana']})


##Useful functions
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple(np.array(255*np.array(rgb),dtype=int))

def make_rgb_transparent(rgb, bg_rgb, alpha):
    return [alpha * c1 + (1 - alpha) * c2
            for (c1, c2) in zip(rgb, bg_rgb)]

def hex_to_rgb(h):
    return [int(h[i:i + 2], 16) / 255. for i in (1, 3, 5)] # skip '#'


def add_logo_fitz(name_in,name_out,logo,pos=(50,0,200,40)):
    """
    Adds a logo (in pdf) to a pdf
    
    name_in = pdf input
    name_out = pdf output
    logo = filename of logo
    pos = position of logo (x_start,y_start,x_final,y_final). (0,0) is the top left corner
    """
    
    import fitz
    # define the position (upper-right corner)
    image_rectangle = fitz.Rect(*pos)

    # retrieve the first page of the PDF
    file_handle = fitz.open(name_in)
    first_page = file_handle[0]

    src = fitz.open(logo)  # show page 0 of this
    # add the image
    first_page.showPDFpage(image_rectangle, src=src,overlay=True)

    file_handle.save(name_out)
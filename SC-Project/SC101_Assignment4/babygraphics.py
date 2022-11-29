"""
File: babygraphics.py
Name: Yi Lin Yang
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE+((width-GRAPH_MARGIN_SIZE*2)/len(YEARS))*year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for year in YEARS:
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year))
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x_coordinate+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=year, anchor=tkinter.NW,
                           font='times')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # loop over look_up_names
    color_index = 0
    for i in range(len(lookup_names)):
        # first year on the figure
        x_coordinate_0 = get_x_coordinate(CANVAS_WIDTH, 0) + TEXT_DX
        if str(YEARS[0]) in name_data[lookup_names[i]]:
            rank_0 = str(name_data[lookup_names[i]][str(YEARS[0])])
            y_coordinate_0 = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE) * int(rank_0) // MAX_RANK
        else:
            rank_0 = '* '
            y_coordinate_0 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
        label_0 = lookup_names[i] + ' ' + rank_0
        canvas.create_text(x_coordinate_0, y_coordinate_0, text=label_0, fill=COLORS[color_index], anchor=tkinter.SW)

        # loop over YEARS except the first year
        for j in range(1, len(YEARS)):
            x_coordinate_j = get_x_coordinate(CANVAS_WIDTH, j)
            if str(YEARS[j]) in name_data[lookup_names[i]]:
                rank_j = str(name_data[lookup_names[i]][str(YEARS[j])])
                y_coordinate_j = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE) * int(rank_j) // MAX_RANK
            else:
                rank_j = '* '
                y_coordinate_j = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            label_j = lookup_names[i] + ' ' + rank_j
            canvas.create_text(x_coordinate_j, y_coordinate_j, text=label_j, fill=COLORS[color_index],
                               anchor=tkinter.SW)
            canvas.create_line(x_coordinate_0, y_coordinate_0, x_coordinate_j, y_coordinate_j, width=LINE_WIDTH,
                               fill=COLORS[color_index])

            # for line drawing, reassign the start point in each loop
            x_coordinate_0 = x_coordinate_j
            y_coordinate_0 = y_coordinate_j

        # considering index of COLORS out of range
        if color_index == len(COLORS):
            color_index = 0
        else:
            color_index += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()

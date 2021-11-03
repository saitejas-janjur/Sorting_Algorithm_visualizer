from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')

# variables
selected_alg = StringVar()
data = []


# function
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    offset = 30
    x_width = (c_width - offset) / len(data) # should take offset into account
    spacing = min(x_width/4, 10)  # spacing is at most 10
    normalizedData = [i/max(data) for i in data]
    for i, height in enumerate(normalizedData):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height* 340
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height  # y0 + x_width/2

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text((x0+x1)/2, y0, anchor=S, text=data[i])
    root.update_idletasks()


def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))

    drawData(data, ['red' for x in range(len(data))])  # ['red', 'red' ,....]


def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, drawData, speedScale.get())

    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())

    drawData(data, ['green' for x in range(len(data))])

#Outer frame

UI_frame = Frame(root, width= 600, height=200, bg='red')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=650, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# User Interface
Label(UI_frame, text="Algorithm: ", bg='white').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=0)
algMenu.current(0)

# Button to start the sorting algo
speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='white').grid(row=0, column=3, padx=5, pady=5)


# Number of data in array
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

# Min value of the array
minEntry = Scale(UI_frame, from_=1, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

# Max value of the array
maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

# Button to generate
Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)


root.mainloop()
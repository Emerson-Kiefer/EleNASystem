from tkinter import *
import tkintermapview 

#Add a new marker to map 
def add_marker_event(coords):
    print("Add marker:", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="new marker")

root = Tk()
root.title('OSM GUI')
root.geometry("1200x900")

my_label = LabelFrame(root)
# my_label.pack(pady=20)
my_label.grid(row=0, column=2, rowspan=80)

startLatitude = IntVar(None)
L1 = Label(root, text="Start Latitude:")
L1.grid(row=0, column=0)
E1 = Entry(root, bd=1, textvariable=startLatitude)
E1.grid(row=0, column=1)

startLongitude = IntVar()
L2 = Label(root, text="Start Longitude:")
L2.grid(row=1, column=0)
E2 = Entry(root, bd=1, textvariable=startLongitude)
E2.grid(row=1, column=1)

endLatitude = IntVar()
L3 = Label(root, text="End Latitude:")
L3.grid(row=2, column=0)
E3 = Entry(root, bd=1, textvariable=endLatitude)
E3.grid(row=2, column=1)

endLongitude = IntVar()
L4 = Label(root, text="End Longitude:")
L4.grid(row=3, column=0)
E4 = Entry(root, bd=1, textvariable=endLongitude)
E4.grid(row=3, column=1)

percent = IntVar()
L5 = Label(root, text="Percent of optimal distance :")
L5.grid(row=4, column=0)
E5 = Entry(root, bd=1, textvariable=percent)
E5.grid(row=4, column=1)


def generatePath():
    print("Percent: ", percent.get())
    print("Start: ", startLatitude.get(), startLongitude.get())
    print("End: ", endLatitude.get(), endLongitude.get())

B1 = Button(root, text="Generate Path", fg="green", bg="black", command= generatePath)
B1.grid(row=6, column=0)

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=800, corner_radius=0)

map_widget.set_position(42.386522559621, -72.5293540281545)
map_widget.set_zoom(15)

map_widget.add_right_click_menu_command(label="Add Marker", command=add_marker_event, pass_coords=True)

# path_1 = map_widget.set_path([marker_2.position, marker_3.position, (52.57, 13.4), (52.55, 13.35)])

# marker_1 = map_widget.set_marker(startString.get())
# if startString.get() != 
map_widget.grid(row=0, column = 2, rowspan=10)

root.mainloop()
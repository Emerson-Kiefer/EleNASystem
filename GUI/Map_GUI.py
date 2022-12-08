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


L1 = Label(root, text="Start Coordinates:")
L1.grid(row=0, column=0)
E1 = Entry(root, bd=1)
E1.grid(row=0, column=1)

L2 = Label(root, text="End Coordinates:")
L2.grid(row=1, column=0)
E2 = Entry(root, bd=1)
E2.grid(row=1, column=1)

L3 = Label(root, text="Percent of optimal distance :")
L3.grid(row=2, column=0)
E3 = Entry(root, bd=1)
E3.grid(row=2, column=1)

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=800, corner_radius=0)

map_widget.set_position(42.386522559621, -72.5293540281545)
map_widget.set_zoom(15)

map_widget.add_right_click_menu_command(label="Add Marker", command=add_marker_event, pass_coords=True)

marker_1 = map_widget.set_marker
map_widget.grid(row=0, column = 2, rowspan=10)

root.mainloop()
#pip install customtkinter
#pyinstaller
import os
import sys
import tkinter
from customtkinter import *
from tkinter import messagebox
from datetime import datetime
month = datetime.now().month
year = datetime.now().year
current_date = datetime.now()
start_of_year = datetime(current_date.year, 1, 1)
weeks_since_start = ((current_date - start_of_year).days // 7) + 1


window = CTk()
window.geometry("770*440")
set_appearance_mode("dark") #light , dark, system
window.resizable(False, False)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


window.title("Serial Number Generator")

def enter_data():
    #User info
    user_year = int(supply_yr_entry.get())
    user_week = int(supply_wk_entry.get())
    supply = supply_name_entry.get()
    name = program_name_entry.get()
    version = program_version_entry.get()
    serialstart = int(serial_start_entry.get())
    serialend = int(serial_end_entry.get())
    filenm = file_name_entry.get()


    a = int(serialstart)
    data = [""] * (int(serialend) - int(serialstart) + 1)  # Adjust the loop range
    data2 = [""] * (int(serialend) - int(serialstart) + 1)  # Adjust the loop range

    for x in range(int(serialstart), int(serialend) + 1):  # Adjust the loop range
        if x < 10:
            num = "-000"
        elif x > 9:
            num = "-00"
        if user_week < 10:
            num2 = "0"
        else:
            num2 = ""

        data2[x - a] = supply + "-" + str(user_year - 2000) + num2 + str(user_week) + num + str(x)  # Adjust the index
        data[x - a] = "@" + name + "@" + version + supply + "-" + str(user_year - 2000) + num2 + str(user_week) + num + str(x)  # Adjust the index

    # Merging Arrays         #=======#
    dataarray = [""] * 2 * (int(serialend) - int(serialstart) + 1)
    a = 0
    b = 0
    for y in range(2 * (int(serialend) - int(serialstart) + 1)):
        if y % 2 == 0:
            dataarray[y] = data[a]
            a = a + 1
        else:
            dataarray[y] = data2[b]
            b = b + 1

    if supply=="":
        tkinter.messagebox.showwarning(title="Error", message="Supply name is empty")
    elif name=="":
        tkinter.messagebox.showwarning(title="Error", message="Program name is empty")
    elif serialstart==serialend:
        tkinter.messagebox.showwarning(title="Error", message="Start Serial number and End Serial number is same")
    else:
        #Write data to txt file 
        file_path = r"c:\Downloads\\" + filenm + ".txt"


        with open(file_path, "w") as file:
            for item in dataarray: #====#
                file.write(item + "\n")

        print("Data written")

infopadx = 30
infopady = 15
fontfamily = "Helvetica"
fontsize = 20

frame = CTkFrame(master = window, fg_color="#242424")
frame.pack()

#1st data frame
info_frame = CTkFrame(master = frame, fg_color = "#E3170A", border_color = "#F4544A", border_width = 3)
info_frame.grid(row=0, column=0, padx=infopadx, pady=infopady)

supply_yr_label = CTkLabel(master = info_frame, text= "Supply year")
supply_yr_label.grid(row=0, column=0)

supply_wk_label = CTkLabel(master = info_frame, text= "Supply week")
supply_wk_label.grid(row=0, column=1)

supply_name_label = CTkLabel(master = info_frame, text= "Supply name")
supply_name_label.grid(row=0, column=2)

slider_label_1 = CTkLabel(master = info_frame, text= year)
slider_label_1.grid(row=1, column=0)

slider_label_2 = CTkLabel(master = info_frame, text= weeks_since_start)
slider_label_2.grid(row=1, column=1)

#SLIDERS ========

def slider1(value):
    slider_label_1.configure(text=int(value))
    if(value == year):
        supply_wk_entry.configure(from_=weeks_since_start)
        slider_label_2.configure(text = weeks_since_start)
        supply_wk_entry.set(weeks_since_start)
    else:
        supply_wk_entry.configure(from_= 1)
        slider_label_2.configure(text = 1)
        supply_wk_entry.set(1)

def slider2(value):
    slider_label_2.configure(text=int(value))

supply_yr_entry = CTkSlider(master = info_frame, from_=year, to=year+20, button_color="black", button_hover_color = "#242424", progress_color="black", command=slider1)
supply_yr_entry.grid(row=2, column=0)
supply_yr_entry.set(year)


supply_wk_entry = CTkSlider(master = info_frame, from_=weeks_since_start, to=53, button_color="black", button_hover_color = "#242424", progress_color="black", command=slider2)
supply_wk_entry.grid(row=2, column=1)
supply_wk_entry.set(weeks_since_start)

#SLIDERS ========

supply_name_entry = CTkEntry(master = info_frame, placeholder_text= "Enter Supply Name...", width=250)
supply_name_entry.grid(row=1, column=2)

for widget in info_frame.winfo_children():
    widget.grid_configure(padx=infopadx, pady=infopady)
    if isinstance(widget, (CTkEntry, CTkLabel)):
        widget.configure(font=(fontfamily,fontsize))

#Pink frame
info_frame_2 = CTkFrame(master = frame, fg_color = "#de0d92", border_color = "#f549b6", border_width = 3)
info_frame_2.grid(row=1, column=0, padx=infopadx, pady=infopady)

serial_start_label = CTkLabel(master = info_frame_2, text= "Serial Start Value")
serial_start_label.grid(row=0, column=0)

serial_end_label = CTkLabel(master = info_frame_2, text= "Serial End Value")
serial_end_label.grid(row=0, column=1)

file_name_label = CTkLabel(master = info_frame_2, text= "File name")
file_name_label.grid(row=0, column=2)

slider_label_3 = CTkLabel(master = info_frame_2, text= 0)
slider_label_3.grid(row=1, column=0)

slider_label_4 = CTkLabel(master = info_frame_2, text= 100)
slider_label_4.grid(row=1, column=1)

#SLIDERS ========

def slider3(value):
    slider_label_3.configure(text=int(value))

def slider4(value):
    slider_label_4.configure(text=int(value))

serial_start_entry = CTkSlider(master = info_frame_2, from_=0, to=100, button_color="black", button_hover_color = "#242424", progress_color="black", command=slider3)
serial_start_entry.grid(row=2, column=0)
serial_start_entry.set(0)

serial_end_entry = CTkSlider(master = info_frame_2, from_=1, to=300, button_color="black", button_hover_color = "#242424", progress_color="black", command=slider4)
serial_end_entry.grid(row=2, column=1)
serial_end_entry.set(100)

#SLIDERS ========

file_name_entry = CTkEntry(master = info_frame_2, placeholder_text= "Enter File Name...", width=250)
file_name_entry.grid(row=1, column=2)

for widget in info_frame_2.winfo_children():
    widget.grid_configure(padx=infopadx, pady=infopady)
    if isinstance(widget, (CTkEntry, CTkLabel)):
        widget.configure(font=(fontfamily,fontsize))

#Blue Frame
info_frame_3 = CTkFrame(master = frame, fg_color = "#4464ad", border_color = "#6782c0", border_width = 3)
info_frame_3.grid(row=2, column=0, padx=infopadx, pady=infopady)

program_name_label = CTkLabel(master = info_frame_3, text= "Program Name")
program_name_label.grid(row=0, column=0)

program_version_label = CTkLabel(master = info_frame_3, text= "Program Version")
program_version_label.grid(row=0, column=1)

program_name_entry = CTkEntry(master = info_frame_3, placeholder_text= "Enter Program Name...", width=250)
program_name_entry.grid(row=1, column=0)

program_version_entry = CTkEntry(master = info_frame_3, placeholder_text= "Enter Program Version...", width=250)
program_version_entry.grid(row=1, column=1)

for widget in info_frame_3.winfo_children():
    widget.grid_configure(padx=infopadx, pady=infopady)
    if isinstance(widget, (CTkEntry, CTkLabel)):
        widget.configure(font=(fontfamily,fontsize))

#Green Button
button = CTkButton(master = frame, fg_color="#20a149", text = "Enter Data", font=(fontfamily,fontsize), hover_color = "#15692f", width=250, height=40, command=enter_data)
button.grid(row=3, column=0, padx=infopadx, pady=infopady)

window.mainloop()
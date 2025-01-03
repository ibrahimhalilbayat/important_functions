try:
    import matplotlib
    import matplotlib.pyplot as plt
    from geopy.distance import distance
    from geopy.point import Point
    from numpy import deg2rad, sin, tan
    import os 
    from datetime import datetime
    import csv
    from geopy.distance import geodesic
    from pandas import read_csv, read_excel, notna
    import tkinter as tk
    from tkinter import ttk
    from tkinter import filedialog
    from openpyxl import Workbook, load_workbook
    from adjustText import adjust_text
    import sys

    matplotlib.use('TkAgg')

except Exception as e:
    print("An error occured during importing the libraries: ", e)

class RedirectStdout:
    """Custom class to redirect stdout to a Tkinter Text widget."""
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert("end", string)
        self.text_widget.see("end")

    def flush(self):
        """Needed for Python's logging module compatibility."""
        pass

def show_frame(frame):
    '''
    Function to show the interface
    '''
    frame.tkraise()

def create_menu(container, arayuzler, name, button_text, label_text):
    '''
    Function to create menu.
    '''
    frame = tk.Frame(container, bg=BACKGROUND_COLOR)
    arayuzler[name] = frame
    frame.grid(row=0, column=0, sticky="nsew")
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    label = tk.Label(frame, text=label_text, font=("Arial", 16), bg=BACKGROUND_COLOR, fg=LETTER_COLOR)
    label.pack(pady=20)

    back_button = tk.Button(frame, text="Back to Main Menu", font=("Arial", 12), command=lambda: show_frame(main_menu), bg=BUTTON_COLOR, fg=LETTER_COLOR)
    back_button.pack(pady=20)

    button = tk.Button(main_menu, text=button_text, font=("Arial", 12), command=lambda: show_frame(frame), bg=BUTTON_COLOR, fg=LETTER_COLOR)
    button.pack(pady=5)

def something_function(something_input, output_label):
    '''
    A random function
    '''

    the_string =  f"User input is: {something_input}"
    output_label.config(text=the_string)

    return the_string


BACKGROUND_COLOR = "dark slate gray"
LETTER_COLOR = "white"
BUTTON_COLOR = "gray0"

INFO_TEXT = """

This text is for informaiton. I like sports and music. I listen a wide range of types. I love hitting the gym. Life is beautiful
"""
try:
    root = tk.Tk()
    root.title("İbo Interaface")
    root.geometry("800x600")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    container = tk.Frame(root, background=BACKGROUND_COLOR)
    container.grid(row=0, column=0, sticky="nsew")

    container.columnconfigure(0, weight=1)
    container.rowconfigure(0, weight=1)

    arayuzler = {}

    main_menu = tk.Frame(container, background=BACKGROUND_COLOR)
    arayuzler["main_menu"] = main_menu
    main_menu.grid(row=0, column=0, sticky="nsew")

    title_label = tk.Label(root, text="İbrahim Halil BAYAT", font=("Arial", 14), background=BACKGROUND_COLOR)
    title_label.place(relx=1.0, rely=1.0, anchor="se")

    # Main menu label
    label = tk.Label(main_menu, text="Welcome!\n\n\nMAIN MENU", font=("Arial", 16), bg=BACKGROUND_COLOR, fg=LETTER_COLOR)
    label.pack(pady=20)

    create_menu(container, arayuzler, "Information", "Information", "Information")
    create_menu(container, arayuzler, "Something", "Something","Something")

    
    # EXE0 "Info"  --------------------------------------------------------------------------------------------------------------------------------------------
    exe0_mesafe_arayuzu = arayuzler["Information"]

    exe0_canvas = tk.Canvas(exe0_mesafe_arayuzu, bg=BACKGROUND_COLOR)
    exe0_canvas.pack(side="left", fill="both", expand=True)

    exe0_scrollbar = ttk.Scrollbar(exe0_mesafe_arayuzu, orient="vertical", command=exe0_canvas.yview)
    exe0_scrollbar.pack(side="right", fill="y")
    exe0_canvas.configure(yscrollcommand=exe0_scrollbar.set)

    def exe0_on_mouse_wheel(event):
        exe0_canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    exe0_canvas.bind("<MouseWheel>", exe0_on_mouse_wheel)
    exe0_canvas.bind("<Button-4>", lambda event: exe0_canvas.yview_scroll(-1, "units"))
    exe0_canvas.bind("<Button-5>", lambda event: exe0_canvas.yview_scroll(1, "units"))

    exe0_entry_container = tk.Frame(exe0_canvas, bg=BACKGROUND_COLOR)
    exe0_canvas.create_window((0, 0), window=exe0_entry_container, anchor="nw")

    def exe0_update_scrollregion(event=None):
        exe0_canvas.configure(scrollregion=exe0_canvas.bbox("all"))

    exe0_entry_container.bind("<Configure>", exe0_update_scrollregion)

    info_label = tk.Label(exe0_entry_container, text=INFO_TEXT, font=("Arial", 12), justify="left", wraplength=700, bg=BACKGROUND_COLOR, fg=LETTER_COLOR)
    info_label.pack(pady=10)


    # EXE1 "Something function" ----------------------------------------------------------------------------------------------------------------------------
    exe1_mesafe_arayuzu = arayuzler["Something"]
    exe1_canvas = tk.Canvas(exe1_mesafe_arayuzu, bg=BACKGROUND_COLOR)
    exe1_canvas.pack(side="left", fill="both", expand=True)
    exe1_scrollbar = ttk.Scrollbar(exe1_mesafe_arayuzu, orient="vertical", command=exe1_canvas.yview)
    exe1_scrollbar.pack(side="right", fill="y")
    exe1_canvas.configure(yscrollcommand=exe1_scrollbar.set)

    def exe1_on_mouse_wheel(event):
        exe1_canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    exe1_canvas.bind("<MouseWheel>", exe1_on_mouse_wheel)  
    exe1_canvas.bind("<Button-4>", lambda event: exe1_canvas.yview_scroll(-1, "units")) 
    exe1_canvas.bind("<Button-5>", lambda event: exe1_canvas.yview_scroll(1, "units"))  

    exe1_entry_container = tk.Frame(exe1_canvas, bg=BACKGROUND_COLOR)
    exe1_canvas.create_window((0, 0), window=exe1_entry_container, anchor="nw")

    def exe1_update_scrollregion(event=None):
        exe1_canvas.configure(scrollregion=exe1_canvas.bbox("all"))

    exe1_entry_container.bind("<Configure>", exe1_update_scrollregion)

    exe1_labels_entries = [
        ("Please type your input: ", "User Input"),
    ]

    exe1_entries = {}

    for label_text, entry_key in exe1_labels_entries:
        tk.Label(exe1_entry_container, text=label_text, font=("Arial", 14), bg=BACKGROUND_COLOR, fg=LETTER_COLOR).pack(pady=10)
        entry = tk.Entry(exe1_entry_container, font=("Arial", 14), bg=BACKGROUND_COLOR, fg=LETTER_COLOR)
        entry.pack(pady=10)
        exe1_entries[entry_key] = entry

    exe1_output_label = tk.Label(exe1_entry_container, text="", font=("Arial", 14), bg=BACKGROUND_COLOR, fg=LETTER_COLOR)
    exe1_output_label.pack(pady=10)

    exe1_calculate_button = tk.Button(
        exe1_entry_container,
        text="Submit",
        font=("Arial", 12),
        command=lambda: something_function(
            exe1_entries["User Input"].get(),
            exe1_output_label,
        ),
    )
    exe1_calculate_button.pack(pady=10)

    show_frame(main_menu)
    root.mainloop()


except Exception as e:
    print("An exception occured: ", e)
    
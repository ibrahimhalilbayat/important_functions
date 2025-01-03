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
    print("An exception occured in importing libraries: ", e)

def parse_coord(coord_string):
    '''
    Function to convert degree, minute, second to float 
    '''
    try:
        if ' ' in coord_string:
            degrees, minutes, seconds = map(float, coord_string.split())
            return degrees + (minutes / 60) + (seconds / 3600)
        else:
            return float(coord_string)
    except Exception as e:
        print("An excepition occured in parse_coord function", e)

def calculate_distance(coord1, coord2):
    '''
    Calculate the distance between two points
    Input: (lat, lon) , (lat, lon) 
    Output: Distance in KM
    '''
    try:
        return geodesic(coord1, coord2).km
    except Exception as e:
        print("An exception occured in calculate_distance function: \n", e)

def calculate_new_position(lat, lon, bearing, distance_km):
    '''
    Calculating new coordinate based on input
    '''
    try:
        start_point = Point(lat, lon)
        destination = distance(kilometers=distance_km).destination(start_point, bearing)
        return destination.latitude, destination.longitude
    except Exception as e:
        print("An exception occured in calculate_new_position:", e)


# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 17:12:34 2023

@author: HP

""""importing the required python packages"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""Reading data set using pandas"""
# Using square brackets to create a list of column names
Productivity_and_Hourly_Compensation_1948_2021 = [
    'year',
    'net_productivity_per_hour_worked',
    'average_compensation_of_production_and_nonsupervisory_workers',
    'average_compensation',
    'median_compensation',
    'men_median_compensation',
    'women_median_compensation'
]

def read_dataset(file_path):
    return pd.read_csv(file_path)

"""function to plot line plot"""
def line_plot(x, y1, y2, x_label, y_label, title, label1, label2):
    """
    Plotting the line graph using the given data.
    
    Arguments:
    x: str - column name for the x-axis
    y1: str - column name for the y-axis
    y2: str - column name for the y-axis
    title: str - title for the line graph
    
    Returns:
    None
    """
    """Plotting a line graph"""
    plt.plot(x, y1, marker='o', linestyle='-', label=label1)
    plt.plot(x, y2, marker='o', linestyle='-', label=label2)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.show()

def scatter_plot(x1, y, x_label, y_label, title):
    """Creating a scatter plot"""
    plt.scatter(x1, y, marker='o', color='r', alpha=0.5)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.show()

def histogram(data, bins, x_label, y_label, title):
    """Creating a histogram"""
    plt.hist(data, bins=bins, edgecolor='black', alpha=0.7)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.show()

# Read dataset
df = read_dataset("C:\\Users\\HP\\Downloads\\archive (1)\\productivity_n_hourly_compensation.csv")


# Create line_plot
line_plot(df['year'], df['men_median_compensation'], df['women_median_compensation'],
          'Year', 'Net Productivity Per Hour Worked', 'Productivity Over the Years', 'Men', 'Women')

# Create scatter plot
scatter_plot(df['net_productivity_per_hour_worked'], df['average_compensation_of_production_and_nonsupervisory_workers'],
             'Net Productivity Per Hour Worked', 'Productivity of Avg and Non-supervisory Workers',
             'Hours per average productivity and non-supervisory workers')

# Create histogram
histogram(df['average_compensation'], bins=15, x_label='average_compensation',
          y_label='Median compensation of workers', title='wages of avg v/s median compensation')
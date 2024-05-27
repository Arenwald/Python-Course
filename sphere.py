"""
Program quintanilla_sphere.py
Author: Carlos Quintanilla
Date: 05/24/2024

This program calculates the diameter, circumference, 
surface area, and volume of a sphere.
It promps the user for the radius of the sphere.
Results are rounded to 3 digit decimal.

Input: The radius as an int or floating-point number.

Output: Diameter, Circumference, Surface Area, and Volume of a Sphere.

Equations:
diameter: 2 * radius
circunference: diameter * PI
surface area: 4 * PI * radius * radius
volume: 4/3 * PI * radius * radius * radius

"""

from math import pi #for simplicity, only imports pi to use on equations

#Input Begings

#Get "radius” from the user.
radius = float(input("Enter the radius: ", )) 

#convert radius int to floating number

float(radius) #convert int into a float number

#Equations Beging

#Calculate diameter
diameter = 2 * radius

#calulate circumference
circumference = diameter * pi

#calculate surface area
surface_area = 4 * pi * radius * radius

#calculate volume
volume = 4/3 * pi * radius * radius * radius

#Output Begings

#display the results rounded to 3 decimals
print("The Diameter of the Sphere is ", round(diameter,3))
print("The Circumference of the Sphere is ", round(circumference,3))
print("The Surface Area of the Sphere is ", round(surface_area,3))
print("The Volume of the Sphere is ", round(volume,3))

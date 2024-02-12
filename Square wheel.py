#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:00:04 2024

@author: jamescraig
"""

import numpy as np
import matplotlib.pyplot as plt

# Implicit cartesian equation for square of side lenth a

# |x-y|+|x+y| = a

# In polar form

# |rcos(theta)-rsin(theta)|+|rcos(theta)+rsin(theta)| = a

# r = a*1/(|cos(theta)-sin(theta)|+|cos(theta)+sin(theta)|)


# Tracing the distance from axle as a function of angle for a square wheel with axle at centre
a = 2

theta = np.arange(0,360,1)
theta_rad = np.radians(theta)
r = a*1/(np.abs(np.cos(theta_rad)-np.sin(theta_rad))+np.abs(np.cos(theta_rad)+np.sin(theta_rad)))
    
    
fig = plt.figure()
plt.plot(theta,r, 'k.')
plt.xlabel('$\Theta / ^{\circ}$')
plt.ylabel('Radius')
plt.show()

# Distance below axis

dist = -r

fig = plt.figure()
plt.plot(theta,dist)
plt.xlabel('$\Theta / ^{\circ}$')
plt.ylabel('y-position')
plt.savefig('Trace_for_square_wheel.pdf')
plt.show()



# Trace for ellipse with centre at origin
# Define semi-major and minor axis
a = 3
b = 2

ecc = np.sqrt(1-(b**2/a**2))

r1 = b/(np.sqrt(1-ecc**2*np.cos(theta_rad)**2))

fig = plt.figure()
plt.plot(theta,r1, 'k.')
plt.xlabel('$\Theta / ^{\circ}$')
plt.ylabel('Radius')
plt.show()

# Distance below axis

dist1 = -r1

fig = plt.figure()
plt.plot(theta,dist1)
plt.xlabel('$\Theta / ^{\circ}$')
plt.ylabel('y-position')
plt.savefig('Trace_for_centre_ellipse_wheel.pdf')
plt.show()


# Ellipse with foci at origin

r2 = a*(1-ecc**2)/(1+ecc*np.cos(theta_rad))

fig = plt.figure()
plt.plot(theta,r2, 'k.')
plt.xlabel('$\Theta / ^{\circ}$')
plt.ylabel('Radius')
plt.show()

# Distance below axis

dist2 = -r2

fig = plt.figure()
plt.plot(theta,dist2)
plt.xlabel('$ \Theta / ^{\circ}$')
plt.ylabel('y-position')
plt.savefig('Trace_for_focus_ellipse_wheel.pdf')
plt.show()

def Road_Plotter( x, y, a, b):
    """
    Road_Plotter - Function to plot visualisation of road surface 

    Parameters
    ----------
    x : array of x values for closed shape.
    y : array of y values for closed shape.
    a : x-coordinate of axle.
    b : y-coordinate of axle.

    Returns
    -------
    None.

    """
    # Calculates r and theta for each data point assuming axle is at (a,b)
    r = np.sqrt((a-x)**2+(b-y)**2)
    theta = np.arctan((b-y)/(a-x))
    dist = -r
    
    # Plots the distance from the axle to the rim of wheel
    fig = plt.figure()
    plt.plot(theta,dist)
    plt.xlabel('$\Theta / ^{\circ}$')
    plt.ylabel('y-position')
    plt.show()
    
    
    
    
# Plot of shape of road for an ellipse with the axle at one focus for k=1 and ecc = 1/sqrt(2)
    
fig = plt.figure()
x = np.arange(0,12.5,0.1)
y = -np.sqrt(2)+np.cos(x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('ellipse_focus_vals.pdf')
plt.show()
    










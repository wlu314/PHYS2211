from vpython import *
#GlowScript 3.0 VPython
## PHYS 2211 Online
## Lab 1: Constant Velocity
## 2211-lab1start.py
## Last updated: 2021-01-11 EAM


## =====================================
## VISUALIZATION & GRAPH INITIALIZATION
## =====================================

# Uncomment this next line if you prefer a white background
#scene.background = color.white

# Visualization (object, trail, origin)
ball = sphere(color=color.blue, radius=0.22)
trail = curve(color=color.green, radius=0.02)
origin = sphere(pos=vector(0,0,0), color=color.yellow, radius=0.04)

# Graphing (if needed, you can add more plot and curve lines)
plot = graph(title="Position vs Time", xtitle="Time (s)", ytitle="Position (m)")
poscurve = gcurve(color=color.green, width=4)
plot = graph(title="Velocity vs Time", xtitle="Time (s)", ytitle="Velocity (m/s)")
velcurve = gcurve(color=color.green, width=4)


## =======================================
## SYSTEM PROPERTIES & INITIAL CONDITIONS 
## =======================================

# System Mass -- EDIT THIS NEXT LINE
ball.m = 1

# Initial Conditions -- EDIT THESE TWO LINES (as necessary)
ball.pos = vector(0,0,0)
ball.vel = vector(0.7512,0,0)

# Time -- EDIT THESE TWO LINES (as necessary)
t = 0           # where the clock starts
deltat = 0.01   # size of each timestep



## ======================================
## CALCULATION LOOP
## (motion prediction and visualization)
## ======================================

while t < 2.5:
    # Control how fast the program runs (larger number runs faster)
    rate(100)
    
    # Calculate Net Force -- EDIT THIS NEXT LINE (add more lines if necessary)
    Fnet = vector(0,0,0)

    # Apply the Momentum Principle (Newton's 2nd Law)
    # Update the object's velocity -- EDIT THIS NEXT LINE

    ball.vel = ball.vel 
    
    # Update the object's position -- EDIT THIS NEXT LINE
    ball.pos = ball.pos + ball.vel * deltat
    
    # Advance the clock
    t = t + deltat
    # Update the object's track
    trail.append(pos=ball.pos)

    # Plot position and velocity as a function of time
    poscurve.plot(t,ball.pos.x)
    velcurve.plot(t,ball.vel.x)
    
    # Displaying the position values
    # The information that gets printed is the same as the information that is plotted above
    # EDIT THIS NEXT LINE if you want to output velocity instead
    print(t,ball.pos.x)

print("All done!")
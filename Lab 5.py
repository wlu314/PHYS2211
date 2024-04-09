from vpython import *
import numpy as np

## ===========================================
## INITIAL CONSTANTS, ANGLES, ANGULAR VELOCITY
## ===========================================

## Constant of gravitational force near Earth's Surface
g = 9.8

## Starting angles of the pendulum represented in FBD (theta)
theta1 = 90 * np.pi / 180  # Theta for the first pendulum
theta2 = 180 * np.pi / 180  # Theta for the second pendulum

## Starting Angular Velocity (rad/s)
omega1 = 0  # Angular velocity of the first pendulum
omega2 = 1  # Angular velocity of the second pendulum

## Mass (kgs) and Length (meters)
L1 = 2
L2 = 2
M1 = 2
M2 = 2

## INITIALIZING THE SYSTEM
pivot = sphere(pos=vector(0, L1, 0), radius=0.05)
m1 = sphere(pos=pivot.pos-vector(0, L1, 0), radius=0.05, color=color.white)
rod1 = cylinder(pos=pivot.pos, axis=m1.pos-pivot.pos, radius=0.015, color=color.yellow)
m2 = sphere(pos=m1.pos-vector(0, L2, 0), radius=0.05, color=color.white)
rod2 = cylinder(pos=m1.pos, axis=m2.pos-m1.pos, radius=0.015, color=color.yellow)

## Update the position of the balls and rods according to the Starting Theta
m1.pos = pivot.pos + vector(L1*np.sin(theta1), -L1*np.cos(theta1), 0)
m2.pos = m1.pos + vector(L2*np.sin(theta2), -L2*np.cos(theta2), 0)
rod1.axis = m1.pos - pivot.pos
rod2.pos = m1.pos
rod2.axis = m2.pos - m1.pos

## Time and Time Increment
t = 0
dt = 0.0001

# Initialize the graphs
changeEnergyGraph = graph(title='Change in Total Energy vs Time', xtitle='Time', ytitle='Change in Energy')
keGraph = graph(title='Kinetic Energy vs Time', xtitle='Time', ytitle='Kinetic Energy')
peGraph = graph(title='Potential Energy vs Time', xtitle='Time', ytitle='Potential Energy')

changeEnergyCurve = gcurve(color=color.cyan, graph=changeEnergyGraph)
keCurve = gcurve(color=color.red, graph=keGraph)
peCurve = gcurve(color=color.green, graph=peGraph)

attach_trail(m2, retain=1000)

while t < 50:
    rate(10000)
    
    ## Lagrange Equations for theta1 and theta2
    alpha1 = (-g*(2*M1+M2)*np.sin(theta1) - M2*g*np.sin(theta1-2*theta2) - 2*np.sin(theta1-theta2)*M2*(L2*omega2**2 + L1*np.cos(theta1-theta2)*omega1**2)) / (L1*(2*M1+M2-M2*np.cos(2*theta1-2*theta2)))
    alpha2 = (2*np.sin(theta1-theta2)*((M1+M2)*L1*omega1**2 + g*(M1+M2)*np.cos(theta1) + L2*M2*np.cos(theta1-theta2)*omega2**2)) / (L2*(2*M1+M2-M2*np.cos(2*theta1-2*theta2)))
    
    ## Euler Formula for Update Angular Velocity
    omega2 = omega2 + alpha2*dt
    omega1 = omega1 + alpha1*dt
    
    ## Update angles
    theta1 = theta1 + omega1*dt
    theta2 = theta2 + omega2*dt
    
    ## Update Position of M1, M2, Rod1, Rod2, and Time
    m1.pos = pivot.pos + vector(L1*np.sin(theta1), -L1*np.cos(theta1), 0)
    m2.pos = m1.pos + vector(L2*np.sin(theta2), -L2*np.cos(theta2), 0)
    rod1.axis = m1.pos - pivot.pos
    rod2.pos = m1.pos
    rod2.axis = m2.pos - m1.pos
    t = t + dt

    
    # Velocities of masses
    v1 = np.sqrt((L1 * omega1)**2)
    v2 = np.sqrt((L1 * omega1)**2 + (L2 * omega2)**2 + 2 * L1 * L2 * omega1 * omega2 * np.cos(theta1 - theta2))
    
    # Kinetic energy: KE = 1/2 * m * v^2
    KE1 = 0.5 * M1 * v1**2
    KE2 = 0.5 * M2 * v2**2
    KE_total = KE1 + KE2

    # Potential energy: PE = mgh
    h1 = L1 * (1 - np.cos(theta1))
    h2 = L1 * (1 - np.cos(theta1)) + L2 * (1 - np.cos(theta2))
    PE1 = M1 * g * h1
    PE2 = M2 * g * h2
    PE_total = PE1 + PE2
    
    # Update the energy plot
    total_energy = KE_total + PE_total
    
    keCurve.plot(t, KE_total)
    peCurve.plot(t, PE_total)
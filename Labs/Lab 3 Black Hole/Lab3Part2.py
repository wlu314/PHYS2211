Web VPython 3.2

## PHYS 2211
## Lab 3: Black Hole - Part 2



## =====================================
## VISUALIZATION & GRAPH INITIALIZATION
## =====================================

# White background so the black hole is visible
scene.background = color.white

# Visualization (object, trail, origin)
bh = sphere(pos=vec(0,0,0), color=color.black, radius=2e8)
planet = sphere(pos=vec(1e10,0,0), color=color.cyan, radius=1e8)
trailplanet = curve(color=color.cyan)
ship = sphere(pos=vec(planet.pos.x,planet.radius,0), color=color.magenta, radius=3e7)
trailship = curve(color=color.magenta)


## =======================================
## SYSTEM PROPERTIES & INITIAL CONDITIONS 
## =======================================


# Mass of the black hole 
# EDIT THIS LINE with your result from Part 1 of the lab
bh.m = 8.70964e33


# Other constants - DO NOT CHANGE THESE FIVE LINES
G = 6.7e-11             # gravitational constant
planet.m = 9e28         # mass of planet
ship.m = 7e10           # mass of spaceship
deltat = 1              # deltat (in seconds)
t=0                     # initial time
# DO NOT CHANGE THE ABOVE FIVE LINES


# Maximum time to run the simulation
# Default is ONE HOUR, but you can change it to a longer
# amount (e.g., 2hrs, 5hrs, etc) if you need more time to
# visualize a full orbit
tmax=60*60  


# Initial conditions for the planet 
planet_speed = sqrt(G * bh.m / mag(planet.pos) )
planet.vel = vec(0,planet_speed,0)
print("Planet's orbital speed:", planet_speed, "m/s")
print("Planet's orbital period:", (2*pi*mag(planet.pos)/planet_speed)/(60*60), "hrs")
print("---")


# Initial conditions for the spaceship
# EDIT THESE LINES as needed to change the initial velocity of the ship
# Remember that your spaceship cannot move faster than the speed of light
ship_speed_x = -7.26e6
ship_speed_y = 7.9e6
ship.vel = vec(ship_speed_x, ship_speed_y, 0)



## =================
## CALCULATION LOOP
## =================

while t < tmax:
    rate(100)

    # Net force on the planet
    # EDIT THESE LINES (and/or add more if needed) to find:
    # 1) Fgrav on the planet by the black hole
    # 2) Fgrav on the planet by the spaceship
    # 3) the net force on the planet
    r_bh_to_planet = planet.pos-bh.pos
    r_hat_bh_to_planet = r_bh_to_planet / mag(r_bh_to_planet)
    F_bh_ON_planet = -(G*bh.m*planet.m)/(mag(r_bh_to_planet)**2)*r_hat_bh_to_planet
    
    r_ship_to_planet = planet.pos-ship.pos
    r_hat_ship_to_planet = r_ship_to_planet/mag(r_ship_to_planet)
    F_ship_ON_planet = -(G*planet.m*ship.m)/(mag(r_ship_to_planet)**2)*r_hat_ship_to_planet
    
    Fnet_ON_planet = F_ship_ON_planet + F_bh_ON_planet
    
    
    # Net force on the spaceship
    # EDIT THESE LINES (and/or add more if needed) to find:
    # 1) Fgrav on the spaceship by the black hole
    # 2) Fgrav on the spaceship by the planet
    # 3) the net force on the spaceship
    r_bh_to_ship = ship.pos - bh.pos 
    print (mag(r_bh_to_ship))
    r_hat_bh_to_ship = r_bh_to_ship / mag(r_bh_to_ship)
    F_bh_ON_ship = -(G*bh.m*ship.m)/(mag(r_bh_to_ship)**2)*r_hat_bh_to_ship
    
    r_planet_to_ship = ship.pos-planet.pos
    r_hat_planet_to_ship = r_planet_to_ship/mag(r_planet_to_ship)
    F_planet_ON_ship = -(G*planet.m*ship.m)/(mag(r_planet_to_ship)**2)*r_hat_planet_to_ship

    Fnet_ON_ship = F_bh_ON_ship + F_planet_ON_ship


    # MAKING THINGS MOVE   
    # Apply Newton's 2nd law and the position update formula 
    # to make the planet and spaceship move
    planet.vel = planet.vel + ((Fnet_ON_planet)/planet.m) * deltat
    planet.pos = planet.pos + planet.vel * deltat

    ship.vel = ship.vel + ((Fnet_ON_ship)/ship.m)*deltat
    ship.pos = ship.pos + ship.vel*deltat 


    # Adding break conditions, in case of a crash
    # Do not edit these lines
    if mag(r_bh_to_ship) < bh.radius:
        print("Oh no, you got sucked into the black hole!")
        break
    if mag(r_ship_to_planet) < planet.radius:
        print("Oh no, you crashed into the planet!")
        break

    trailplanet.append(pos=planet.pos)      # Planet is cyan
    trailship.append(pos=ship.pos)          # Spaceship is magenta
    
    t = t+deltat

print("---")
print("Calculations finished after ",t/60,"minutes")
print("The ship is now", mag(ship.pos)-bh.radius, "m away from the event horizon of the black hole")
print("All done!")
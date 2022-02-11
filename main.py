from classes.waterlevel import Tank, bcolors
import os


run = True

tank = Tank(50, 20)


def level_contorlling():

    global run
    
    # Clearing the Screen
    
    print("\n[===========================================| Automatic Water Level Control |===========================================]")
    p= 0.2 * tank.maxcap
    if(tank.capacity > p):
        tank.decrease_capacity()
    else:
        print("\n[===========================================| The Tank Capcity is Low ... |===========================================]\n")
        user_input = input("Do you want to turn on the Water Pump  [y/n]: ")
        if(user_input == "y"):
            while run:
                tank.increase_capacity()
                if(tank.capacity >= tank.maxcap):
                    print("\n[===========================================| The tank is full, The water pump has been switched off automatically. |=============================]\n")
                    run= False
            

while run:
    level_contorlling()

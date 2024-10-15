#!/usr/bin/env python3
import sys
name = "Isobel"
fav_color = "Blue"
fav_activity = "Baking"
fav_animal = "Sea Otter (Enhydra lutris)"
new_line = "\n"
print("My name: Isobel")
print("My favorite color:", fav_color)
print("My favorite activity:", fav_activity)
print("My favorite animal:", fav_animal)
print("My name is", name, ", my favorite color is", fav_color,", my favorite activity is", fav_activity, ", and my favorite animal is", fav_animal)
print(f"My name is {name}, my favorite color is {fav_color}, my favorite activity is {fav_activity},{new_line}and my favorite animal is {fav_animal}.")
name_sys = sys.argv[1]
color_sys = sys.argv[2]
activity_sys = sys.argv[3]
animal_sys = sys.argv[4]
print(name_sys,color_sys,activity_sys,animal_sys)
print(name_sys+color_sys+activity_sys+animal_sys)
print(f"My name: {name_sys} {new_line}My favorite color: {color_sys} {new_line}My favorite activity: {activity_sys} {new_line}My favorite animal: {animal_sys}")

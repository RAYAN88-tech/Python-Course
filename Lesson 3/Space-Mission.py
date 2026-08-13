# ====================================
# MY SPACE MISSION REPORTER
# File: my-space-mission-reporter.py
# ====================================


# PART 1 - USER INPUT
planet = input("Enter the planet you are visiting:")
distance = float(input("Enter the distance from Earth in million km:"))


# PART 2 - if STATEMENT
if distance > 100:
    print("Warning: This is a very far planet!")

# PART 3 - if - else
if distance < 50:
    print("This planet is quite close to Earth!")
else:
    print("Prepare for a long space journey!")


# PART 4 - if-elif-else
if distance < 20:
    print("Mission: Short Space Trip")
elif distance < 50:
    print("Mission: Medium Space Trip")
elif distance < 100:
    print("Mission: Long Space Trip")
else:
    print("Mission: Extreme Space Adventure")


# PART 5 -datetime MODULE
import datetime
import calendar

now = datetime.datetime.now()

print("Planet:", planet)
print("Mission Start Time:", now)

print(calendar.calendar(now.year))
...
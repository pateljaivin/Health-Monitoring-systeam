from pygame import mixer
from datetime import datetime
from time import time


def playsound(filename):
    mixer.init()
    mixer.music.load(f"{filename}.mp3")
    mixer.music.play()
    while True:
        a = input("Enter the 'stop' to stop the aleram::")
        if (a == 'stop'):
            mixer.music.stop()
        break


def logfile(msg):
    with open('logfile.txt', 'a') as a:
        a.write(f"\n{msg}  + {datetime.now()}")


water_time = time()
eye_time = time()
exercise_time = time()

# set all time in second
watertime = 2000  # every 1800 second it can give reminder
eyetime = 2400  # every 2400 second it can give reminder
exercisetime = 3600  # every 3600 second it can give reminder

while(True):
    if(time() - water_time) > watertime:
        print("Plese Drink the water::")
        playsound("Water")
        logfile("WATER")
        water_time = time()

    elif(time() - eye_time) > eyetime:
        print("Plese do eye exercise::")
        playsound("Eye")
        logfile("EYE EXCERCISE")
        eye_time = time()

    elif(time() - exercise_time) > exercisetime:
        print("Plese do the physical exercise::")
        playsound("Exercise")
        logfile("PHYSICAL EXCERCISE")
        excrcise_time = time()

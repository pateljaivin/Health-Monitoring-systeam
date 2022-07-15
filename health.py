def getdate():
    import datetime
    return str(datetime.datetime.now())


def entry(name):
    e = int(input(''' enter  the  1 - Excercise 2 - Diet ::::'''))
    if (e == 1):
        execerise = input("enter the execercise::::")
        with open(f"{name}e.txt", 'a') as a:
            a.write(getdate() + " " + execerise)
            print("Succesfully added")
    elif (e == 2):
        food = input("enter the food eat::::")
        with open(f"{name}f.txt", 'a') as a:
            a.write(getdate() + " " + food)
            print("Sucessfully added")
    else:
        print("INVALID")


def retrive(name):
    e = int(input(''' enter  the 1 - Excercise 2 - Diet::::'''))
    if (e == 1):
        with open(f"{name}e.txt", 'r') as a:
            b = a.read()
            print(b)
    elif (e == 2):
        with open(f"{name}f.txt", 'r') as a:
            b = a.read()
            print(b)
    else:
        print("INVALID")


name = input("enter your username::")
wish = int(input("enter1/2    1 - entry 2 - retrive:::"))

if(wish == 1):
    entry(name)
elif(wish == 2):
    retrive(name)
else:
    print("INVALID")

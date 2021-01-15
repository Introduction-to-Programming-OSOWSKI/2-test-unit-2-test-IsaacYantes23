def waterState(f):
    if f <= 32:
        return "solid"
    elif f >= 212:
        return "gas"
    else:
        return "liquid"
print(waterState(100))

def isDozen(d):
    if d % 12 == 0:
        return True
    else:
        return False
print(isDozen(36))

def toGerman(w):
    if w == "yes":
        return "ja"
    else:
        return "nein"
print(toGerman("no"))

def stopLight(c):
    if c == "green":
        return "go"
    elif c == "yellow":
        return "slow"
    else:
        return "stop"
print(stopLight("yellow"))

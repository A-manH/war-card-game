import time

def slowprint(string, speed=0.02):
    for i in string:
        print(i, end="")
        time.sleep(speed)

        if i == " ":
            time.sleep(.53)
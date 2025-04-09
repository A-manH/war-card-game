import time

def slowprint(string, letter_speed=0.02, space_speed=0.1, end=""):
    string = str(string)
    for i in string:
        print(i, end=end)
        time.sleep(letter_speed)

        if i == " ":
            time.sleep(space_speed)
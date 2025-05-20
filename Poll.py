import random

def coinflip():
    
    result = random.randint(0, 1)
    
    if result == 0:
        print("Pile")
    elif result == 1:
        print("Face")
    else:
        print("[ERROR] An issue happened during the poll.")

def dice():

    result = random.randint(1, 6)

    if result in range(1, 7):
        print(result)
    else:
        print("[ERROR] An issue happened during the poll.")

def poll():
    return 0
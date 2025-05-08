import datetime

# Late from France
CAL = -9
QC = -6
NY = -6

# In advance from France
REU = 3
CN = 6
JP = 7
AUS = 8

# Clock
def timeClock(in_zone):
  
  print((int(datetime.datetime.now().strftime("%H")) + in_zone) % 24, end="")
  print(datetime.datetime.now().strftime(":%M:%S"), end=" ")
  
  if in_zone != 0:
    print("+" if in_zone > 0 else "-")
  elif in_zone == 0:
    print("=")
  else :
    print("[ERROR] Not a TimeZone.")

# Delta
def timeDiff(in_zone):
  return in_zone
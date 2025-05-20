import datetime

# Late from France
CAL = cal = Cal = California = -9
QC = Quebec = qc = -6
NY = NewYork = ny = nyc = -6

# In advance from France
REU = reunion = Reunion = 3
CN = Chine = chine = China = china = 6
JP = Japan = japan = Japon = japon = 7
AUS = aus = Australia = australia = 8

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

def age(in_year, in_month = 1, in_day = 1):
  
  local_today = datetime.datetime.today()
  
  return local_today.year - in_year - ((local_today.month, local_today.day) < (in_month, in_day))
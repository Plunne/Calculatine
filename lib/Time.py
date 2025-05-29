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

# Time
def time(in_zone = 0):
  """
  Display time of the country/city/state/region and the delta from France.

  List of Countries/Cities/States/Regions availables :

  [Africa]
  - REU, reunion, Reunion

  [America]
  - CAL,cal,Cal,California
  - QC, Quebec, qc
  - NY, NewYork, ny, nyc

  [Asia]
  - CN, Chine, chine, China, china
  - JP, Japan, japan, Japon, japon

  [Oceanie]
  - AUS, aus, Australia, australia
  """

  print((int(datetime.datetime.now().strftime("%H")) + in_zone) % 24, end="")
  print(datetime.datetime.now().strftime(":%M:%S"), end=" ")
  
  if (in_zone == 0):
    print("(=)")
  elif in_zone != 0:
    print("(+" if in_zone > 0 else "(", end="")
    print(f"{in_zone}h)")
  else :
    print("[ERROR] Not a TimeZone.")

# Age
def age(in_year, in_month = 1, in_day = 1):
  """
  Find the age of a person by birth date.

  age(YYYY, MM, DD)

  - Year : mandatory
  - Month : optional
  - Day : optional
  """
  
  local_today = datetime.datetime.today()
  
  return local_today.year - in_year - ((local_today.month, local_today.day) < (in_month, in_day))

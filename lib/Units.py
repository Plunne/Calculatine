# Weight
kg = Kg = 1
lbs = Lbs = 2.20462

# Weight
def toLbs(in_weight):
  return in_weight * lbs

fromKg = fromkg = tolbs = toLbs

def fromLbs(in_weight):
  return in_weight / lbs

toKg = tokg = fromlbs = fromLbs

# Pressure
Bar = 1
Psi = 14.5038
Pa = 100000

# Pressure
def toPsi(in_pressure):
  return in_pressure * Psi

topsi = toPsi

def fromPsi(in_pressure):
  return in_pressure / Psi

frompsi = fromPsi

def toPa(in_pressure):
  return in_pressure * Pa

topa = toPa

def fromPa(in_pressure):
  return in_pressure / Pa

frompa = fromPa

def pressure(in_fromPressure, in_value, in_toPressure):
  return (in_value / in_fromPressure) * in_toPressure

# Speed
kph = Kph = kmh = Kmh = 1
mph = Mph = 0.621371
kn = Kn = 1852

def toMph(in_speed):
  return in_speed * mph

fromKph = fromkph = fromKmh = fromkmh = tomph = toMph

def fromMph(in_speed):
  return in_speed / mph

toKph = tokph = toKmh = tokmh = frommph = fromMph

def toKn(in_speed):
  return in_speed * kn

tokn = toKn

def fromKn(in_speed):
  return in_speed / kn

fromkn = fromKn

def speed(in_fromSpeed, in_value, in_toSpeed):
  return (in_value / in_fromSpeed) * in_toSpeed

# Fuel
L100km = 1
mpg = Mpg = 235.21

def toMpg(in_fuel):
  return in_fuel * mpg

fromLkm = fromlkm = tompg = toMpg

def fromMpg(in_fuel):
  return in_fuel / mpg

toLkm = tolkm = frommpg = fromMpg

# Temperature
C = Cel = Celsius = 1
K = Kel = Kelvin = -273.15
F = Far = Fareneight = -459.67

def toK(in_temperature):
  return in_temperature * Kel

toKelvin = toKel = tokel = toK

def fromK(in_temperature):
  return in_temperature / Kel

fromKelvin = fromKel = fromkel = fromK

def toF(in_temperature):
  return in_temperature * Far

toFareneight = toFar = tofar = toF

def fromF(in_temperature):
  return in_temperature / Far

fromFareneight = fromFar = fromfar = fromF

def temp(in_fromTemperature, in_value, in_toTemperature):
  return (in_value / in_fromTemperature) * in_toTemperature

# Power
HP = hp = 1
KW = kW = kw = 0.7457

def toKW(in_power):
  return in_power * KW

fromHP = fromHp = fromhp = tokw = toKW

def fromKW(in_power):
  return in_power / KW

toHP = toHp = tohp = fromkw = fromKW

# Force
kgf = Kgf = 1
Nmm = 9.0665

def toNmm(in_force):
  return in_force * Nmm

fromKgF = fromKgf = fromkgf = tonmm = toNmm

def fromNmm(in_force):
  return in_force / Nmm

toKgF = toKgf = tokgf = fromnmm = fromNmm
##################
#     Weight     #
##################

kg = Kg = 1
lbs = Lbs = 2.20462

def toLbs(in_weight = 1):
  """
  [kg -> Lbs]

  Aliases : fromKg, fromkg, tolbs
  """
  return in_weight * lbs

fromKg = fromkg = tolbs = toLbs

def fromLbs(in_weight = 1):
  """
  [Lbs -> kg]

  Aliases : toKg, tokg, fromlbs
  """
  return in_weight / lbs

toKg = tokg = fromlbs = fromLbs

####################
#     Pressure     #
####################

Bar = 1
Psi = 14.5038
Pa = 100000

def pressure(in_fromPressure, in_value, in_toPressure):
  """
  Convert a pressure value into another pressure unit.

  pressure(in_fromPressure, in_value, in_toPressure)

  - in_fromPressure : Unit to convert
  - in_value : Value to convert
  - in_toPressure : Result unit

  List of pressure units availables :

  - Bar
  - Pa
  - Psi
  """
  return (in_value / in_fromPressure) * in_toPressure

def toPa(in_pressure = 1):
  """
  [Bar -> Pascal]

  Aliases : toPascal, topascal, topa
  """
  return in_pressure * Pa

toPascal = topascal = topa = toPa

def fromPa(in_pressure = 1):
  """
  [Pascal -> Bar]

  Aliases : fromPascal, frompascal, frompa
  """
  return in_pressure / Pa

fromPascal = frompascal = frompa = fromPa

def toPsi(in_pressure = 1):
  """
  [Bar -> Psi]

  Alias : topsi
  """
  return in_pressure * Psi

topsi = toPsi

def fromPsi(in_pressure = 1):
  """
  [Psi -> Bar]

  Alias : frompsi
  """
  return in_pressure / Psi

frompsi = fromPsi

#################
#     Speed     #
#################

kph = Kph = kmh = Kmh = 1
mph = Mph = 0.621371
kn = Kn = 1852

def speed(in_fromSpeed, in_value, in_toSpeed):
  """
  Convert a speed value into another speed unit.

  speed(in_fromSpeed, in_value, in_toSpeed)

  - in_fromSpeed : Unit to convert
  - in_value : Value to convert
  - in_toSpeed : Result unit

  List of speed units availables :

  - kph, Kph, kmh, Kmh
  - mph, Mph
  - kn, Kn
  """
  return (in_value / in_fromSpeed) * in_toSpeed

def toKn(in_speed = 1):
  """
  [km/h -> Knots]

  Alias : tokn
  """
  return in_speed * kn

tokn = toKn

def fromKn(in_speed = 1):
  """
  [Knots -> km/h]

  Alias : fromkn
  """
  return in_speed / kn

fromkn = fromKn

def toMph(in_speed = 1):
  """
  [km/h -> mph]

  Aliases : fromKph, fromkph, fromKmh, fromkmh, tomph
  """
  return in_speed * mph

fromKph = fromkph = fromKmh = fromkmh = tomph = toMph

def fromMph(in_speed = 1):
  """
  [mph -> km/h]

  Aliases : toKph, tokph, toKmh, tokmh, frommph
  """
  return in_speed / mph

toKph = tokph = toKmh = tokmh = frommph = fromMph

################
#     Fuel     #
################

L100km = 1
mpg = Mpg = 235.21

def toMpg(in_fuel = 1):
  """
  [L/100km -> mpg]

  Aliases : fromLkm, fromlkm, tompg
  """
  return in_fuel * mpg

fromLkm = fromlkm = tompg = toMpg

def fromMpg(in_fuel = 1):
  """
  [mpg -> L/100km]

  Aliases : toLkm, tolkm, frommpg
  """
  return in_fuel / mpg

toLkm = tolkm = frommpg = fromMpg

#######################
#     Temperature     #
#######################

C = Cel = Celsius = 1
K = Kel = Kelvin = -273.15
F = Far = Fareneight = -459.67

def temp(in_fromTemperature, in_value, in_toTemperature):
  """
  Convert a temperature value into another temperature unit.

  temp(in_fromTemperature, in_value, in_toTemperature)

  - in_fromTemperature : Unit to convert
  - in_value : Value to convert
  - in_toTemperature : Result unit

  List of temperature units availables :

  - C, Cel, Celsius
  - K, Kel, Kelvin
  - F, Far, Fareneight
  """
  return (in_value / in_fromTemperature) * in_toTemperature

def toF(in_temperature = 1):
  """
  [Celsius -> Fareneight]

  Aliases : toFareneight, toFar, tofar, tof
  """
  return in_temperature * Far

toFareneight = toFar = tofar = tof = toF

def fromF(in_temperature = 1):
  """
  [Fareneight -> Celsius]

  Aliases : fromFareneight, fromFar, fromfar, fromf
  """
  return in_temperature / Far

fromFareneight = fromFar = fromfar = fromf = fromF

def toK(in_temperature = 1):
  """
  [Celsius -> Kelvin]

  Aliases : toKelvin, toKel, tokel, tok
  """
  return in_temperature * Kel

toKelvin = toKel = tokel = tok = toK

def fromK(in_temperature = 1):
  """
  [Kelvin -> Celsius]

  Aliases : fromKelvin, fromKel, fromkel, fromk
  """
  return in_temperature / Kel

fromKelvin = fromKel = fromkel = fromk = fromK

#################
#     Power     #
#################

HP = hp = 1
KW = kW = kw = 0.7457

def toKW(in_power = 1):
  """
  [HP -> kW]

  Aliases : fromHP, fromHp, fromhp, tokw
  """
  return in_power * KW

fromHP = fromHp = fromhp = tokw = toKW

def fromKW(in_power = 1):
  """
  [kW -> HP]

  Aliases : toHP, toHp, tohp, fromkw
  """
  return in_power / KW

toHP = toHp = tohp = fromkw = fromKW

#################
#     Force     #
#################

kgf = Kgf = 1
Nmm = 9.0665

def toNmm(in_force = 1):
  """
  [kg/F -> N/mm]

  Aliases : fromKgF, fromKgf, fromkgf, tonmm
  """
  return in_force * Nmm

fromKgF = fromKgf = fromkgf = tonmm = toNmm

def fromNmm(in_force = 1):
  """
  [N/mm -> kg/F]

  Aliases : toKgF, toKgf, tokgf, fromnmm
  """
  return in_force / Nmm

toKgF = toKgf = tokgf = fromnmm = fromNmm

EUR = 1.00
USD = 1.13
CAD = 1.57
GBP = 0.85
CHF = 0.93
JPY = 163.61

def money(in_fromMoney, in_value, in_toMoney):
  """
  Convert a money value into another currency.

  money(in_fromMoney, in_value, in_toMoney)

  - in_fromMoney : Currency to convert
  - in_value : Value to convert
  - in_toMoney : Result currency

  List of currencies availables :

  - EUR
  - USD
  - CAD
  - GBP
  - CHF
  - JPY
  """
  return (in_value / in_fromMoney) * in_toMoney

# USD
def toUSD(in_value = 1):
  """
  [EUR -> USD]

  Alias : tousd
  """
  return in_value * USD

tousd = toUSD

def fromUSD(in_value = 1):
  """
  [USD -> EUR]

  Alias : fromusd
  """
  return in_value / USD

fromusd = fromUSD

# CAD
def toCAD(in_value = 1):
  """
  [EUR -> CAD]

  Alias : tocad
  """
  return in_value * CAD

tocad = toCAD

def fromCAD(in_value = 1):
  """
  [CAD -> EUR]

  Alias : fromcad
  """
  return in_value / CAD

fromcad = fromCAD

# GBP  
def toGBP(in_value = 1):
  """
  [EUR -> GBP]

  Alias : togbp
  """
  return in_value * GBP

togpb = toGBP

def fromGBP(in_value = 1):
  """
  [GBP -> EUR]

  Alias : fromgbp
  """
  return in_value / GBP

fromgpb = fromGBP

# CHF
def toCHF(in_value = 1):
  """
  [EUR -> CHF]

  Alias : tochf
  """
  return in_value * CHF

tochf = toCHF

def fromCHF(in_value = 1):
  """
  [CHF -> EUR]

  Alias : fromchf
  """
  return in_value / CHF

fromchf = fromCHF

# JPY
def toJPY(in_value = 1):
  """
  [EUR -> JPY]

  Alias : tojpy
  """
  return in_value * JPY

tojpy = toJPY

def fromJPY(in_value = 1):
  """
  [JPY -> EUR]

  Alias : fromjpy
  """
  return in_value / JPY

fromjpy = fromJPY

EUR = 1.00
USD = 1.13
CAD = 1.57
GBP = 0.85
CHF = 0.93
JPY = 163.61

def money(in_fromMoney, in_value, in_toMoney):
  return (in_value / in_fromMoney) * in_toMoney

# USD
def toUSD(in_value):
  return in_value * USD

tousd = toUSD

def fromUSD(in_value):
  return in_value / USD

fromusd = fromUSD

# CAD
def toCAD(in_value):
  return in_value * CAD

tocad = toCAD

def fromCAD(in_value):
  return in_value / CAD

fromcad = fromCAD

# GBP  
def toGBP(in_value):
  return in_value * GBP

togpb = toGBP

def fromGBP(in_value):
  return in_value / GBP

fromgpb = fromGBP

# CHF
def toCHF(in_value):
  return in_value * CHF

tochf = toCHF

def fromCHF(in_value):
  return in_value / CHF

fromchf = fromCHF

# JPY
def toJPY(in_value):
  return in_value * JPY

tojpy = toJPY

def fromJPY(in_value):
  return in_value / JPY

fromjpy = fromJPY
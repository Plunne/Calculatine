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

def fromUSD(in_value):
  return in_value / USD

# CAD
def toCAD(in_value):
  return in_value * CAD

def fromCAD(in_value):
  return in_value / CAD

# GBP  
def toGBP(in_value):
  return in_value * GBP

def fromGBP(in_value):
  return in_value / GBP

# CHF
def toCHF(in_value):
  return in_value * CHF

def fromCHF(in_value):
  return in_value / CHF

# JPY
def toJPY(in_value):
  return in_value * JPY

def fromJPY(in_value):
  return in_value / JPY

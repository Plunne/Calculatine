# Gears.py

default_gear = 3
default_value = 1.00
default_lenght = 0.20
default_gears = {
  1 : 2.20,
  2 : 1.40,
  3 : 1.00,
  4 : 0.80,
  5 : 0.70,
  6 : 0.65
}

class Gears:

  def __init__(self):

    self.master_gear = default_gear
    self.master_value = default_value
    self.master_lenght = default_lenght
    self.gears = default_gears

  #################
  #     Gears     #
  #################
  
  def set_gears(self):

    self.gears[self.master_gear] = self.master_value

    if self.master_gear == 3:

      # 2nd to 1st
      self.gears[2] = self.gears[self.master_gear] + (self.master_lenght * 2)
      self.gears[1] = self.gears[self.master_gear - 1] + (self.master_lenght * 4)
      
      # 4th to 6th
      self.gears[4] = self.gears[self.master_gear] - self.master_lenght
      self.gears[5] = self.gears[self.master_gear + 1] - (self.master_lenght / 2)
      self.gears[6] = self.gears[self.master_gear + 2] - (self.master_lenght / 4)

    elif self.master_gear == 4:
      
      # 3rd to 1st
      self.gears[3] = self.gears[self.master_gear] + (self.master_lenght * 2)
      self.gears[2] = self.gears[self.master_gear - 1] + (self.master_lenght * 4)
      self.gears[1] = self.gears[self.master_gear - 2] + (self.master_lenght * 8)
      
      # 5th to 6th
      self.gears[5] = self.gears[self.master_gear] - self.master_lenght
      self.gears[6] = self.gears[self.master_gear + 1] - (self.master_lenght / 2)
    
    else:
      print("[Error] Please use 3rd or 4th gear as master.")
  
  def get_gears(self):
    return self.gears
  
  ##################
  #     Master     #
  ##################

  # master_gear
  def set_master_gear(self, in_gear):
    
    if in_gear in [3, 4]:
      self.master_gear = in_gear
      self.set_gears()
    else:
      print("[Error] Please use 3rd or 4th gear as master.")

  def get_master_gear(self):
    return self.master_gear

  # master_value
  def set_master_value(self, in_value):
    self.master_value = in_value
    self.set_gears()

  def get_master_value(self):
    return self.master_value

  # master_lenght
  def set_master_lenght(self, in_lenght):
    self.master_lenght = in_lenght
    self.set_gears()

  def get_master_lenght(self):
    return self.master_lenght
  
  #################
  #     Reset     #
  #################

  def reset_setup(self):

    self.set_master_gear(default_gear)
    self.set_master_value(default_value)
    self.set_master_lenght(default_lenght)
    
    print(self.gears)

  ################
  #     Full     #
  ################

  def full_setup(self, in_gear, in_value, in_length):

    if in_gear in [3, 4]:
      
      self.set_master_gear(in_gear)
      self.set_master_value(in_value)
      self.set_master_lenght(in_length)
      
      print(self.gears)
    
    else:
      print("[Error] Please use 3rd or 4th gear as master.")

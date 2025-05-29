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
    """
    Class for Forza Horizon gearbox setups for drifting.

    An object is already instanciated at the start of Calculatine as "gbox".

    So you can use gbox.<Gears_method>() to work with directly.
    """

    self.master_gear = default_gear
    self.master_value = default_value
    self.master_lenght = default_lenght
    self.gears = default_gears

  #################
  #     Gears     #
  #################
  
  def set_gears(self):
    """
    Update gearbox.
    """

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
    """
    Get gears ratios.
    """
    return self.gears
  
  ##################
  #     Master     #
  ##################

  # master_gear
  def set_master_gear(self, in_gear):
    """
    Set the master gear.

    [3 or 4]
    """
    
    if in_gear in [3, 4]:
      self.master_gear = in_gear
      self.set_gears()
    else:
      print("[Error] Please use 3rd or 4th gear as master.")

  def get_master_gear(self):
    """
    Get the master gear.
    """
    return self.master_gear

  # master_value
  def set_master_value(self, in_value):
    """
    Set the master gear ratio.
    """
    self.master_value = in_value
    self.set_gears()

  def get_master_value(self):
    """
    Get the master gear ratio.
    """
    return self.master_value

  # master_lenght
  def set_master_lenght(self, in_lenght):
    """
    Set the gap between the master gear and the master gear +1
    """
    self.master_lenght = in_lenght
    self.set_gears()

  def get_master_lenght(self):
    """
    Get the gap between the master gear and the master gear +1
    """
    return self.master_lenght
  
  #################
  #     Reset     #
  #################

  def reset_setup(self):
    """
    Reset the gearbox to default values.
    """
    self.set_master_gear(default_gear)
    self.set_master_value(default_value)
    self.set_master_lenght(default_lenght)
    
    print(self.gears)

  ################
  #     Full     #
  ################

  def full_setup(self, in_gear, in_value, in_length):
    """
    Recalculate an entire gearbox.

    - in_gear : Select the master gear (3 or 4)
    - in_ value : Master gear ratio
    - in_lenght : Gap between master gear and master gear +1
    """

    if in_gear in [3, 4]:
      
      self.set_master_gear(in_gear)
      self.set_master_value(in_value)
      self.set_master_lenght(in_length)
      
      print(self.gears)
    
    else:
      print("[Error] Please use 3rd or 4th gear as master.")

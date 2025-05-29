from .Time import *
from .Units import *
from .Money import *
from .Roll import *
from .Gears import *

class Help:

    def __init__(self):
        print("Use h.<module_name>() for more informations")
        print("List of modules : gears, money, roll, time, units")

    def display(self, in_module_name, in_function_list):

        print(f"\n***** HELP {in_module_name} *****\n")

        for i in in_function_list:
            print(i.__name__ + "()")
            print(i.__doc__)

    def gears(self):

        # Gears functions
        local_gears_functions = [
            Gears.__init__,
            Gears.set_gears,
            Gears.get_gears,
            Gears.set_master_gear,
            Gears.get_master_gear,
            Gears.set_master_value,
            Gears.get_master_value,
            Gears.set_master_lenght,
            Gears.get_master_lenght,
            Gears.reset_setup,
            Gears.full_setup
        ]

        # Display gears documentation
        self.display("GEARS", local_gears_functions)

    def money(self):

        # Money functions
        local_money_functions = [
            money,
            toUSD, fromUSD,
            toCAD, fromCAD,
            toGBP, fromGBP,
            toCHF, fromCHF,
            toJPY, fromJPY
        ]

        # Display money documentation
        self.display("MONEY", local_money_functions)

    def roll(self):

        # Roll functions
        local_roll_functions = [
            coinflip,
            dice,
            roll
        ]

        # Display roll documentation
        self.display("ROLL", local_roll_functions)

    def time(self):

        # Time functions
        local_time_functions = [
            time,
            age
        ]

        # Display time documentation
        self.display("TIME", local_time_functions)

    def units(self):

        # Units functions
        local_units_functions = [
            toLbs, fromLbs,
            pressure,
            toPa, fromPa,
            toPsi, fromPsi,
            speed,
            toMph, fromMph,
            toKn, fromKn,
            toMpg, fromMpg,
            temp,
            toF, fromF,
            toK, fromK,
            toKW, fromKW,
            toNmm, fromNmm
        ]

        # Display units documentation
        self.display("UNITS", local_units_functions)

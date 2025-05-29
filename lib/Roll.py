import random as r
import json
from os.path import dirname, abspath, join

db_roll_file = join(dirname(dirname(abspath(__file__))), join("db", "db_roll.json"))

def coinflip():
    """
    ['Pile' or 'Face']
    """

    result = r.randint(0, 1)
    
    if result == 0:
        return "Pile"
    elif result == 1:
        return "Face"
    else:
        return "[ERROR] An issue happened during the roll."

def dice():
    """
    [1 to 6]
    """

    result = r.randint(1, 6)

    if result in range(1, 7):
        return result
    else:
        return "[ERROR] An issue happened during the roll."

def roll():
    """
    [Customizable]
    - <value> : Add the value to the list to roll
    - <nothing> : Do nothing
    - done : Roll the current list of values
    - spin (Not implemented atm) : Wheelspin the current list of values (this is for funny suspens. Each spin, the result is deleted from the list until there is a winner value)
    - load : Load a preset of values from the json database
    - save : Save the current list of values to the json database
    - delete : Delete a json database preset
    - pop : Remove a value from the list by index
    - rm : Remove a value from the list by value
    - q : Cancel the poll
    """

    print("\n***** CUSTOM ROLL *****\n")
    
    roll_list = []
    
    while 1:

        roll_input = input("-> ")
        
        match roll_input:

            # Finish the roll
            case "done":
                break
            
            # Edit at index
            case "edit":
            
                roll_edit_idx = int(input("edit index : ")) - 1
            
                if roll_edit_idx < len(roll_list):
                    roll_list[roll_edit_idx] = input(f"Change \"{roll_list[roll_edit_idx]}\" to : ")
                else:
                    print("[ERROR] Index sent is greater than the list size.")
            
            # Remove by index + 1
            case "pop":
            
                roll_pop_idx = int(input("pop index : ")) - 1
                
                if roll_pop_idx < len(roll_list):
                    roll_list.pop(roll_pop_idx)
                else:
                    print("[ERROR] Index sent is greater than the list size.")
            
            # Remove by value
            case "rm":
            
                roll_rm_val = input("remove : ")

                if roll_rm_val in roll_list:
                    roll_list.remove(roll_rm_val)
                else:
                    print("[ERROR] Item sent is not in the list.")
            
            # Save to json db
            case "save":

                roll_save_as = input("Save as : ")
                
                with open(db_roll_file, "r+") as roll_save_db:
                    
                    roll_save_tmp = json.load(roll_save_db)
                    roll_save_dict = { roll_save_as : roll_list }
                    roll_save_tmp.update(roll_save_dict)

                    roll_save_db.seek(0)
                    
                    json.dump(roll_save_tmp, roll_save_db, indent = 4)
            
            # Load from json db
            case "load":

                with open(db_roll_file, "r") as roll_load_db:
                    
                    roll_load_tmp = json.load(roll_load_db)
                    print(json.dumps(roll_load_tmp, indent = 4))
                
                roll_load_from = input("Load from : ")

                if roll_load_from in roll_load_tmp:
                    roll_list = roll_load_tmp[roll_load_from]
                # Cancel load
                elif roll_input == "q":
                    print("Load canceled.")
                else:
                    print("[ERROR] This list doesn't exists.")

            # Delete list in json db
            case "delete":
                
                # Get json file content
                with open(db_roll_file, "r") as roll_delete_db:
                    
                    roll_delete_tmp = json.load(roll_delete_db)
                    print(json.dumps(roll_delete_tmp, indent = 4))
                
                # Set json file content
                with open(db_roll_file, "w") as roll_delete_db:

                    roll_delete_list = input("Delete : ")

                    if roll_delete_list in roll_delete_tmp:

                        roll_delete_choice = input(f"Are you sure to delete {roll_delete_list} ? (y/n) : ")

                        if roll_delete_choice == "y":
                            
                            # Delete List
                            print(f"{roll_delete_list} has been deleted.")
                            roll_delete_tmp.pop(roll_delete_list)

                            # Update json file
                            json.dump(roll_delete_tmp, roll_delete_db, indent = 4)

                        else:
                            print("Delete canceled.")
                            continue
                    
                    else:
                        print("[ERROR] This list doesn't exists.")

            
            # Continue the roll if no value
            case "":      
                continue

            # Quit the roll
            case "q":
                return "Roll canceled."
            
            # If value, append to list
            case _:
                roll_list.append(roll_input)
    
    # Display list
    print(f"\n{roll_list}\n")
    
    # Get result from random value
    result = r.randint(0, len(roll_list) - 1)

    return roll_list[result]

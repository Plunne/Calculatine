import random as r
import json

def coinflip():
    
    result = r.randint(0, 1)
    
    if result == 0:
        return "Pile"
    elif result == 1:
        return "Face"
    else:
        return "[ERROR] An issue happened during the poll."

def dice():

    result = r.randint(1, 6)

    if result in range(1, 7):
        return result
    else:
        return "[ERROR] An issue happened during the poll."

def poll():

    print("\n**** Custom Poll ***\n")
    
    poll_list = []
    
    while 1:

        poll_input = input("-> ")
        
        # Finish the poll
        if poll_input == "done":
            break
        
        # Edit at index
        elif poll_input == "edit":
        
            poll_edit_idx = int(input("edit index : ")) - 1
        
            if poll_edit_idx < len(poll_list):
                poll_list[poll_edit_idx] = input(f"Change \"{poll_list[poll_edit_idx]}\" to : ")
            else:
                print("[ERROR] Index sent is greater than the list size.")
        
        # Remove by index + 1
        elif poll_input == "pop":
        
            poll_pop_idx = int(input("pop index : ")) - 1
            
            if poll_pop_idx < len(poll_list):
                poll_list.pop(poll_pop_idx)
            else:
                print("[ERROR] Index sent is greater than the list size.")
        
        # Remove by value
        elif poll_input == "rm":
        
            poll_rm_val = input("remove : ")

            if poll_rm_val in poll_list:
                poll_list.remove(poll_rm_val)
            else:
                print("[ERROR] Item sent is not in the list.")
        
        # Save to json db
        elif poll_input == "save":

            poll_save_as = input("Save as : ")
            
            with open("db_poll.json", "r+") as poll_save_db:
                
                poll_save_tmp = json.load(poll_save_db)
                poll_save_dict = { poll_save_as : poll_list }
                poll_save_tmp.update(poll_save_dict)

                poll_save_db.seek(0)
                
                json.dump(poll_save_tmp, poll_save_db, indent = 4)
        
        # Load from json db
        elif poll_input == "load":

            with open("db_poll.json", "r") as poll_load_db:
                
                poll_load_tmp = json.load(poll_load_db)
                print(json.dumps(poll_load_tmp, indent = 4))
            
            poll_load_from = input("Load from : ")

            if poll_load_from in poll_load_tmp:
                poll_list = poll_load_tmp[poll_load_from]
            # Cancel load
            elif poll_input == "q":
                print("Load canceled.")
            else:
                print("[ERROR] This list doesn't exists.")

        # Delete list in json db
        elif poll_input == "delete":
            
            # Get json file content
            with open("db_poll.json", "r") as poll_delete_db:
                
                poll_delete_tmp = json.load(poll_delete_db)
                print(json.dumps(poll_delete_tmp, indent = 4))
            
            # Set json file content
            with open("db_poll.json", "w") as poll_delete_db:

                poll_delete_list = input("Delete : ")

                if poll_delete_list in poll_delete_tmp:

                    poll_delete_choice = input(f"Are you sure to delete {poll_delete_list} ? (y/n) : ")

                    if poll_delete_choice == "y":
                        
                        # Delete List
                        print(f"{poll_delete_list} has been deleted.")
                        poll_delete_tmp.pop(poll_delete_list)

                        # Update json file
                        json.dump(poll_delete_tmp, poll_delete_db, indent = 4)

                    else:
                        print("Delete canceled.")
                        continue
                
                else:
                    print("[ERROR] This list doesn't exists.")

        
        # Continue the poll if no value
        elif poll_input == "":      
            continue

        # Quit the poll
        elif poll_input == "q":
            return "Poll canceled."
        
        # If value, append to list
        else:
            poll_list.append(poll_input)
    
    # Display list
    print(f"\n{poll_list}\n")
    
    # Get result from random value
    result = r.randint(0, len(poll_list) - 1)

    return poll_list[result]

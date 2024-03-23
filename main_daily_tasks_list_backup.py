
from datetime import datetime
import io
import os


def greet():

    c_time = int(datetime.strftime(datetime.now(), "%H"))
    print(c_time)

    if c_time < 12 and c_time >= 4:
        print("Good Morning!")
    elif c_time == 12:
        print("Good day!")
    elif c_time <= 17 and c_time > 12:
        print("Good Afternoon!")
    else:
        print("Good Evening!")


def main():
    day_for_log = datetime.now().strftime("%m_%d_%Y")
    
    file_name = f"daily_tasks_list_{day_for_log}.txt"
    file_dir = os.path.join(os.path.expanduser("~") , "OneDrive", "Desktop", "Messing Around", "Python", "Daily tasks tracker")
    complete_path = os.path.join(file_dir, file_name)
    print(complete_path)

    greet()

    options1 = ["1","2","new","existing"]

    u_choice = input("Do you want to create a new list or continue with an existing one? (1/2): ")

    while not u_choice in options1:
        print("Enter a valid input.")
        u_choice = input("Do you want to create a new list or continue with an existing one? (1/2): ")

    if u_choice == "1" or u_choice == "new":

        if os.path.exists(complete_path):
            options2 = ["1", "2", "continue", "no"]
            u_choice = input("You already have a log from today, would you like to continue with this one or no. (1/2): ")

            while not u_choice in options2:
                print("Please enter a valid input.")
                u_choice = input("You already have a log from today, would you like to continue with this one or no. (1/2): ")

            if u_choice == "1" or u_choice == "continue":
                with io.open(complete_path, "a") as file:
                    file.write("Testing3")

            else:
                os.remove(complete_path)
                with io.open(complete_path, "a") as file:
                    file.write("Testing2")
        elif len(os.listdir(file_dir)) > 1:
            print("There are old logs in the current directory.")
            options3 = ["1", "2", "3", "4", "5"]
            while True:
                u_choice = input("1 - View them | 2 - Delete one | 3 - Delete all | 4 - Make a new task list | 5 - Exit : ")

                while not u_choice in options3:
                    print("Please enter a valid input.")
                    u_choice = input("1 - View them | 2 - Delete one | 3 - Delete all | 4 - Make a new task list | 5 - Exit : ")

                if u_choice == "1":
                    for file in os.listdir(file_dir):
                        if file == "main.py":
                            continue
                        print(file)
                elif u_choice == "2":
                    delete_file = input("Please enter the name of the file you want to delete: ")
                    while not delete_file in os.listdir(file_dir):
                        print("Please enter a valid input.")
                        delete_file = input("Please enter the name of the file you want to delete: ")
                    os.remove(os.path.join(file_dir, delete_file))
                
                elif u_choice == "3":
                    for file in os.listdir(file_dir):
                        if file == "main.py":
                            continue
                        os.remove(file_dir, file)

        else:
            with io.open(complete_path, "a") as file:
                file.write("Testing1")

    else:
        if os.path.exists(complete_path):
            with io.open(complete_path, "a") as file:
                file.write("Testing4")
main()
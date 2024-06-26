
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


def write_to_file(file_path, task_list):

    with open(file_path, "w+") as file:
        for task in task_list:
            file.write(f"{task}\n")
        file.close()

def append_to_file(file_path, task_list):

    with open(file_path, "r+") as file:
        file.seek(0, 2)
        for task in task_list:
            file.write(f"{task}\n")
        file.close()




def read_print_checkoff_file(file_path):
    with open(file_path, "r") as file:

        lines = list(map(lambda line: line.strip(), file.readlines()))
            
        print(f"Number of tasks: {len(lines)}")

        print(*lines, sep="\n")
        
        file.close()

    while True:
        print("To stop checking off tasks, type 'stop'")
        task = input("Please enter the name of the task you would like to check off: ")

        if task == "stop":
            break

        while not task in lines:
            print("Please input a valid task")
            task = input("Please enter the name of the task you would like to check off: ")
            if task == "stop":
                break

        if task == "stop":
            break

        lines.remove(task)

        write_to_file(file_path, lines)
            
        print("Updated version:\n")
        print(f"Number of tasks: {len(lines)}")

        print(*lines, sep="\n")

        
    


def main():
    day_for_log = datetime.now().strftime("%m_%d_%Y")
    
    file_name = f"daily_tasks_list_{day_for_log}.txt"
    file_dir = os.getcwd()
    complete_path = os.path.join(file_dir, file_name)

    greet()



    def task_handler(file_path):
        task_list = []
        while True:
            print("To stop adding tasks type 'stop' ")
            task = input("Name the task you would like to add: ")
            if task == "stop":
                break
            task_list.append(task)

        append_to_file(file_path, task_list)
        read_print_checkoff_file(file_path)



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
                    task_handler(complete_path)

            else:
                os.remove(complete_path)
                task_handler(complete_path)


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
                        os.remove(os.path.join(file_dir, file))

                elif u_choice == "4":
                    task_handler(complete_path)

                else:
                    exit()
        else:
            task_handler(complete_path)

    else:
        open_file_date = input("Please enter the date of the file you want to open (xx/xx/xxxx): ").split("/")

        while len(open_file_date) != 3:
            print("Please enter the date correctly.")
            open_file_date = input("Please enter the date of the file you want to open (xx/xx/xxxx): ").split("/")

        open_file_name = f"daily_tasks_list_{open_file_date[0]}_{open_file_date[1]}_{open_file_date[2]}.txt"
        complete_open_file_name = os.path.join(file_dir, open_file_name)

        if os.path.exists(complete_open_file_name):
            task_handler(complete_open_file_name)
main()
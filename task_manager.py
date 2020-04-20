"""
Task Manager Application
"""
# imports
from datetime import date
from datetime import datetime
import os.path

def read_login_file_to_dict():
    # read the login file into a dictionary
    login_file_check = open('user.txt', 'r')
    login_dict = {}
    for line_check in login_file_check:
        split_line_check = line_check.split(',')
        login_dict[split_line_check[0].strip('\n')] = split_line_check[1].strip('\n')
    login_file_check.close()
    return login_dict

# define functions
def reg_user():
    #initialise variable to log if creating a new user
    creating_usr = True
    # loop while creating a new user
    while creating_usr:

        # read the login file into a dictionary
        login_dict = read_login_file_to_dict()
        
        new_usr_name = input("\nPlease enter a new username to create: ")
        # if the username is not in the login_dict dictionary, continue to register
        if (new_usr_name not in login_dict): 
            new_usr_name_cmp = input("Please confirm username: ")
            if new_usr_name == new_usr_name_cmp:
                new_passwd = input("\nPlease enter a password: ")
                new_passwd_cmp = input("Please confirm the password: ")
                # check the passwords match
                if new_passwd == new_passwd_cmp:
                    # open the login file for append
                    login_file = open('user.txt', 'a')
                    # write the user and password to the file
                    login_file.write("\n" + new_usr_name + ", " + new_passwd)
                    login_file.close()
                    creating_usr = False
                    # reset the menu selection variable
                    menu_pick = ""
                else:
                    print("Password does not match")
                    creating_usr = False
                    # reset the menu selection variable
                    menu_pick = ""
            else:
                print("Please ensure the username matches")
                creating_usr = False
                # reset the menu selection variable
                menu_pick = ""
        else:
            # user name not in the login_dict dictionary, report this and try again
            print("User already exisits, please try another username")
    return 0

def add_task():
    tasks_dict = read_tasks_to_dict()
    
    # give the task a new Task ID that isn't in use
    new_task_id = str(len(tasks_dict) + 1)
    # create empty dictionary for new task
    tasks_dict[new_task_id] = {}
    # assign the new Task ID key and value pair 
    tasks_dict[new_task_id]['Task ID'] = new_task_id

    # ask for user inputs and assign to key/value pairs in the dictionary
    tasks_dict[new_task_id]['Assigned User'] = input("\nPlease enter a user to assign the task to: ")
    tasks_dict[new_task_id]['Title'] = input("Title\t\t: ")
    tasks_dict[new_task_id]['Description'] = input("Description\t: ")
    tasks_dict[new_task_id]['Due Date'] = input("Due Date\t: ")
    tasks_dict[new_task_id]['Assigned Date'] = (date.today()).strftime("%d %b %Y")

    # task starts as not complete
    tasks_dict[new_task_id]['Complete'] = 'No'
    
    # commit changes to file 
    tasks_file = open('tasks.txt', 'w')
    for task in tasks_dict:
        tasks_file.write(tasks_dict[task]['Task ID'] + ", "
                         + tasks_dict[task]['Assigned User'] + ", "
                         + tasks_dict[task]['Title'] + ", "
                         + tasks_dict[task]['Description'] + ", "
                         + tasks_dict[task]['Due Date'] + ", "
                         + tasks_dict[task]['Assigned Date'] + ", "
                         + tasks_dict[task]['Complete'] + "\n")
    tasks_file.close()
    return 0

def view_all():
    tasks_dict = read_tasks_to_dict()

    # print ALL the tasks assigned to user as default    
    for task in tasks_dict:
            print("Task ID\t\t: " + tasks_dict[task]['Task ID'])
            print("Assigned User\t: " + tasks_dict[task]['Assigned User'])
            print("Title\t\t: " + tasks_dict[task]['Title'] + "\n")
            print("Description\t: " + tasks_dict[task]['Description'] + "\n")
            print("Due Date\t\t: " + tasks_dict[task]['Due Date'])
            print("Assigned Date\t: " + tasks_dict[task]['Assigned Date'])
            print("Complete\t: " + tasks_dict[task]['Complete'] + "\n")
    return 0

def read_tasks_to_dict():
    # open tasks file and read in contents
    tasks_file = open('tasks.txt', 'r')
    tasks_dump = tasks_file.read().strip('\n')
    tasks_file.close()

    # split the lines into a list
    tasks_lines = tasks_dump.split('\n')

    # create empty dictionary
    tasks_dict = {}

    # assign split lines to dictionary
    for line in tasks_lines:
        tasks_split = line.split(',')
        tasks_dict[tasks_split[0]] = {'Task ID':tasks_split[0].strip(),
                                     'Assigned User':tasks_split[1].strip(),
                                     'Title':tasks_split[2].strip(),
                                     'Description':tasks_split[3].strip(),
                                     'Due Date':tasks_split[4].strip(),
                                     'Assigned Date':tasks_split[5].strip(),
                                     'Complete':tasks_split[6].strip('\n').strip()
                                     }
    return tasks_dict

def view_mine():
    tasks_dict = read_tasks_to_dict()
    selected_task = ""
    # print ALL the tasks assigned to user as default    
    for task in tasks_dict:
        if tasks_dict[task]['Assigned User'].strip() == usr_name:
            print("Task ID\t\t: " + tasks_dict[task]['Task ID'])
            print("Assigned User\t: " + tasks_dict[task]['Assigned User'])
            print("Title\t\t: " + tasks_dict[task]['Title'] + "\n")
            print("Description\t: " + tasks_dict[task]['Description'] + "\n")
            print("Due Date\t\t: " + tasks_dict[task]['Due Date'])
            print("Assigned Date\t: " + tasks_dict[task]['Assigned Date'])
            print("Complete\t: " + tasks_dict[task]['Complete'] + "\n")

    # loop to select particular tasks
    while selected_task != "-1":
        # allow user to select one task
        selected_task = input("Please select a task or enter '-1' to return to main menu: ")
        
        if (selected_task != '-1') and (tasks_dict.get(selected_task) != None):
            print("Task ID\t\t: " + tasks_dict[selected_task]['Task ID'])
            print("Assigned User\t: " + tasks_dict[selected_task]['Assigned User'])
            print("Title\t\t: " + tasks_dict[selected_task]['Title'] + "\n")
            print("Description\t: " + tasks_dict[selected_task]['Description'] + "\n")
            print("Due Date\t\t: " + tasks_dict[selected_task]['Due Date'])
            print("Assigned Date\t: " + tasks_dict[selected_task]['Assigned Date'])
            print("Complete\t: " + tasks_dict[selected_task]['Complete'] + "\n")

            print("Press 'c' to mark the task as complete")
            print("Press 'e' to edit the task")
            usr_input = input()
            # if completed, set to 'Yes'
            if usr_input == 'c':
                tasks_dict[selected_task]['Complete'] = 'Yes'
            # edit the task
            elif (usr_input == 'e') and (tasks_dict[selected_task]['Complete'] != 'Yes'):
                tasks_dict[selected_task]['Assigned User'] = input("\nPlease enter a user to assign the task to: ")
                tasks_dict[selected_task]['Title'] = input("Title\t\t: ")
                tasks_dict[selected_task]['Description'] = input("Description\t: ")
                tasks_dict[selected_task]['Due Date'] = input("Due Date\t: ")
                tasks_dict[selected_task]['Assigned Date'] = (date.today()).strftime("%d %b %Y")
            
    # commit changes to file 
    tasks_file = open('tasks.txt', 'w')
    for task in tasks_dict:
        tasks_file.write(tasks_dict[task]['Task ID'] + ", "
                         + tasks_dict[task]['Assigned User'] + ", "
                         + tasks_dict[task]['Title'] + ", "
                         + tasks_dict[task]['Description'] + ", "
                         + tasks_dict[task]['Due Date'] + ", "
                         + tasks_dict[task]['Assigned Date'] + ", "
                         + tasks_dict[task]['Complete'] + "\n")
    tasks_file.close()
            
    return 0

def view_stats():
    # if the files don't exist then generate the reports
    if (os.path.exists('task_overview.txt') == False) or (os.path.exists('task_overview.txt') == False):
        generate_reports()

    # if the files exist open them 
    task_overview = open('task_overview.txt', 'r')
    user_overview = open('user_overview.txt', 'r')
    task_dump = task_overview.read()
    user_dump = user_overview.read()

    print("Overall Task Status\n")
    print(task_dump)
    print("\nUser Tasks Status\n")
    print(user_dump)
    
    # close the files
    task_overview.close()
    user_overview.close()
    return 0

def generate_reports():
    task_overview = open('task_overview.txt', 'w')
    user_overview = open('user_overview.txt', 'w')

    # read the login file into a dictionary
    login_dict = read_login_file_to_dict()

    # read the tasks file into a dictionary
    tasks_dict = read_tasks_to_dict()

    # initialise variables
    count_complete = 0
    count_uncomplete = 0
    count_uncomplete_overdue = 0
    
    # gather the statistics from the tasks dictionary
    for task in tasks_dict:
        # convert string date back to object
        due_date = datetime.strptime(tasks_dict[task]['Due Date'], "%d %b %Y")
        
        if tasks_dict[task]['Complete'] == 'Yes':
            count_complete += 1
        if tasks_dict[task]['Complete'] == 'No':
            count_uncomplete += 1
        if (tasks_dict[task]['Complete'] == 'No') and (due_date < datetime.now()):
            count_uncomplete_overdue += 1

    percentage_incomplete = round((count_uncomplete / len(tasks_dict)) * 100)
    percentage_overdue = round((count_uncomplete_overdue / len(tasks_dict)) * 100)

    # output the statistics to tasks_overview file
    task_overview.write("Total number of tasks: " + str(len(tasks_dict)) + "\n")    
    task_overview.write("Total number of completed tasks: " + str(count_complete) + "\n") 
    task_overview.write("Total number of incomplete tasks: " + str(count_uncomplete) + "\n")
    task_overview.write("Total number of overdue tasks: " + str(count_uncomplete_overdue) + "\n")
    task_overview.write("Percentage Incomplete: " + str(percentage_incomplete) + "%" + "\n")
    task_overview.write("Percentage Overdue: " + str(percentage_overdue) + "%")

    user_overview.write("Total Number of Registered Users: " + str(len(login_dict)) + "\n")
    user_overview.write("Total number of tasks: " + str(len(tasks_dict)) + "\n\n")
    
    for user in login_dict.keys():
        # initialise variables
        count_user_tasks = 0
        count_user_complete_tasks = 0
        count_user_incomplete_tasks = 0
        count_user_overdue_tasks = 0

        user_percent_total = 0
        user_percent_complete = 0
        user_percent_incomplete = 0
        user_percent_overdue = 0
        
        for task in tasks_dict:
            # get the due date as an object to compare
            due_date = datetime.strptime(tasks_dict[task]['Due Date'], "%d %b %Y")

            if tasks_dict[task]['Assigned User'] == user:
                count_user_tasks += 1
            if (tasks_dict[task]['Assigned User'] == user) and (tasks_dict[task]['Complete'] == 'Yes'):
                count_user_complete_tasks += 1
            if (tasks_dict[task]['Assigned User'] == user) and (tasks_dict[task]['Complete'] == 'No'):
                count_user_incomplete_tasks += 1
            if tasks_dict[task]['Assigned User'] == user and (tasks_dict[task]['Complete'] == 'No') and (due_date < datetime.now()):
                count_user_overdue_tasks += 1
                
        # calc a users stats
        user_percent_total = round((count_user_tasks / len(tasks_dict)) * 100)
        if count_user_tasks != 0:
            user_percent_complete = round((count_user_complete_tasks / count_user_tasks) * 100)
            user_percent_incomplete = round((count_user_incomplete_tasks / count_user_tasks) * 100)
            user_percent_overdue = round((count_user_overdue_tasks / count_user_tasks) * 100)
        
        # write the results to a file
        user_overview.write("Total number of tasks for " + str(user) + ": " + str(count_user_tasks) + "\n") 
        user_overview.write("Percentage of Total tasks for " + str(user) + ": " + str(user_percent_total) + "%\n")
        user_overview.write("Percentage of users tasks complete: " + str(user_percent_complete) + "%\n")
        user_overview.write("Percentage of users tasks incomplete: " + str(user_percent_incomplete) + "%\n")
        user_overview.write("Percentage of users tasks overdue: " + str(user_percent_overdue) + "%\n\n")
    
    # close the files
    task_overview.close()
    user_overview.close()

    print("\nReports Generated Successfully!\n")

    return 0

def print_menu():
    print("\nPlease select one of the following options:")
    print("r \t- register user")
    print("a \t- add task")
    print("va \t- view all tasks")
    print("vm \t- view my tasks")
    # give admin user the stats menu item
    if usr_name == "admin":
        print("gr \t- generate reports")
        print("ds \t- display statistics")
    print("e \t- exit\n")
    return 0

# initialise the tracking variables
logged_in = False
usr_valid = False

while not logged_in:
    # prompt for login
    usr_name = input("Username: ")

    # open the login file
    login_file = open('user.txt', 'r')

    # step through the file to find the user
    for line in login_file:
        usr = line.split(',')
        if usr[0] == usr_name:
            print("Welcome " + str(usr_name) + ".")
            usr_valid = True
            break

    if usr[0] != usr_name:
        print("Please re-enter a valid username: ")

    # do the next bit of the login, i.e. password
    while not logged_in & usr_valid:
        passwd = input("Password: ")
        if usr[1].strip() == passwd:
            print("You are now logged in.")
            logged_in = True
        else:
            print("Please re-enter your password.")
    login_file.close()

# successful login attempt, display menu
while logged_in:

    # call print menu function
    print_menu()

    # wait for an input of the menu item
    menu_pick = input()

    # only admin users are allowed to register users
    if (menu_pick == 'r') and (usr_name == "admin"):
        reg_user()
        
    # all non-admin users cannot register new users
    elif (menu_pick == 'r') and (usr_name != "admin"):
        print("\n!Only admin user allowed to register users!")

    # the add task option
    elif menu_pick == 'a':
        add_task()

    # the view all tasks option
    elif menu_pick == 'va':
        view_all()

    # the view my tasks option
    elif menu_pick == 'vm':
        view_mine()

    # only allow admin users to display the stats
    elif (menu_pick == 'gr') and (usr_name == "admin"):
        generate_reports()

    # only allow admin users to display the stats
    elif (menu_pick == 'ds') and (usr_name == "admin"):
        view_stats()

    # exit menu item
    elif menu_pick == 'e':
        break

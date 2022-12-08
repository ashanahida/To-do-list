from printing_functions import main_menu
from operation_functions import user_input


def main():
    main_menu()
    user_input()


main()


def main_menu():

#main function for TO*DO list

    print("""            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                      TODO LIST
                ---------------------
                1. Add Task
                2. Update Task
                3. Delete Task
                4. Show All Tasks
                5. Save Tasks In File
                6. Search Task
                7. Exit The List
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   
    """)


def quit():
    #when user want to exit this application
    print("Please visit again!")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


from printing_functions import quit, main_menu

todo_list = []

def add_task():
    # adding task to list
    task = input("Enter a new task: ")
    todo_list.append(["", "", "", "", ""])
    todo_list[-1][0] = task
    todo_list[-1][1] = input("Enter a date : ")
    todo_list[-1][2] = input("Enter Start time : ")
    todo_list[-1][3] = input("Enter End time : ")
    todo_list[-1][4] = input("Enter the description: ")
    print("\nTask Added....!")
    main_menu()
    user_input()


def update_task():
    # Updating task in list
    task_or_date = input("Enter a task : ")
    for index, task in enumerate(todo_list):
        if task[0] == task_or_date or task[1] == task_or_date:
            todo_list[index][0] = input("Enter the Updated task : ")
            todo_list[index][1] = input("Enter the Updated date : ")
            todo_list[index][2] = input("Enter the Updated Start time : ")
            todo_list[index][3] = input("Enter the Updated End time : ")
            todo_list[-1][4] = input("Enter the description: ")
            print("\nTask Updated successfully!")
    main_menu()
    user_input()


def delete_task():
    task_to_delete = input("Enter a task : ")
    for index, task in enumerate(todo_list):
        if task[0] == task_to_delete or task[1] == task_to_delete:
            todo_list.pop(index)
            print("Task deleted successfully...!")
    main_menu()
    user_input()


def view_all():
    for item in todo_list:
        task, date, start_time, end_time, des = item
        print("Task", task)
        print("Date:", date)
        print("Start Time:", start_time)
        print("End Time:", end_time)
        print("Description :", des)

    main_menu()
    user_input()


def operation(operation_type, operation_value, operation_list):
    if operation_type == "delete":
        # delete task
        operation_list.pop(operation_value)
    elif operation_type == "view":
        print(operation_list)
    elif operation_type == "save":
        with open("todo.txt", "w") as file:
            for item in operation_list:
                file.write(item + "\n")
    elif operation_type == "search":
        for item in operation_list:
            if operation_value in item:
                print(item)
    elif operation_type == "exit":
        print("Goodbye...!")
    else:
        print("Invalid operation")


def user_input():
    menu = input("Enter your choice: ")
    while menu != "7":
        if menu == "1":
            add_task()
        elif menu == "2":
            update_task()
        elif menu == "3":
            delete_task()
        elif menu == "4":
            view_all()
        elif menu == "5":
            operation("save", None, todo_list)
        elif menu == "6":
            task = input("Enter the task you want to search: ")
            operation("search", task, todo_list)
        else:
            print("Invalid choice")
        menu = input("Enter your choice: ")

    quit()

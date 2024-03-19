#obj
#To-do list application that allows user to add,edit,delete and mark tasks as completed


print('Welcome to your ToDo list, what would you like to do?')
print('1. Add Task \n2. Show Tasks \n3. Edit Task \n4. Delete Task \n5. Mark Task as Completed \n6. Exit')

while True:
    choice = input('Enter your choice: ')

    if choice == '1':
        try:
            with open('mytask.txt', 'a') as file:
                while True:
                    added_task = input('Enter a task or type "done" to finish: ')
                    if added_task.lower() == "done":
                        break
                    file.write(added_task + '\n')
        except FileNotFoundError:
            print('File not found')

    elif choice == '2':
        try:
            with open('mytask.txt', 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print('File not found')

    elif choice == '3':
        try:
            with open('mytask.txt', 'r') as file:
                lines = file.readlines()

            for index, line in enumerate(lines, start=1):
                print(f'{index}: {line.strip()}')
        except FileNotFoundError as e:
            print(f'Error: {e}')

        index_to_edit = int(input('Enter index to edit: '))
        if 1 <= index_to_edit <= len(lines):
            edited_task = input('Enter updated task: ')
            lines[index_to_edit - 1] = f'{edited_task}\n'

            with open('mytask.txt', 'w') as file:
                file.writelines(lines)
            print(f'Index {index_to_edit} has been updated')

    elif choice == '4':
        try:
            with open('mytask.txt', 'r') as file:
                lines = file.readlines()

            for index, line in enumerate(lines, start=1):
                print(f'{index}: {line.strip()}')
        except FileNotFoundError as e:
            print(f'Error: {e}')

        index_to_delete = int(input('Enter index to delete: '))
        if 1 <= index_to_delete <= len(lines):
            removed_task = lines.pop(index_to_delete - 1)

            with open('mytask.txt', 'w') as file:
                file.writelines(lines)
            print(f'Item at index {index_to_delete} has been deleted')

    elif choice == '5':
        try:
            with open('mytask.txt', 'r') as file:
                lines = file.readlines()

            for index, line in enumerate(lines, start=1):
                print(f'{index}: {line.strip()}')
        except FileNotFoundError as e:
            print(f'Error: {e}')

        index_to_mark = int(input('Enter index to mark as completed: '))
        if 1 <= index_to_mark <= len(lines):
            lines[index_to_mark - 1] = lines[index_to_mark - 1].strip() + ' [X]\n'

            with open('mytask.txt', 'w') as file:
                file.writelines(lines)
            print(f'Task at index {index_to_mark} has been marked as completed')

    elif choice == '6':
        exit_task = input('Type "exit" or " " to close your ToDo list: ')
        if exit_task.lower() == "exit" or exit_task == " ":
            print("Exiting ToDo list...")
            break

    else:
        print('Invalid input, please input a valid choice between 1 to 6')

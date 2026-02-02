import os

while True:
    if not 'todos.txt' in os.listdir():
            with open('todos.txt', 'w') as file:
                file.write('')

    action = input('Type add, show, edit, complete or exit: ')
    action = action.strip()

    if 'add' in action:
        todo = action[4:].capitalize() + '\n'

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    
    elif 'show' in action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    
    elif 'edit' in action:
        number = int(action[5:])
        print(number)

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        todo_removal = todos[index].strip('\n')
        todos.pop(index)

    elif 'complete' in action:
        number = int(action)[9:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        todo_removal = todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        
        message = f'Todo {todo.removal} was removed from the list.'
        print(message)

    elif 'exit' in action:
        break

    else:
        print('command is not valid')

print("Bye!")

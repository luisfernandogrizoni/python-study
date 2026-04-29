import os

def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todo_local = file_local.readlines()
    return todos_local

def write_todos():
    with open('todos.txt', 'w') as file:
    file.writelines(todos)

def remove_todos():
    index = number - 1
    todo_removal = todos[index].strip('\n')
    todos.pop(index)
    
while True:
    if not 'todos.txt' in os.listdir():
            with open('todos.txt', 'w') as file:
                file.write('')

    action = input('Type add, show, edit, complete or exit: ')
    action = action.strip()

    if action.startswith("add"):
        todo = action[4:].capitalize() + '\n'

        todos = get_todos('todos.txt')
        todos.append(todo)
        todos = write_todos()
    
    elif action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    
    elif action.startswith('edit'):
        number = int(action[5:])
        
        print(number)
        todos = get_todos()
        pop = remove_todos()

    elif action.startswith('complete'):
        number = int(action)[9:]
        
        todos = get_todos('todos.txt')
        pop = remove_todos()
        todos = write_todos()
        
        message = f'Todo {todo.removal} was removed from the list.'
        print(message)

    if action.startswith("exit"):
        break

    else:
        print('command is not valid')

print("Bye!")

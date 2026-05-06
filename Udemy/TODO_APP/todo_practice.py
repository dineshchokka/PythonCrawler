todos = []

while True:
    print("Welcome to the todo app")
    user_action = input("add or show or complete or exit : ")
    user_action = user_action.strip() 

    match user_action:
        case 'add':
            todo = input("enter a todo : ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1} : {item}"
                print(row)
        case 'exit':
            break


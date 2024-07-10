import json

def load_tasks():
    try:
        with open('task.json','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open('tasks.json','w') as file:
        json.dump(tasks,file)
def display_tasks(tasks):
    for i, task in enumerate(tasks, 1):
        print(f"{i}.{task}")     

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List:")
        display_tasks(tasks)
        print("\nOptions: [A]dd, [D]elete, [Q]uit")
        choice = input("Choose an Option: ").strip()      

        if choice ==  'A':
            task = input("Enter a new Task: ").strip()
            tasks.append(task)
            save_tasks(tasks)
        elif choice == 'D':
            task_num =int(input("Enter Task Number To Delete: "))      
            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)
                save_tasks(tasks)
        elif choice == 'Q':
            break


if __name__ == '__main__':
    main()




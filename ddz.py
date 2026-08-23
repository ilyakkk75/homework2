path = "resources/workouts.txt"

def add_workout(**kwargs):
    workouts = dict()
    try:
        with open(path, "r", encoding="utf-8") as file:
            for i in file.readlines():
                ls = i.strip().split(",")
                if len(ls) == 2:
                    workouts[ls[0]] = ls[1]
    except FileNotFoundError:
        pass
    workouts[kwargs['name']] = f"{kwargs['exercises']}"
    with open(path, "w", encoding="utf-8") as file:
        for key, value in workouts.items():
            file.write(f"{key},{value}\n")

def show_workouts():
    try:
        with open(path, "r", encoding="utf-8") as file:
            for i in file.readlines():
                ls = i.strip().split(",")
                if len(ls) == 2:
                    print(f"{ls[0]} - {ls[1]}\n")
    except FileNotFoundError:
        pass
        print("список пуст\n")

while True:
    action = input("команда (add/show/exit): ")
    if action == "add":
        name = input("название тренировки: ")
        exercises = input("упражнения через ; : ")
        add_workout(name=name, exercises=exercises)
    elif action == "show":
        show_workouts()
    elif action == "exit":
        break
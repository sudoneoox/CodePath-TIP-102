def print_todo_list(task):
    i = 1
    print("Pooh's To Dos:")
    for item in task:
        print(f"{i}. {item}")
        i += 1
    print()


task = [
    "Count all the bees in the hive",
    "Chase all the clouds from the sky",
    "Think",
    "Stoutness Exercises",
]
print_todo_list(task)

task = []
print_todo_list(task)

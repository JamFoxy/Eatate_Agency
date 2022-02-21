def work():
    d_1 = "\n Enter 1 - show 'to-do list'\n"
    d_2 = "Enter 2 - write the deal you are going to do\n"
    d_3 = "Enter 3 - show list of finished instructions\n"
    d_4 = "Enter 4 - show salary\n"
    print(d_1, d_2, d_3, d_4)
    wo = int(input("Please dial the menu number to work with the program,\n If you're done, dial 5:"))
    import json
    if wo == 1:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            print(tasks)
            for item in tasks:
                print(item["number"], item["item"])
            work()
    if wo == 2:
        import d_task
        d_task.d_task()
        work()
    if wo == 3:
        with open("completed_tasks.json", "r") as c_file:
            c = json.load(c_file)
            new_list = []
            new_list.append(c)
            for item in new_list:
                print("Done: ", item["Done"])
        work()
    if wo == 4:
        print("Your salary is 500$")
        work()
    if wo == 5:
        print("The program is over, we look forward to your return! ")

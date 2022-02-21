def d():
    import json
    d_1 = "\n Enter 1 - Show a list of all coverage areas\n"
    d_2 = "Enter 2 - Show list of budget categories\n"
    d_3 = "Enter 3 - Show dedicated budget for a specific category of marketing sites\n"
    d_4 = "Enter 4 - Show current marketing funds\n"
    d_5 = "Enter 5 - Show total budget required for salary\n"
    d_6 = "Enter 6 - Increase the salary of an employee\n"
    d_7 = "Enter 7 - Decrease the salary of an employee\n"
    d_8 = "Enter 8 - Show a list of equipment for the construction of objects\n"
    print(d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8)
    ab = int(input("Please dial the menu number to work with the program,\n If you're done, dial 9:"))
    if ab == 1:
        print("List of all coverage for specific areas")
        with open("areas.json", "r") as file:
            areas = json.load(file)
            for i in areas:
                print(i["c"], i["n"])
        d()
    elif ab == 2:
        def b():
            budg = input("Choose a category of budget m/s: ")
            mark = "The marketing budget: 400.000$"
            sal = "Salary budget: 380.000$"
            if budg == "m":
                print(mark)
                d()
            elif budg == "s":
                print(sal)
                d()
            else:
                print("Try again")
                b()
        print(b())
        d()
    elif ab == 3:
        print("Marketing Zones Budget::")
        bu = int(input("\n1 - Facebook \n2 - Instagram \n3 - Google Ads \n4 - YouTube \nSelect one from the list (1-4):"))
        if bu == 1:
            print("1100$")
            d()
        if bu == 2:
            print("450$")
            d()
        if bu == 3:
            print('129.44$')
            d()
        if bu == 4:
            print('85$')
            d()
        else:
            print("You must type numbers from 1 to 4!")
    elif ab == 4:
        print("General marketing media: ")
        with open("cost.json", "r") as r_file:
            costos = json.load(r_file)
            list_1 = []
            list_1.append(costos)
            for i in list_1:
                print(i["Last"], "$ left")
        d()
    elif ab == 5:
        g_budg = 300000
        print("Salary budget: ", g_budg)
        d()
    elif ab == 6:
        print("--------All employees--------")
        with open("sale-manager_db.json", "r") as r_file:
            sale_db = json.load(r_file)
            print("     Sale-managers:")
            for item in sale_db:
                print(item)
        with open("worker_db.json", "r") as r_file:
            worker_db = json.load(r_file)
            print("     Workers:")
            for item in worker_db:
                print(item)
        with open("manager_db.json", "r") as r_file:
            manager_db = json.load(r_file)
            print("     Managers:")
            for item in manager_db:
                print(item)
        with open("marketing_db.json", "r") as r_file:
            marketing_db = json.load(r_file)
            print("     Marketers:")
            for item in marketing_db:
                print(item)
        emp = input("Type the name of the employee you want to increase the salary for:")
        mark = 700
        final = int(input("Enter the amount of the salary increase: "))
        sal = mark + final
        print("The surcharge has been successfully completed!\nThe current salary for this employee after the surcharge is: ", sal)
        d()
    elif ab == 7:
        print("--------All employees--------")
        with open("sale-manager_db.json", "r") as r_file:
            sale_db = json.load(r_file)
            print("     Sale-managers:")
            for item in sale_db:
                print(item)
        with open("worker_db.json", "r") as r_file:
            worker_db = json.load(r_file)
            print("     Workers:")
            for item in worker_db:
                print(item)
        with open("manager_db.json", "r") as r_file:
            manager_db = json.load(r_file)
            print("     Managers:")
            for item in manager_db:
                print(item)
        with open("marketing_db.json", "r") as r_file:
            marketing_db = json.load(r_file)
            print("     Marketers:")
            for item in marketing_db:
                print(item)
        emp = input("Type the name of the employee you want to decrease the salary for:")
        mark = 700
        final = int(input("Enter the amount of the salary decrease: "))
        sal = mark - final
        print("The decrease has been successfully completed!\nThe current salary for this employee after the decrease:", sal)
        d()
    elif ab == 8:
        with open("objects.json","r") as file:
            objects = json.load(file)
            for item in objects:
                print(item["number"], item["obj"], item["sta"])
            d()
    elif ab == 9:
        print("The program is over, we look forward to your return! ")
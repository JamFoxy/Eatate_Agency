def man():
    d_1 = "\n Enter 1 - to see list of all workers\n"
    d_2 = "Enter 2 - to see 'to-do list'\n"
    d_3 = "Enter 3 - list of instructions to employees\n"
    d_4 = "Enter 4 - show a list of all coverage for specific areas\n"
    d_5 = "Enter 5 - show the amount for real estate, for sale, for rent\n"
    d_6 = "Enter 6 - calculate % by category of real estate\n"
    print(d_1, d_2, d_3, d_4, d_5, d_6)
    m = int(input("Please dial the menu number to work with the program,\n If you're done, dial 7:"))
    import json
    if m == 1:
        with open("marketing_db.json", "r") as r_file:
            marketing_db = json.load(r_file)
            print("Marketers:")
            for i in marketing_db:
                print(i)
        with open("worker_db.json", "r") as r_file:
            worker_db = json.load(r_file)
            print("Workers:")
            for ite in worker_db:
                print(ite)
        with open("sale-manager_db.json", "r") as r_file:
            sale_db = json.load(r_file)
            print("Sale-managers:")
            for i in sale_db:
                print(i)
        man()
    if m == 2:
        with open("m_tasks.json", "r") as file:
            m_tasks = json.load(file)
            for item in m_tasks:
                print(item["number"], item["item"])
            f = "item"
            a = input("Enter the name of task: ")
            m_tasks[5][f] = a
            with open("m_tasks.json", "w") as w_file:
                json.dump(m_tasks, w_file)
        man()
    if m == 3:
        with open("list_em.json", "r") as file:
            list_em = json.load(file)
            for k in list_em:
                print(k["emp"], k["do"])
        man()
    if m == 4:
        print("List of all coverage for specific areas")
        with open("areas.json", "r") as file:
            areas = json.load(file)
            for i in areas:
                print(i["c"], i["n"])
        man()
    if m == 5:
        with open("sale_building.json", 'r')as file:
            sale_building = json.load(file)
            print("Total amount for sale:")
            for item in sale_building:
                print(item["nam"], item["sum"])
        with open("rent_building.json", 'r')as file:
            rent_building = json.load(file)
            print("Total amount for rent:")
            for item in rent_building:
                print(item["nam"], item["sum"])
        man()
    if m == 6:
        prop = int(input("Enter the rental amount with subsequent purchase: "))
        v1 = ('{:.10f}'.format(prop / 100 * 45))
        print("Rent - 45%: ", v1.rstrip('0'))
        v2 = ('{:.10f}'.format(prop / 100 * 50))
        print("Sale - 50%: ", v2.rstrip('0'))
        v3 = ('{:.10f}'.format(prop / 100 * 5))
        print("Long-term lease with subsequent purchase - 5%: ", v3.rstrip('0'))
        man()
    if m == 7:
        print("The program is over, we look forward to your return!")

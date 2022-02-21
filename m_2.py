def m_2():
    import m
    import json
    with open("cost.json") as file:
        try:
            cos = json.load(file)
        except json.decoder.JSONDecodeError:
            cos = {}
    bg = 40000
    prom = input(" \nFacebook \nInstagram \nGoogle Ads \nYouTube \nChoose a title to promote:")
    if prom == "Facebook":
        am = int(input("Type the amount of expense you want to spend from the budget:"))
        if am > bg:
            print("amount exceeded!")
            m_2()
        if am < bg:
            cost = bg - am
            key = "Last"
            cos[key] = cost
            with open("cost.json", 'w') as file:
                json.dump(cos, file)
            print(" Sucsess!\n You have", cost, "$ left")
            m.m()
    if prom == "Instagram":
        am = int(input("Type the amount of expense you want to spend from the budget:"))
        if am > bg:
            print("amount exceeded!")
            m_2()
        if am < bg:
            cost = bg - am
            key = "Last"
            cos[key] = cost
            with open("cost.json", 'w') as file:
                json.dump(cos, file)
            print(" Sucsess!\n You have", cost, "$ left")
            m.m()
    if prom == "Google Ads":
        am = int(input("Type the amount of expense you want to spend from the budget:"))
        if am > bg:
            print("amount exceeded!")
            m_2()
        if am < bg:
            cost = bg - am
            key = "Last"
            cos[key] = cost
            with open("cost.json", 'w') as file:
                json.dump(cos, file)
            print("You have", cost, "$ left")
            m.m()
    if prom == "YouTube":
        am = int(input("Type the amount of expense you want to spend from the budget:"))
        if am > bg:
            print("amount exceeded!")
            m_2()
        if am < bg:
            cost = bg - am
            key = "Last"
            cos[key] = cost
            with open("cost.json", 'w') as file:
                json.dump(cos, file)
            print(" Sucsess!\n You have", cost, "$ left")
            m.m()

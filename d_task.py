def d_task():
    import json
    with open("completed_tasks.json") as com_file:
        try:
            compl = json.load(com_file)
        except json.decoder.JSONDecodeError:
            compl = {}
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
        for item in tasks:
            print(item["number"], item["item"])
    d = {"1": ["Make a review"], "2": ["Revise old projects"], "3": ["Talk with boss"], "4": ["Prepare all documents"]}
    a = input("Type the number of deal you are going to do: ")
    b = "Done"
    if a in d.keys():
        word = 'You deal with: '
        h = d[a][0]
        print(word, h)
        dict = {}
        dict[b] = h
        with open("completed_tasks.json", "w") as com_file:
            compl = json.dump(dict, com_file)
    else:
        print("Sorry, but you need to type number from 1 to 4")
        d_task()

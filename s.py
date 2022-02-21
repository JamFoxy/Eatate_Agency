import pandas as pd
import json
def s():
    d_1 = "\n Enter 1 - Show all clients\n"
    d_2 = "Enter 2 - Client search\n"
    d_3 = "Enter 3 - Show available apartments for purchase\n"
    d_4 = "Enter 4 - Show sold apartments\n"
    d_5 = "Enter 5 - Show the most expensive apartment\n"
    d_6 = "Enter 6 - Show the cheapest apartment\n"
    d_7 = "Enter 7 - Sell an apartment\n"
    d_8 = "Enter 8 - Rent out an apartment\n"
    d_9 = "Enter 9 - Show free objects\n"
    d_10 = "Enter 10 - Display of rented objects\n"
    print(d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10)
    sale = int(input("Please dial the menu number to work with the program,\n If you're done, dial 11:"))
    if sale == 1:
        df = pd.read_csv('search.csv')
        print(df)
        s()
    elif sale == 2:
        df = pd.read_csv('search.csv')
        print(df['Clients'])
        df.index +=1
        a = input('Enter customer name to search: ')
        b = df['Clients'].isin([a])
        print("Client was found: ")
        print(df[b])
        s()
    elif sale == 3:
        print("Free Apartments: ")
        with open("free_ap.json", "r", encoding='utf-8') as file:
            free_ap = json.load(file)
            for item in free_ap:
                print(item["number"], item["place"])
        s()
    elif sale == 4:
        print("Sold Apartments: ")
        with open("sold_ap.json", "r", encoding='utf-8') as file:
            sold_ap = json.load(file)
            for item in sold_ap:
                print(item["number"], item["place"])
        s()
    elif sale == 5:
        expensive = "Apartment 75: Jal-29,18. Cost: 366 $ per month"
        print("Most expensive apartment: ", expensive)
        s()
    elif sale == 6:
        cheep = "Apartment 111: Tokombaeva 21/3"
        print("The cheapest apartment: ", cheep)
        s()
    elif sale == 7:
        with open("sale-buildings.json", "r", encoding='utf-8') as file:
            sale_buildings = json.load(file)
            for item in sale_buildings:
                print(item["adress"], item["name"])
        def Seven():
            f = "adress"
            n = "name"
            adr = input("Please write the sales address: ")
            host = input("Please write the new owner of the apartment: ")
            with open("sale-buildings.json", "r", encoding='utf-8') as file:
                sale_buildings = json.load(file)
                if adr == "Tynystanova 12":
                    sale_buildings[0][f] = adr
                    sale_buildings[0][n] = host
                    with open("sale-buildings.json", "w") as w_file:
                        json.dump(sale_buildings, w_file)
                elif adr == "Gorkogo 3":
                    sale_buildings[2][f] = adr
                    sale_buildings[2][n] = host
                    with open("sale-buildings.json", "w") as fi3le:
                        json.dump(sale_buildings, fi3le)
                elif adr == "Isanova 33":
                    sale_buildings[3][f] = adr
                    sale_buildings[3][n] = host
                    with open("sale-buildings.json", "w") as w_f:
                        json.dump(sale_buildings, w_f)
                elif adr == "Abay 4":
                    sale_buildings[1][f] = adr
                    sale_buildings[1][n] = host
                    with open("sale-buildings.json", "w") as w_fi:
                        json.dump(sale_buildings, w_fi)
                else:
                    print("Please, choose something from the list")
                    Seven()
            print("Done!")
            print()
        print(Seven())
        s()
    elif sale == 8:
        with open("rent.json", "r") as file:
            rent = json.load(file)
            for i in rent:
                print(i["address"], i["name"], i["sum"], i["dline"])
        def Eight():
            f = "address"
            n = "name"
            status = "status"
            fin = "occupied"
            adr = input("Please write the sales address: ")
            host = input("Please write the new owner of the apartment: ")
            with open("rent.json", "r") as file:
                rent = json.load(file)
                if adr == "Tynystanova 12":
                    rent[1][f] = adr
                    rent[1][n] = host
                    rent[1][status] = fin
                    with open("rent.json", "w") as w_file:
                        json.dump(rent, w_file)
                        print("Done!")
                elif adr == "Abay 4":
                    rent[3][f] = adr
                    rent[3][n] = host
                    rent[3][status] = fin
                    with open("rent.json", "w") as w_file:
                        json.dump(rent, w_file)
                        print("Done!")
                elif adr == "Gogolya 56":
                    rent[4][f] = adr
                    rent[4][n] = host
                    rent[4][status] = fin
                    with open("rent.json", "w") as w_file:
                        json.dump(rent, w_file)
                        print("Done!")
                elif adr == "Gorkogo 3":
                    rent[6][f] = adr
                    rent[6][n] = host
                    rent[6][status] = fin
                    with open("rent.json", "w") as w_file:
                        json.dump(rent, w_file)
                        print("Done!")
                elif adr == "Isanova 33":
                    rent[8][f] = adr
                    rent[8][n] = host
                    rent[8][status] = fin
                    with open("rent.json", "w") as w_file:
                        json.dump(rent, w_file)
                        print("Done!")
                elif adr == "Togolok-Moldo 132":
                    print("This apartment is occupied!\nPlease, choose another apartment")
                    Eight()
                elif adr == "Chyngyz Aitmatov Avenue 176":
                    print("This apartment is occupied!\nPlease, choose another apartment")
                    Eight()
                elif adr == "Gogolya 44":
                    print("This apartment is occupied!\nPlease, choose another apartment")
                    Eight()
                elif adr == "Matrosova 5":
                    print("This apartment is occupied!\nPlease, choose another apartment")
                    Eight()
                else:
                    print("Please, choose something from the list!")
                    Eight()
        print(Eight())
        s()
    elif sale == 9:
        with open("rent.json", "r", encoding='utf-8') as file:
            rent = json.load(file)
            new_list = []
            for d in rent:
                if d.get('status') == 'occupied':
                    new_list.append(d)
                    for item in new_list:
                        pass
                    print(item["address"], item["status"])
        s()
    elif sale == 10:
        with open("rent.json", "r", encoding='utf-8') as file:
            rent = json.load(file)
            new_list = []
            for d in rent:
                if d.get('status') == 'free':
                    new_list.append(d)
                    for item in new_list:
                        pass
                    print(item["address"], item["status"])
        s()
    elif sale == 11:
        print("The program is over, we look forward to your return! ")


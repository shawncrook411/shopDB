from ShopSurvey import ShopSurvey
from Employee import Employee
from Store import Store
import datetime
import pickle
import os

# TODO: Tie valid stores so they aren't hardcoded, into the Store obj files
validStores = ["1626", "1515"]

def create_employee():
    try:
        employee = Employee()
        value = input("What is the Employee ID: ").upper()

        if value in os.listdir(Employee.obj_file_path):
            print("Employee ID is already used, duplicate error")
            repeat = input("Did you want to re-create it?: ")

            if 'n' in repeat.lower() or 'f' in repeat.lower():
                return None
        employee.employeeID = value

        value = value[1:5]

        if value in validStores:
            employee.storeID = value

        else:
            while True:
                value = input("What is the Store ID: ").strip()

                if value in validStores:
                    employee.storeID = value
                    break
                print("Invalid Store ID, please try again")

        value = input("What is the employees full name? : 'first last': ")
        value = value.lower().split(" ")
        
        employee.first = value[0].capitalize()
        employee.last = value[1].capitalize()
        

        while True:
                try:
                    value = input("\nWhat day did this employee get hired? Put in MM/DD/YY format: ")
                    value = value.split("/")
                    employee.hired_date = datetime.datetime(int(value[2]), int(value[0]), int(value[1]))
                    break
                except TypeError:
                    print("\nInvalid day type, please try Again\n")

        value = input("Is this employee a manager? Press [1/t/True] or [2/f/False]\n")
        if 't' in value or '1' in value:
            employee.manager = True

            while True:
                try:
                    value = input("\nWhat day did this manager certify? Put in MM/DD/YY format: ")
                    value = value.split("/")
                    employee.cert_date = datetime.datetime(int(value[2]), int(value[0]), int(value[1]))
                    break
                except TypeError:
                    print("\nInvalid day type, please try Again\n")       

        return employee 

    except ValueError as e:
        print(e)


def create_shop():
    try:
        shop = ShopSurvey()       
        value = input("What is the Shop ID: ")
        
        if value in os.listdir(ShopSurvey.obj_file_path):
            print("Shop ID is already used, duplicate error")
            repeat = input("Did you want to re-create it?: ")

            if 'n' in repeat.lower() or 'f' in repeat.lower():
                return None
        
        shop.shopID = int(value)


        while True:
            value = input("What is the Store ID: ").strip()

            if value in validStores:
                shop.storeID = value
                break

        while True:
            value = int(input("\nWhat time was the Shop:\nPress 1 for 11-1:30\nPress 2 for 1:30-4\nPress 3 for 4-7\nPress 4 for 7-10\nPress 5 for Phantom\n"))
            if 0 < value <= 5:
                shop.set_time_code(value-1)
                break

        while True:
            value = input("\nWhat type of shop was this?\nPress 1 for Regular\nPress 2 for Online\nPress 3 for Curbside\nPress 4 for Delivery\nPress 5 for Call-In\n")
            if 0 < int(value) <= 5:
                shop.type = value
                break

        while True:
            try:
                value = input("\nWhat day was this shop? Put in MM/DD/YY format: ")
                value = value.split("/")
                shop.day = datetime.datetime(int(value[2]+2000), int(value[0]), int(value[1]))
                shop.weekday = shop.day.strftime("%A")
                break
            except TypeError:
                print("\nInvalid day type, please try Again\n")

        
        while True:
            try:
                value = int(input("What was the Total Score?: "))
                
                if value == 100:
                    shop.perfect()

                    shop.cashier = input("Who was the Cashier?: ")
                    return shop
                
                if 0 <= value < 100:
                    shop.score = value               
                        

                value = int(input("What was the Service Score?: "))
                if 0 <= value <= 100:
                    shop.service_score = value

                value = int(input("What was the Quality Score?: "))
                if 0 <= value <= 100:
                    shop.quality_score = value

                value = int(input("What was the Cleanliness Score?: "))
                if 0 <= value <= 100:
                    shop.clean_score = value

                value = int(input("What was the Satisfaction Score?: "))
                if 0 <= value <= 100:
                    shop.satisfy_score = value

                check = shop.check_valid_scores(shop.score, shop.service_score, shop.quality_score, shop.clean_score, shop.satisfy_score)
                if not check:
                    print("\nValues don't add up, please try again\n")
                    continue
                print()
                break 
            except TypeError:
                print("\nInvalid types given, please Try Again\n")               

        while True:
            try:
                value = float(input("What was the ticket time? Put in decimal notation, so 8.45 for 8 mins 45 seconds\n"))
                x = int(value * 100)
                y = int(value*100 % 100)
                x = (x // 100) + (y/60)

                shop.large_ticket_time = True
                shop.small_ticket_time = True

                if x >= 10:
                    shop.large_ticket_time = False
                    
                if x >= 8:
                    shop.small_ticket_time = False

                shop.ticket_min = x
                shop.ticket_time = value
                break

            except ValueError:
                print("Invalid time value, please try again")

        value = input("\nWas upsell okay? [1/t/True] or [2/f/False]\n")        
        if 't' in value.lower() or '1' in value:
            shop.upsell = True   
        else:
            shop.upsell = False
                    
          
        value = input("Was Fry Quality okay?\nPress [1/t/True] or [2/f/False]\n")
        if 't' in value.lower() or '1' in value:
            shop.fry_quality = True
        else:        
            shop.fry_quality = False        

        
        value = input("Was Fry Quantity okay?\nPress [1/t/True] or [2/f/False]\n")
        if value.lower() in ['1', 't', 'true']:
            shop.fry_quantity = True            
        else:
            shop.fry_quantity = False
            

        
        value = input("Was Friendly Greeting okay?\nPress [1/t/True] or [2/f/False]\n")
        if value.lower() in ['1', 't', 'true']:
            shop.friendly_greeting = True            
        else:
            shop.friendly_greeting = False           

        
        value = input("Was Lobby Cleanliness okay?\nPress [1/t/True] or [2/f/False]\n")
        if value.lower() in ['1', 't', 'true']:
            shop.lobby_clean = True            
        else:
            shop.lobby_clean = False           
        
        shop.cashier = input("Who was the Cashier?: ")

        return shop
    
    except KeyboardInterrupt:
        return None    


def write_obj(obj):

    if isinstance(obj, ShopSurvey):
        with open(f"{ShopSurvey.obj_file_path}{obj.shopID}", 'wb') as file:
            pickle.dump(obj, file)

    elif isinstance(obj, Store):
        with open(f"{Store.obj_file_path}{obj.storeID}", 'wb') as file:
            pickle.dump(obj, file)
    
    elif isinstance(obj, Employee):
        with open(f"{Employee.obj_file_path}{obj.employeeID}", 'wb') as file:
            pickle.dump(obj, file)
    else:
        print('PICKLE FAILURE, OBJ INVALID TYPE')

def open_obj(folder_dir):
    data = []
    for objID in os.listdir(folder_dir):
        with open(folder_dir + objID, 'rb') as file:
            obj = pickle.load(file)
            data.append(obj)
    return data

def rewrite_sqls():
    with open(ShopSurvey.sql_file_path, "w") as sql:
        data = open_obj(ShopSurvey.obj_file_path)
        sql.write(f"DELETE FROM {ShopSurvey.sql_table};\n\n")
        for shop in data:
            sql.write(shop.to_sql_insert())

    with open(Store.sql_file_path, "w") as sql:
        data = open_obj(Store.obj_file_path)
        sql.write(f"DELETE FROM {Store.sql_table};\n\n")
        for store in data:
            sql.write(store.to_sql_insert())

    with open(Employee.sql_file_path, "w") as sql:
        data = open_obj(Employee.obj_file_path)
        sql.write(f"DELETE FROM {Employee.sql_table};\n\n")
        for e in data:
            sql.write(e.to_sql_insert())

def clean_data():
    data = open_obj(Employee.obj_file_path)
    for obj in data:
        write_obj(obj)
   

    data = open_obj(ShopSurvey.obj_file_path)
    for obj in data:    
        write_obj(obj)

    data = open_obj(Store.obj_file_path)
    for s in data:
        write_obj(s)
    

def main():
    
    shops = []
    print("Welcome to Shop Survey CLI!\n")
    while True:
        print("\nWhat would you like to do?\n1. Input new Shop\n2. Print saved obj files\n3. Re-create SQL file(s)\n4. Re-write Store(s)\n5. Input New Employee(s)\n6. Quit")
        answer = input()
        
        if '1' in answer:
            while True:
                shop = create_shop()

                if isinstance(shop, ShopSurvey):
                    shops.append(shop)
                    write_obj(shop)
                else:
                    print("Create Shop Failure")
                    print("SHOP: " + str(shop))
                    

                continueBool = input("Would you like to create another?: ")

                if 'n' in continueBool.lower():
                    break

            continue
        
        if '2'in answer:
            data = open_obj(ShopSurvey.obj_file_path)
            for shop in data:
                print(shop)

            print()

            data = open_obj(Employee.obj_file_path)
            for e in data:
                print(e)

            print()

            data = open_obj(Store.obj_file_path)
            for s in data:
                print(s)
            
            continue

       
        if '3' in answer:
            rewrite_sqls()   

            continue
        
        if '4' in answer:
            data = []

            data.append(
                Store(1515, "Casper", "CHELSEY")
            )

            data.append(
                Store(1626, "Cheyenne", "JESSICA")
            )            

            for store in data:
                write_obj(store)           
            
        if '5' in answer:
            while True:
                employee = create_employee()
                employees = []

                if isinstance(employee, Employee):
                    employees.append(employee)
                    write_obj(employee)
                else:
                    print("Create Employee Failure")
                    print("EMPLOYEE: " + str(employee))
                    

                continueBool = input("Would you like to create another?: ")

                if 'n' in continueBool.lower():
                    break

            continue

        if '6' in answer:
            break
        

        if 'x' in answer:
            clean_data()



        

        
        






if __name__ == "__main__":
    main()
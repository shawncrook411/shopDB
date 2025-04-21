from ShopSurvey import ShopSurvey
from Employee import Employee
from Store import Store
from SQL_Table import SQL_Table
import datetime
import pickle
import os

import mysql.connector

classes = [ShopSurvey, Store, Employee]

def create_employee(validStores):
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
                    employee.hired_date = datetime.datetime(int(value[2]+2000), int(value[0]), int(value[1]))
                    break
                except TypeError:
                    print("\nInvalid day type, please try Again\n")

        value = input("Is this employee a manager? Press [1/t/True] or [2/f/False] or 3 for GM\n")
        if 't' in value or '1' in value or '3' in value:
            employee.manager = 1

            if '3' in value: 
                employee.manager = 2            

            while True:
                try:
                    value = input("\nWhat day did this manager certify? Put in MM/DD/YY format: ")
                    value = value.split("/")
                    employee.cert_date = datetime.datetime(int(value[2])+2000, int(value[0]), int(value[1]))
                    break
                except TypeError:
                    print("\nInvalid day type, please try Again\n")       

        return employee 

    except ValueError as e:
        print(e)
    except ValueError:
        return create_employee(validStores)


def create_shop(validStores, validEmployees):
    try:
        shop = ShopSurvey()       
        
        while True:
            value = input("What is the Shop ID: ")

            if value in os.listdir(ShopSurvey.obj_file_path):
                print("Shop ID is already used, duplicate error")
                repeat = input("Did you want to re-create it?: ")

                if 'n' in repeat.lower() or 'f' in repeat.lower():
                    return None
            
            shop.shopID = int(value)
            break


        while True:
            value = int(input("What is the Store ID: "))

            if value in validStores:
                shop.storeID = value
                break
            else:
                print(f"Invalid StoreID given, Valid Stores : {validStores}")

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
                value = input("\nWhat day was this shop? Put in MM/DD/YY format: ").strip()
                value = value.split("/")

                if int(value[2]) < 2000: 
                    value[2] = int(value[2]) + 2000

                shop.day = datetime.datetime(int(value[2]), int(value[0]), int(value[1]))
                shop.weekday = shop.day.strftime("%A")
                break
            except TypeError as e:
                print(e)
                print("\nInvalid day type, please try Again\n")

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
        
        while True:
            try:
                value = int(input("What was the Total Score?: "))
                
                if value == 100:
                    shop.perfect()

                    while True:
                        value = input("Who was the Cashier?: ")

                        for e in validEmployees:
                            if value in e and shop.storeID in e:
                                shop.cashier = e[-1]
                                return shop      
                        print("No Employee found with that first name, please try again\n")
                
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
        
        while True:
            value = input("Who was the Cashier?: ")

            for e in validEmployees:
                if value in e and shop.storeID in e:
                    shop.cashier = e[-1].capitalize()
                    return shop      
            print("No Employee found with that first name, please try again\n")    

    
    except KeyboardInterrupt:
        return None  
    except ValueError as e:
        print(e)
        print("\n\n\tPlease Try again\n")
        return create_shop(validStores, validEmployees)  
    
def populate_shops(validEmployees, validShops):
    while True:
        try:
            while True:
                value = input("What is the ShopID: ")

                if value in validShops:
                    shop = validShops.indexof(value)
                    break

                print("Invalid ShopID given, Please try again\n")

            while True:
                value = input("Which employeee (first_name) would you like to add?")                

                for e in validEmployees:
                    if value in e and shop[1] :
                        shop.cashier = e[-1]
                        return shop      
                print("No Employee found with that first name, please try again\n")



        except ValueError | TypeError as err:
            print(err)


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

    for cls in classes:
        with open(cls.sql_file_path, "w") as sql:
            data = open_obj(cls.obj_file_path)
            sql.write(f"DELETE FROM {cls.sql_table};\n\n")
            for shop in data:
                sql.write(shop.to_sql_insert())   

def clean_data():

    for cls in classes:
        data = open_obj(cls.obj_file_path)
        for obj in data:
            write_obj(obj)

    data = open_obj(Employee.obj_file_path)
    for obj in data:
        write_obj(obj)
        

def main():

    shopConnection = mysql.connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        database='shop',
        auth_plugin='mysql_native_password'
    )

    cur  = shopConnection.cursor()

    cur.execute("SELECT * FROM STORE")
    rows = cur.fetchall()
    
    validStores = []
    for row in rows:
        validStores.append(row[0])

    cur.execute("SELECT First_Name, StoreID, EmployeeID FROM CREW")
    rows = cur.fetchall()

    validEmployees = []
    for row in rows:
        validEmployees.append(row)

    cur.execute("SELECT ShopID, StoreID FROM ShopResult")
    rows = cur.fetchall()

    validShops = []
    for row in rows:
        validShops.append(row)  
    
    
    shops = []
    print("Welcome to Shop Survey CLI!\n")
    while True:
        print( 
            (
                "   What would you like to do?\n"
                "1. Input new Shop\n"
                "2. Print saved obj files\n"
                "3. Re-create SQL file(s)\n"
                "4. Re-write Store(s)\n"
                "5. Input New Employee(s)\n"
                "6. Add Employees to Shop\n"
                "7. Quit"
            )
        )
        answer = input()
        
        if '1' in answer:
            while True:
                shop = create_shop(validStores, validEmployees)

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
                Store(1515, "Casper")
            )

            data.append(
                Store(1626, "Cheyenne")
            )            

            for store in data:
                write_obj(store)           
            
        if '5' in answer:
            while True:
                employee = create_employee(validStores)
                employees = []

                if isinstance(employee, Employee):
                    employees.append(employee)
                    write_obj(employee)
                else:
                    print("Create Employee Failure")
                    print("EMPLOYEE: " + str(employee))
                    

                continueBool = input("Would you like to create another?: ")

                if 'n' in continueBool.lower():
                    shopConnection.close()
                    break

            continue

        if '6' in answer:
            populate_shops(validEmployees, validShops)



        if '7' in answer:
            break        

        if 'x' in answer:
            clean_data()

        if 't' in answer:
            print(issubclass(ShopSurvey, SQL_Table))



        

        
        






if __name__ == "__main__":
    main()
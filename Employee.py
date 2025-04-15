import datetime
from SQL_Table import SQL_Table

class Employee(SQL_Table):
    obj_file_path = 'data/crew_obj/'
    sql_file_path = 'sql_data/employee.sql'
    sql_table = 'Crew'

    def __init__(self):
        self.storeID = None
        self.employeeID = None
        self.first = None
        self.last = None
        self.manager = False
        self.hired_date = None
        self.cert_date = None

    def __str__(self):
        return (
            f"Employee Information:\n"
            f"  Employee ID: {self.employeeID}\n"
            f"  Store ID: {self.storeID}\n"
            f"  Name: {self.first} {self.last}\n"
            f"  Hired Date: {self.hired_date.strftime("%x")}\n"
            f"  Manager: {self.manager}\n"
            f"  Certify Date:  {self.cert_date.strftime("%x")}\n" if self.manager else ""            
        )  

    def to_sql_insert(self):
        """
        Generates an SQL INSERT statement for adding the survey data to the Store table.
        
        Returns:
            str: SQL INSERT statement for the ShopResult table
        """
        # Format values according to SQL data types
        # Convert None values to 'NULL'
        # Wrap strings in quotes
        # Convert booleans to 1/0

        def convert_bool_to_null(attr):
            if attr is None:
                return "'NULL'"
            if attr:
                return '1'
            return '0'
        
        def convert_str_to_null(attr):
            if attr is None:
                return "'NULL'"
            return f'"{attr}"'
        
        def convert_int_to_null(attr):
            if attr is None:
                return "'NULL'"
            return attr     

        def convert_date_to_sql(date):
            if isinstance(date, datetime.datetime):
                return (
                    f'"{date.strftime("%Y")}-{date.strftime("%m")}-{date.strftime("%d")}"'
                )  
            return "'NULL'"    
       
        # Format bool fields
        manager = convert_bool_to_null(self.manager)

        # Format string fields
        id = convert_str_to_null(self.employeeID)
        first = convert_str_to_null(self.first) 
        last = convert_str_to_null(self.last)

        # Format numeric fields
        storeID = convert_int_to_null(self.storeID)

        if self.manager:
            return (
            f"INSERT INTO Crew (\n"
            f"EmployeeID, First_Name, Last_Name, Manager, "
            f"StoreID, HiredDate, Manager_Certify_Date"
            f") VALUES (\n"
            f"    {id}, {first}, {last},"
            f"    {manager}, {storeID}, {convert_date_to_sql(self.hired_date)},"
            f"    {convert_date_to_sql(self.cert_date)}" 
            f");\n\n"
        )

        else:

            return (
            f"INSERT INTO Crew (\n"
            f"EmployeeID, First_Name, Last_Name,"
            f"StoreID, HiredDate"
            f") VALUES (\n"
            f"    {id}, {first}, {last},"
            f"    {storeID}, {convert_date_to_sql(self.hired_date)}"
            f");\n\n"
        )              
            

def main():
    pass

if __name__ == "__main__":
    main()
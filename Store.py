from SQL_Table import SQL_Table

class Store(SQL_Table):
    obj_file_path = 'data/store_obj/'
    sql_file_path = 'sql_data/store.sql'
    sql_table = 'Store'

    def __init__(self, id, name, gm):
        if id <= 2500:
            self.storeID = id
        else:
            raise ValueError
        
        self.name = name
        
        self.gm = gm
        self.employees = []

    def __str__(self):
        return (
            f"Store Information: "
            f"  StoreID: {self.storeID}"
            f"  General Manager: {self.gm}"
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
       
        # Format string fields
        gm = convert_str_to_null(self.gm)
        name = convert_str_to_null(self.name)

        # Format numeric fields
        storeID = convert_int_to_null(self.storeID)

        # Build the SQL INSERT statement
        insert_statement = (
            f"INSERT INTO Store (\n"
            f"StoreID, Store_Name, General_Manager"           
            f") VALUES (\n"
            f"    {storeID}, {name},{gm}"
            f");\n\n"
        )
        
        return insert_statement
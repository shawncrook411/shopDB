import fitz as pdf
import os
import datetime


class ShopSurvey():
    obj_file_path = 'shop_obj/'
    sql_file_path = 'data_shops.sql'
    sql_table = 'ShopResult'
    
    def __init__(self, file_name=None):
        
        self.shopID = None
        self.storeID = None
        self.shift = None
        self.time = None
        self.time_code = None
        self.type = None
        self.day = None
        self.weekday = None
 
        self.score = None
        self.service_score = None
        self.quality_score = None
        self.clean_score = None
        self.satisfy_score = None
 
        self.upsell = None
        self.ticket_time = None
        self.ticket_min = None
        self.small_ticket_time = None
        self.large_ticket_time = None
        self.fry_quality = None
        self.fry_quantity = None
        self.lobby_clean = None
        self.friendly_greeting = None

        self.cashier = None
        
        if file_name:
            self.read_from_txt(file_name)

    def __str__(self):
        return (
            f"Shop Information:\n"
            f"  Shop ID: {self.shopID}\n"
            f"  Store ID: {self.storeID}\n"
            f"  Day: {self.day.strftime("%x")}\n"
            f"  WeekDay: {self.weekday}\n"
            f"  Shift: {self.shift}\n"
            f"  Time: {self.time}\n"
            f"  Time Code: {self.time_code}\n"
            f"  Type: {self.type}\n\n"
            
            f"Scores:\n"
            f"  Overall Score: {self.score}\n"
            f"  Service Score: {self.service_score}\n"
            f"  Quality Score: {self.quality_score}\n"
            f"  Cleanliness Score: {self.clean_score}\n"
            f"  Satisfaction Score: {self.satisfy_score}\n\n"
            
            f"Service Details:\n"
            f"  Upsell: {self.upsell}\n"
            f"  Ticket Time: {self.ticket_time}\n"
            f"  Ticket Minutes: {self.ticket_min}\n"
            f"  Small Ticket Time: {self.small_ticket_time}\n"
            f"  Large Ticket Time: {self.large_ticket_time}\n\n"
            
            f"Quality Details:\n"
            f"  Fry Quality: {self.fry_quality}\n"
            f"  Fry Quantity: {self.fry_quantity}\n\n"
            
            f"Facility & Staff:\n"
            f"  Lobby Cleanliness: {self.lobby_clean}\n"
            f"  Friendly Greeting: {self.friendly_greeting}\n"
            f"  Cashier: {self.cashier}"
        )    
    

    def perfect(self):
        self.score = 100
        self.clean_score = 100
        self.quality_score = 100
        self.satisfy_score = 100
        self.service_score = 100
        self.large_ticket_time = True
        self.small_ticket_time = True
        self.fry_quality = True
        self.fry_quantity = True
        self.friendly_greeting = True
        self.lobby_clean = True

    def set_type_code(self, code):
        types = ['REGULAR', 'ONLINE', 'PHANTOM', 'DELIVERY', 'CURB-SIDE']
        # TODO: uPDATE THIS AREA OF CODE SO THAT TYPE ISN'T INT

    def set_time_code(self, code):
        shifts = ["11am-1:30pm", "1:30pm-4pm", "4pm-7pm", "7pm-10pm"]
        
        match code:

            case 0 | 1: 
                self.shift = "LUNCH"
                self.time_code = code
                self.time = shifts[code]

            case 2 | 3:
                self.shift = "DINNER"
                self.time_code = code
                self.time = shifts[code]

            case 4:
                self.shift = "PHANTOM"
                self.time_code = code
                self.time = shifts[-1]

        if self.shift is None:
            raise ValueError("Testing")

    
    def to_sql_insert(self):
        """
        Generates an SQL INSERT statement for adding the survey data to the ShopResult table.
        
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
            return f"'{attr}'"
        
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
        
        # Format the day as 'YYYY-MM-DD' if it exists
        day_value = convert_date_to_sql(self.day)
        
        # Format boolean fields
        upsell =                convert_bool_to_null(self.upsell)
        small_ticket_time =     convert_bool_to_null(self.small_ticket_time)
        large_ticket_time =     convert_bool_to_null(self.large_ticket_time)
        fry_quality =           convert_bool_to_null(self.fry_quality)
        fry_quantity =          convert_bool_to_null(self.fry_quantity)
        lobby_clean =           convert_bool_to_null(self.lobby_clean)
        friendly_greeting =     convert_bool_to_null(self.friendly_greeting)
        
        # Format string fields
        ticket_time = convert_str_to_null(self.ticket_min)
        cashier =     convert_str_to_null(self.cashier.split(' ')[0])
        shift =       convert_str_to_null(self.shift)
        type_code =  convert_str_to_null(self.type)
        
        # Format numeric fields
        shopID =        convert_int_to_null(self.shopID)    
        storeID =       convert_int_to_null(self.storeID)    
        time_code =     convert_int_to_null(self.time_code)        
        score =         convert_int_to_null(self.score)    
        service_score = convert_int_to_null(self.service_score)            
        quality_score = convert_int_to_null(self.quality_score)            
        clean_score =   convert_int_to_null(self.clean_score)        
        satisfy_score = convert_int_to_null(self.satisfy_score) 

        # Format date fields           
        
        # Build the SQL INSERT statement
        insert_statement = (
            f"INSERT INTO ShopResult (\n"
            f"    ShopID, StoreID, Shift, TimeCode, TypeCode, Day,\n"
            f"    Score, Score_Service, Score_Quality, Score_Clean, Score_Satisfaction,\n"
            f"    Upsell, Ticket_Time, Small_Ticket_Time, Large_Ticket_Time,\n"
            f"    Fry_Quality, Fry_Quantity, Lobby_Clean, Friendly_Greeting,\n"
            f"    Cashier\n"
            f") VALUES (\n"
            f"    {shopID}, {storeID}, {shift}, {time_code}, {type_code}, {day_value},\n"
            f"    {score}, {service_score}, {quality_score}, {clean_score}, {satisfy_score},\n"
            f"    {upsell}, {ticket_time}, {small_ticket_time}, {large_ticket_time},\n"
            f"    {fry_quality}, {fry_quantity}, {lobby_clean}, {friendly_greeting},\n"
            f"    {cashier}\n"
            f");\n\n"
        )
        
        return insert_statement

    @staticmethod
    def check_valid_scores(overall, service, quality, clean, satisfy):
        combined = service + clean + satisfy + quality
        if combined > 300:
            if combined - 300 != overall:
                return False
            return True
        return overall == 0

if __name__ == "__main__":
    ShopSurvey.run_all()
    
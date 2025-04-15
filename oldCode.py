@staticmethod
    def get_all_files(directory="./shop_files"):
        return os.listdir(directory)

    @staticmethod
    def convert_pdf_to_text(file_name):
        pdf_name = "./shop_files/" + file_name
        doc = pdf.open(pdf_name)

        file_prefix = file_name.split(".")[0]

        out = open("./shop_txt/"+file_prefix+".txt", "wb")
        for page in doc:
            text= page.get_text().encode("utf8")
            out.write(text)
            out.write(bytes((12,)))
        out.close()

    def read_from_txt_test(self, file_name):
        file_name = "./shop_txt/" + file_name


        with open(file_name) as file:
            content = file.read()

    def read_from_txt(self, file_name):
        file_name = "./shop_txt/" + file_name

       
        
        with open(file_name) as file:    
            content = file.read()

            self.content = content            
        
            self.find_StoreID(file)        
            self.find_ShopID(file)
            self.find_Day(file)
            self.find_Score(file)
            self.find_Quality_Score(file)
            self.find_Service_Score(file)
            self.find_Clean_Score(file)
            self.find_Satisfy_Score(file)
            self.find_Time(file)
            self.find_Type(file)
            self.find_Friendly(file)
            self.find_Upsell(file)
            self.find_Ticket_Time(file)
            self.find_Fry_Quantity(file)
            self.find_Fry_Quality(file)
            self.find_Lobby_Clean(file)
            self.find_Cashier(file)
              

    def find_StoreID(self, file):     
    
        for index, line in enumerate(file):       

            if line.find("Site") != -1:
                self.StoreID = int(line.split()[-1])
                return
    
    def find_ShopID(self, file):
        check_index = None
        for index, line in enumerate(file):

            if line.find("Assignment") != -1:
                check_index = index+1

            if index == check_index:
                self.ShopID = int(line.split()[-1])
                return
            
        
            
    def find_Time(self, file):
        check_index = None
        for index, line in enumerate(file):

            if line.find("Time In:") != -1:
                check_index = index+1

            if index == check_index:
                self.Time = line.strip()
                break
        
        # TODO: UPDATE VALUES AND CONVERTED ARRAY TO MEET FORMATTING, 4 SHIFTs TOTAL
        values = ["11 am-1:29 pm", "1:30 pm-3:59 pm", "4 pm-6:59 pm", "7 pm-9:59 pm"] 
        converted = ["11am-1:30pm", "1:30pm-4pm", "4pm-7pm", "7pm-10pm"]

        if self.Time in values:  
            self.TimeCode = values.index(self.Time)
            self.Time = converted[self.TimeCode]

            if self.TimeCode <= 1:
                self.Shift = "LUNCH"
            else:
                self.Shift = "DINNER"

        # TODO: ADD PHANTOM SHIFT FUNCTIONALITY, HOW TO TEST FOR???

    def find_Type(self, file):
        check_index = None
        for index, line in enumerate(file):

            if line.find("Shop Type") != -1:
                check_index = index+1
                continue

            if index == check_index:
                self.Type = line.strip()
                return
            
    def find_Day(self, file):
        check_index = None
        for index, line in enumerate(file):

            if line.find("Shop Date") != -1:
                check_index = index+1
                continue

            if index == check_index:
                self.Day = line.split()[-1]
                return
            
    def find_Score(self, file):
        check_index = None
        for index, line in enumerate(file):
            if line.find("/100") != -1:
                self.Score = line.split("/")[0]
                return
            
    def find_Service_Score(self, file):
        check_index = None
        for index, line in enumerate(file):

            if line.find("Service") != -1:
                check_index = index+1
                continue

            if index == check_index:
                self.Score_Service = line.rstrip()
                return
            
    def find_Quality_Score(self, file):
        check_index = None
        for index, line in enumerate(file):

            if line.find("Quality") != -1:
                check_index = index+1
                continue

            if index == check_index:
                self.Score_Quality = line.rstrip()
                return
            
    def find_Clean_Score(self, file):
        check_index = None
        for index, line in enumerate(file):
            if line.find("Cleanliness") != -1:
                check_index = index+1
                continue

            if index == check_index:
                self.Score_Clean = line.rstrip()
                return
            
    def find_Satisfy_Score(self, file):
        check_index = None
        for index, line in enumerate(file):

            if line.find("Satisfaction") != -1:
                check_index = index+1
                continue

            if index == check_index:
                self.Score_Satisfaction = line.rstrip()
                return
            
    def find_Upsell(self, file):
        check_index = None
        for index, line in enumerate(file):

            if line.find("crew member offer") != -1:
                check_index = index+1
                continue

            if index == check_index:
                if line.find("Y") != -1:
                    self.Upsell = True
                    
                else:
                    self.Upsell = False
                return

    def find_Ticket_Time(self, file):
        check_index = None
        for index, line in enumerate(file):

            if line.find("How long") != -1:
                check_index = index+1
                continue

            if index == check_index:
                self.Ticket_Time = line.strip()

                self.Ticket_Min = int(self.Ticket_Time.split()[0][:-1]) + round(int(self.Ticket_Time.split()[1][:-1])/60,2)

                if self.Ticket_Min >= 10:
                    self.Large_Ticket_Time = False
                    self.Small_Ticket_Time = False
                    return
            
                self.Large_Ticket_Time = True                    

                if self.Ticket_Min >= 8:
                    self.Small_Ticket_Time = False              
                else:
                    self.Small_Ticket_Time = True
                return
                  
    def find_Fry_Quality(self, file):
        check_index = None
        for index, line in enumerate(file):

            if index == check_index:
                if line.find("20") != -1:
                    self.Fry_Quality = True
                    
                else:
                    self.Fry_Quanlity = False
                return     
            
            print(line)
             
            if line.find("quality of the fries") != -1 or line.find("quality of your fries") != -1:     
                check_index = index+2                
                continue


    def find_Fry_Quantity(self, file):
        check_index = None
        for index, line in enumerate(file):

            if line.find("31. Did the quantity") != -1:
                check_index = index+1
                continue

            if index == check_index:
                if line.find("Y") != -1:
                    self.Fry_Quantity = True
                    
                else:
                    self.Fry_Quantity = False
                return

    def find_Lobby_Clean(self, file):
        check_index = None
        for index, line in enumerate(file):

            if line.find("45. Was the dining") != -1:
                check_index = index+2
                continue

            if index == check_index:
                if line.find("Y") != -1:
                    self.Lobby_Clean = True
                    
                else:
                    self.Lobby_Clean = False
                return

    def find_Friendly(self, file):
        check_index = None
        for index, line in enumerate(file):

            if line.find("genuinely friendly") != -1:
                check_index = index+2
                continue

            if index == check_index:
                if line.find("Y") != -1:
                    self.Friendly_Greeting = True
                    
                else:
                    self.Friendly_Greeting = False
                return

    def find_Cashier(self, file):
        check_index = None
        for index, line in enumerate(file):

            if line.find("64. Cashier") != -1:
                check_index = index+1
                continue

            if index == check_index:
                self.Cashier = line.strip()
                return

    @staticmethod
    def run_all():
        list = ShopSurvey.get_all_files()
        
        for file in list:
            ShopSurvey.convert_pdf_to_text(file)

        list = ShopSurvey.get_all_files("./shop_txt")
        data = []

        for file in list:
            shop = ShopSurvey(file)
            data.append(shop)

        for shop in data:
            print(shop)
            print("\n*********************\n")
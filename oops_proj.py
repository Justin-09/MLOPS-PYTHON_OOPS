class chatbook:
    def __init__(self):
        self.name = "justin"
        self.password = "1234"
        self.loggedin = True
        if self.loggedin == True:
             self.menu()
       
        
    def menu(self):
        print("menu entered")
        userinput = input ("""Welcome to the chatbook
                        1.sign up
                        2.sign in
                        3.Post
                        4.Message a friend
                        5.Exit                     
                     """)   
        if userinput == "1":
            pass
        elif userinput == "2":
            pass
        elif userinput == "3":
            pass
        elif userinput == "4":
            pass
        else:
            exit()
            
obj = chatbook()

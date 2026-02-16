class chatbook:
    def __init__(self):
        self.name = "justin"
        self.password = "1234"
        self.loggedin = False
        # if self.loggedin == True:
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
            self.signUp()
        elif userinput == "2":
            self.signin()
        elif userinput == "3":
            pass
        elif userinput == "4":
            pass
        else:
            exit()
    
    def signUp(self):
        self.email = input("enter your email: ")
        self.pwd = input("enter your password: ")
        print("success")
        self.menu()
    
    def signin(self):
        if self.email == '' and self.pwd == '':
            print("Please sign up first by pressing 1")
        else :
            uname = input("please enter email")
            pwd = input("pwd please")
            if self.email == uname and self.pwd == pwd:
                print("u are SIGNED in")
                self.loggedin = True
        self.menu()
            
obj = chatbook()

    


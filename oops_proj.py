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
            self.post()
        elif userinput == "4":
            self.sendmessg()
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
    
    def post(self):
        if self.loggedin == True:
            self.txt = input("write a post")
            print(f"Your post: {self.txt}")
        else:
            print("please sign In")
        self.menu()
    
    def sendmessg(self):
        if self.loggedin == True:
            self.mssg = input("enter the message : ")
            self.frnd = input("enter the name of the friend you want to send the message to: ")
            self.frnd = input(f"the messg {self.mssg} has been sent to {self.frnd}")
        else:
            print("please sign in ")
        self.menu()
        
                    
chatbook()

    


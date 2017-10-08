# user has a username, full name and password
# user should be able to sign up using the details above

class SignUp:

    def __init__(self, full_name, username, password):
        self.username = username
        self.full_name = full_name
        self.password = password
        self.user_list = []

    def sign_up(self,user):

        self.user_list.append(user)

def add_user():
    name_ = input("Enter your full name: ")
    username_ = input("Enter your username: ")
    password_ = input("Enter a password: ")
    
    new_user = Twitter(name_,username_,password_)
    new_user.sign_up()
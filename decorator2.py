# 6.	Decorator:
# o	Create a decorator that checks if a function has a specific argument (user_type="admin") and prints "Access Granted" or "Access Denied".

def check_user_type(fun):
    def wrapper(a, b):
        if b.get("user_type") == "admin":
            print("Access Granted")
            return fun(a , b)
        else:
            print("Access Denied")
            return None
    return wrapper

@check_user_type
def dashbord(user_type):
    print("to the admit.")
    
dashbord(user_type="admin")
dashbord(user_type="abc")
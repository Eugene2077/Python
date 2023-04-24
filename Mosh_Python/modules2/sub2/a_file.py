
print("[module:a_file] is initialized", __name__) # name method(built in) returns the name of the module
# If you run this file directly, the __name__ method returns "__main__" instead of the real name
#so we can use this like this

if __name__ == "__main__":
    print("it is now using as a script")
    # here comes the codes you need when it is work as a script
    # this part will not run when it is used as a module
    # so this way, you can use the same file as a script as well as a module


def orange(num):
    print("here is Orange:",num)

from modules2.sub import sub_module
sub_module.message(10)



# filenotfound

try:
    file = open("afile.txt")
    a_dic = {"key":"Value"}
    print(a_dic["sdfasdf"])
# we have to mention which error we need to except otherwise will leave all the error
except FileNotFoundError:
    file = open("afile.txt", "w")
    file.write("Something")
# we use multiple except
# except KeyError:
#     print("This key not exist")
# how to catch the error
except KeyError as error:
    print(f"this is {error}")

# after try block executes the "else" block will open
else:
    content = file.read()
    print(content)
# finally will execute always
finally:
    file.close()
    print("The file was closed.")
    # raise keyword is used to raise your own error with messages also
    raise KeyError("This is an error that I made up of.")
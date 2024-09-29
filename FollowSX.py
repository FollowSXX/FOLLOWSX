import subprocess as s ,time as t ,importlib as i #line:1:import subprocess as s,time as t,importlib as i
try :#line:2:try:
    i .import_module ('importlib')#line:3:i.import_module('importlib')
except ImportError :#line:4:except ImportError:
    print ("\x1b[31mERROR: The 'importlib' library is not installed.")#line:5:print("\x1b[31mERROR: The 'importlib' library is not installed.")
    print ("Please install the 'importlib' library using the command:")#line:6:print("Please install the 'importlib' library using the command:")
    print ("pip install importlib")#line:7:print("pip install importlib")
    exit (1 )#line:8:exit(1)
try :#line:9:try:
    i .import_module ('subprocess')#line:10:i.import_module('subprocess')
except ImportError :#line:11:except ImportError:
    print ("\x1b[31mERROR: The 'subprocess' library is not installed.")#line:12:print("\x1b[31mERROR: The 'subprocess' library is not installed.")
    print ("Please install the 'subprocess' library using the command:")#line:13:print("Please install the 'subprocess' library using the command:")
    print ("pip install subprocess")#line:14:print("pip install subprocess")
    exit (1 )#line:15:exit(1)
try :#line:17:try:
    i .import_module ('time')#line:18:i.import_module('time')
except ImportError :#line:19:except ImportError:
    print ("\x1b[31mERROR: The 'time' library is not installed.")#line:20:print("\x1b[31mERROR: The 'time' library is not installed.")
    print ("Please install the 'time' library using the command:")#line:21:print("Please install the 'time' library using the command:")
    print ("pip install time")#line:22:print("pip install time")
    exit (1 )#line:23:exit(1)
a ="""\033[31m ███████████          ████  ████                            █████████  █████ █████\033[0m
\033[32m░░███░░░░░░█         ░░███ ░░███                           ███░░░░░███░░███ ░░███ \033[0m
\033[33m ░███   █ ░   ██████  ░███  ░███   ██████  █████ ███ █████░███    ░░░  ░░███ ███  \033[0m
\033[34m ░███████    ███░░███ ░███  ░███  ███░░███░░███ ░███░░███ ░░█████████   ░░█████   \033[0m
\033[35m ░███░░░█   ░███ ░███ ░███  ░███ ░███ ░███ ░███ ░███ ░███  ░░░░░░░░███   ███░███  \033[0m
\033[36m ░███  ░    ░███ ░███ ░███  ░███ ░███ ░███ ░░███████████   ███    ░███  ███ ░░███ \033[0m
\033[37m █████      ░░██████  █████ █████░░██████   ░░████░████   ░░█████████  █████ █████\033[0m
\033[0m░░░░░        ░░░░░░  ░░░░░ ░░░░░  ░░░░░░     ░░░░ ░░░░     ░░░░░░░░░  ░░░░░ ░░░░░ \033[0m"""#line:32:\033[0m░░░░░        ░░░░░░  ░░░░░ ░░░░░  ░░░░░░     ░░░░ ░░░░     ░░░░░░░░░  ░░░░░ ░░░░░ \033[0m"""
print (a )#line:34:print(a)
b =input ("Enter the Instagram URL: ")#line:36:b = input("Enter the Instagram URL: ")
while True :#line:38:while True:
    c =input ("Enter the number of followers (1K max) :")#line:39:c = input("Enter the number of followers (1K max) :")
    if c .isdigit ():#line:40:if c.isdigit():
        d =int (c )#line:41:d = int(c)
        break #line:42:break
    else :#line:43:else:
        print ("The number of followers must be an integer.")#line:44:print("The number of followers must be an integer.")
e =0 #line:46:e = 0
try :#line:48:try:
    while True :#line:49:while True:
        f =input ()#line:50:f = input()
        if f =="":#line:51:if f == "":
            e +=1 #line:52:e += 1
            if e ==2 :#line:53:if e == 2:
                print ("Loading...")#line:54:print("Loading...")
                s .run (["FollowsX.exe"])#line:55:s.run(["FollowsX.exe"])
                print ("Loading complete.")#line:56:print("Loading complete.")
                break #line:57:break
        else :#line:58:else:
            e =0 #line:59:e = 0
    print ("Thank you for using FollowSX. If you encounter any problems, I may be able to help. Contact me on Discord at '@rebug_termed'.")#line:61:print("Thank you for using FollowSX. If you encounter any problems, I may be able to help. Contact me on Discord at '@rebug_termed'.")
except KeyboardInterrupt :#line:62:except KeyboardInterrupt:
    pass #line:63:pass

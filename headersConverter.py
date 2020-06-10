import re
fileIn = "headers_in.txt"
fileOut = "headers_out.txt"

try:
    with open(f"./{fileIn}","r") as f:
        a = f.readlines()
except FileNotFoundError:
        open(f"./{fileIn}","w")
        print(f"{fileIn} has just generated! please retry")
        exit(0)

with open(f"./{fileOut}","w+") as f:
    p = re.compile("(.*?):(.*)")
    for index,val in enumerate(a):
        end=""
        if(index != len(a)-1):
            end=",\n"
        try:
            f.writelines("'" + p.search(val).group(1) + "':'"+p.search(val).group(2).strip()+"'"+end)
        except AttributeError:
            print("Invalid input, please check it again")
            exit(0)
    print(f"Convert finish! check {fileOut}")
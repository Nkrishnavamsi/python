import re
email=input=("enter the email id")
result=re.fullmatch("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+,email")

if result:
    print("vaild email id")""
else
    print("not vaild email id")
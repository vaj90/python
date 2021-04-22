# regular expressions
import re
def validate_email(email):
    if(re.search(r'\b[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b',email)):
        print("Valid email")
    else:
        print("Invalid email")

e1 = 'danil235@gmail.com'
validate_email(e1)
e2 = 'myemail.email.com'
validate_email(e2)
e3 = 'muemail@mu.email.ca.com'
validate_email(e3)
e4 = 'myemail()*@gmail.com'
validate_email(e4)
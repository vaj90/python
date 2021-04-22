# regular expressions
import re
str = "This cat has 9 Lives, Tom 99Jerry"
print(re.findall(r"[A-z][a-z]+", str))

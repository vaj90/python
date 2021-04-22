def discriminant(a,b,c):
    b_sqr = eval("{0}*{1}".format(b, b))
    ac_value = eval("4*{0}*{1}".format(a, c))
    discriminant_value = eval("{0}-{1}".format(b_sqr, ac_value))
    return discriminant_value


import math
a = 1
b = 5
c = 6
dis_value = discriminant(a, b, c)
sqrt_dis_value = math.sqrt(dis_value)
eq = "(-{0}+{1})/(2*{2})".format(b, sqrt_dis_value, a)
print(eq)
x1 = eval(eq)
print(x1)

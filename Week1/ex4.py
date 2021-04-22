#format output
print("The price is ${0:7.2f}".format(19.9));
print("The price is ${0:7.2f}".format(109.9));
print("The price is ${0:7.2f}".format(1009.9));

print("The price is ${val:7.2f}.".format(val=19.9))

shoes = 2
socks = 1.5

str1 = "I have {:d} pairs of shoes and " \
    "{:f} pairs of socks".format(shoes, socks)
print(str1)

str2 = "I have {0:d} pairs of shoes and "\
    "{1:f} pairs of socks".format(shoes, socks)
print(str2)


str3 = "I have {numShoes:d} pairs of shoes and " \
    "{numSocks:f} pairs of socks "\
    .format(numShoes=shoes, numSocks=socks)

print(str3)


str4 = "I have {0:1d} pairs of shoes and "\
    "{1:0.1f} pairs of socks".format(shoes, socks)
print(str4)

# with specifier
# functios ljust(), rjust(), center()

print("Left spacing".rjust(25))
print()
print("Left spacing".rjust(15, '*'))
print()
print("Left spacing".rjust(15), "Middle".ljust(10), "Right spacing".center(20));
print("Left spacing".rjust(15, '#'), "Middle".ljust(10, '|'), "Right spacing".center(20, '*'));

# error
# print("1". -1)

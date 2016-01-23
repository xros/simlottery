from lottery import RandomLottery

# Print 
print("""#### Lottery generator ####
nubmer amount: 6, number range: 1,49 (49 not included), unique: False, sort: True
""")
a=RandomLottery()
print(a.get_number_list())

print("""#### Lottery generator ####
nubmer amount: 4, number range: 1,6 (6 not included), unique: True, sort: False
""")
b=RandomLottery(4,(1,6),True,False)
print(b.get_number_list())

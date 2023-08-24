# output should be 555  457  234

area_code = int(input())
prefix = int(input())
line_number = int(input())
print("Country  Phone Number")
print("-------  ------------")
print("U.S.     +1 (",area_code,")",prefix, "-",line_number)
print("Brazil   +55(",area_code,")",prefix + 100, "-",line_number)
print("Croatia  +385(",area_code,")",prefix, "-",line_number + 50)
print("Egypt    +20(",area_code + 30,")",prefix, "-",line_number)
print("France   +33(",prefix,")",area_code, "-",line_number)
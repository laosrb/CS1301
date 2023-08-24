# prompt 
# Compute how many gallons of paint are needed to cover the given square feet of walls. 
# Assume 1 gallon can cover 350.0 square feet. So gallons = the square feet divided by 350.0. 
# If the input is 250.0, the output should be:
# 0.7142857142857143
# Note: Do not format the output.

wall_area = float(input())

# Assign gallons_paint below

gallons_paint = wall_area / 350

print(gallons_paint)
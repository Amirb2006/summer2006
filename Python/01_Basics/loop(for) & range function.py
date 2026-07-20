temperatures = [22.4, 25.1, 19.8, 24.2]


for i in range(len(temperatures)):
    # 1. Subtract 1.5 from the current element at index i and save it back
    temperatures[i] = temperatures[i] - 1.5 
# better way to do is to use -= 1.5 instead of  temperatures[i] - 1.5

# 2. Print the calibrated list

for i in range(len(temperatures)):
    print("Calibrated temperatures:", temperatures[i] )
#in python we can print a list just by below command

print("Calibrated temperatures:", temperatures)
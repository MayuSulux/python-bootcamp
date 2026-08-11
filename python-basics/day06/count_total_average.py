sales = [30,65,80,45,100]

count = 0
total = 0
avarage=0

for sale in sales:
    count = count +1
    total = total + sale

avarage = total/count

print("Number of Sale ",count)
print("Total sale ", total)
print ("Average sale", avarage)


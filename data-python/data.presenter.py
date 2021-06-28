import matplotlib.pyplot as plt
plt.plot(i)
plt.ylabel('')
plt.show()


fhand = open('CupcakeInvoices.csv')

total = 0
for i in fhand:
    # print(i)
    i = i.rstrip('/n').split(',')
    # print(round( float(i[3]) * float(i[4]), 2))
    total += round( float(i[3]) * float(i[4]), 2)

print(round(total, 2))
print(round(choco, 2))
print(round(vanilla, 2))
print(round(strawberry, 2))

types = ["choco", "vanilla", "strawberry"]
totals = [choco, vanilla, strawberry]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(types, totals)

plt.show()

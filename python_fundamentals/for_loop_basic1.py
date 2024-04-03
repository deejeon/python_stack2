for i in range(0,151):
    print(i)

for i in range(5,1000001):
    if i % 5 == 0:
        print(i)

for i in range(1,101):
    if i % 10 == 0: print("Coding Dojo")
    elif i % 5 == 0: print("Coding")
    else: print(i)

sum = 0
for i in range(0,500001):
    if i % 2 != 0:
        sum += i
print(sum)

current = 2018
while(current > 0):
    print(current)
    current -= 4

def countup(low,high,mult):
    counter = low
    while(counter <= high):
        if counter % mult == 0:
            print(counter)
        counter += 1

countup(2,9,3)

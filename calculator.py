def main():
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))
    largeNumber(x,y)

def square(n):
    return n*n

def largeNumber(n1,n2):
    if n1 > n2:
        print(f"{n1} is greater than {n2}")
    elif n2 > n1:
        print(f"{n2} is greater than {n1}")
    else:
        print(f"{n1} is equal to {n2}")

def loop():
    people = ["PrayGod", "Baraka", "Mndeme"]
    for _ in range(len(people)):
        print(people[_], end=" ")

loop()

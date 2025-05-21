capital= float(input("capital:"))
yadd= float(input("Yearly addition:"))
yret= float(input("Yearly  return:"))
ynum= int(input("How many years:"))
profit= int((capital*yret-capital)*yret+yadd)
n=ynum
number=profit
def repeated_multiplication(number, n):
    result = 1
    for _ in range(n):
        result *= number
    return result

print(capital*yret+repeated_multiplication(number,n))

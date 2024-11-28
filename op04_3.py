def  bank(amount, years):
    result = amount
    for i in range(years-1):
        result =  result * 1.1
        print(result)
    return result

a = int(input("Сумма : "))
b = int(input("Срок (лет) : "))
result = bank(a,b)
print("")
print("Мтого : " + '{:,.2f}'.format(result))
def karatsuba(num1,num2):
    if num1 < 10 and num2 < 10:
        return num1*num2
    else:
        if num1 > num2:
            divider = pow(10,len(str(num1)) / 2)
        else:
            divider = pow(10,len(str(num2)) / 2)
    a = num1 // divider
    b = num1 % divider
    c = num2 // divider
    d = num2 % divider
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    e = a+b
    f = c+d
    ef = karatsuba(e,f)
    return (ac*pow(divider,2) + bd + ((ef-bd-ac)*divider))

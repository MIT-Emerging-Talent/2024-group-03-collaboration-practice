#create function that takes two inputs that are numbers in form of strings (a,b)
def add_string_numbers(a,b):
#we will test if (a and b) is not a decimal number then we will transform them to numbers using int
    if "." not in a and "." not in b:
        num1= int(a)
        num2= int(b)
        ans= num1+ num2
#if (a or b) is a decimal we use float to get numbers and determine the number of decimal digits for each number to choose the biggest and use it to round answer and avoid error from using float
    else:
        dec1= len(a.split(".")[-1])
        dec2= len(b.split(".")[-1])
        decimalDigits= max(dec1, dec2)
        num1= float(a)
        num2= float(b)
        ans= round(num1+num2, decimalDigits)
#the answer will be returned as string    
    return str(ans)
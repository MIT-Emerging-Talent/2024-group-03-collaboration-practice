# Add string numbers
This is a Function that adds two numbers provided as string. It can be used if numbers are intigers or decimals.
## Description:
This function first test if either of input numbers are decimals (contain ".") if not then numbers can be taken using int() and add them, and if one of the numbers is decimal then first we use float to get the numbers. then, the function counts the highest number of decimal digits in the two inputs to round the addition answer and avoid error due to float usage.
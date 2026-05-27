import numpy as np

#Filtering is selecting elements from an array that match a given condition

ages = np.array([[21,17,19,20,16,30,18,65],
                [39,22,15,99,18,19,20,21]])
teenagers = ages[ages < 18]
#adults = ages[(ages >= 18) & (ages < 65)]   #in numpy you must use "&" instead of "and" for logical operators
                                            #and use "|" instead of "or"
#seniors = ages[ages >=65]
#even = ages[ages % 2 == 0]                  #The modulus operator "%" gives the remainder of any division
#odds = ages[ages % 2 != 0]                  #The operator "!=" means "not equal to"

#When using np.where, there are 3 arguments.
# np.where(condition,array,fill value)    fill value is the number that replaces the indexes that do not meet the condition
#People do this to maintain the array shape
adults = np.where(ages >= 18, ages,0)

#print(ages.shape)
#print(teenagers)
print(adults)
#print(seniors)
#print(even)
#print(odds)

#!/usr/bin/env python
# coding: utf-8

# 1. Suppose you invested in Bitcoin at the end of 2017 when Bitcoin gained a lot of value. What would be your money at the end of a week if you had invested \$1000 with an average daily increase of 12\% ? You can solve the problem using Python.
# 
#         ##### Help
# 
#         # Create a variable capital ($1000)
# 
#         # Create a variable for daily growth (12%)
# 
#         # Create a variable for period (7)
# 
#         # Calculate the final growth rate
# 
#         # Calculate result
# 
#         # Print result
# 
# 

# In[32]:


beginning_capital=1000
capital=beginning_capital
period=7
daily_growth=12
x=0
for x in range(0,period):
    capital=capital+capital*(daily_growth/100)
    x=x+1
total_earned=capital-beginning_capital
print("After one week, total earned money is", total_earned)
growth_rate=((capital-beginning_capital)*100)/1000
print("weekly growth rate is" ,growth_rate)


# 2. Print the text in quotes with Python. However, you must get the numbers from variables using `.format()` notation. <br> Because the text is long, you might consider writing in two lines:
# 
#         `"When we buy bitcoin with 1000 USD at the beginning of the week, we would earn 1210.68 USD at the end of the week, with an average gain of 12\%."`

# In[36]:


print("When we buy bitcoin with {} USD at the beginning of the week,we would earn {:.2f} USD at the end of the week, with an average gain of {}\%.".format(beginning_capital,total_earned,daily_growth))


# 3. Get the temperature in Fahrenheit from user and write a code to convert it to Celcius. For conversion, you can use this formula: C = (5/9) * (F - 32)
# 
#         Enter the temperature in Fahrenheit: 
#         user --> 26
#         output --> Temperature (C) : -3.33

# In[ ]:


f_temp=input("Enter the temprature in fahrenheit: ")
c_temp=(5/9)*(int(f_temp)-32)
print("Temperature (C): ", c_temp)


# 4. Get a three digit number the from user and calculate the sum of the digits in the integer.
# 
#         user --> 365
#         output --> "The sum of digits in the number is 14

# In[40]:


number=input('Enter a three digit number: ')
digit1=int(number[0])
digit2=int(number[1])
digit3=int(number[2])
print('The sum of digits in the number is ', digit1+digit2+digit3)


# 5. Write some code to calculate the hypotenuse of a right angled triangle. Get the side lengths from the user.
# 
#         user --> first side lenth : 6
#         user --> first side lenth : 8
#         output --> "The length of the hypotenuse is 10

# In[ ]:


first_side=input("Enter the first side length: ")
second_side=input("Enter the second side length: ")
hypotenuse=sqrt((int(first_side))**2+(int(second_side))**2)
print("The length of the hypotenuse is: ", hypotenuse)


# In[ ]:





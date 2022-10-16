# 1.Triple all the numbers given in list
# x=map(lambda i:i*3,(1,2,3,4,5,6))
# print("\nTriple all numbers:")
# print(list(x))








# 2. Separate even odd number from given list

# a=[]
# n=int(input("Enter number of elements:"))
# for i in range(int(n)):
#     b=int(input("Enter element:"))
#     a.append(b)
# even=[]
# odd=[]
# for j in a:
#     if(j%2==0):
#         even.append(j)
#     else:
#         odd.append(j)
# print("The even list",even)
# print("The odd list",odd)

# ------------------------------------------------------

# 3.Print all string in lower case from given tuple

# def example(s):
#     return s.lower()
    
# lower_name=('MEET','NEEL','MEHUL')
# update_name=map(example,lower_name)
# print(tuple(update_name))
# ------------------------------------------------------
# 4.Print square root of numbers given in list

# def example(i):
#     return i*i

# num=map(example,(5,10,20,30,40))
# print(list(num))
# ------------------------------------------------------


# 5.Eliminate duplicate letter from given string
# from collections import OrderedDict
#
#
# def remove_duplicate(str1):
#     return "".join(OrderedDict.fromkeys(str1))
#
#
# print(remove_duplicate("patel"))

# ------------------------------------------------------
# 6.Print table of any number 

# number = int(input ("enter the number of table "))            
# print ("The Multiplication Table of: ", number)    
# for count in range(1,11):      
#     print (number, 'x', count, '=', number * count)   

# ------------------------------------------------------
# 7.Add two list

# a=['meet','neel','mehul']
# b=['het','tax']
# a.extend(b)
# print(a)

# ------------------------------------------------------
# 8.Convert all float digits into integer using built in function from given list.

# def example(s):
#     s.integer()
    
# float_number=(12.3,13.5,14.5)
# update_number=map(example,float_number)
# print(list(update_number))


# num=12.3

# num1=int(num)
# print(num1)

# ----------------------------------------------------------------------------------------------------
# 9.Reverse given set

# list=[1,2,3,'a','b','c']
# list.reverse()
# print(list)


# ------------------------------------------------------------------
# 10.Add ‘@gmail.com’ to all the values of given dictionary and convert it to lower case.

# def example(s):
#     return s.upper()

# value_name=('@g', 'ma' ,'il','.c' , 'om')
# update_num=map(example,value_name)
# print(dict(update_num))

# --------------------------------------------------------------------------------------------------------------




# 1.using filter() function filter the list so that only negative numbers are left.

# list1=[-1,2,4,-5,6,-13,12,22,-14,-18,20,3]
# list2=list(filter(lambda x:x>0,list1))
# print(list2)



# 2.using filter function filter the even numbers so that only odd numbers are passed to the new list

# list1=[1,2,3,4,5,11,12,13,14,15,21,22,23,24,25,31,32,33,34,35]
# print(list1)
# list2=list(filter(lambda x:x%2!=0,list1))
# print(list2)



# 3.using filter() and list() functions and .lower() method filter all the vowels in a given string

# str="When you have a dream, you've got to grab it and never let go."
# list1 = list(filter(lambda x: True if x.lower() in "aeiou" else False, str))
# print(list1)



# 4.This time using filter() and list() functions filter all the positive integers in the string.

# str="William Faulkner's Absalom, Absalom! (1936) contains a sentence composed of 1,288 words (in the 1951 Random House version)."
# list1 = list(filter(lambda x: True if x in "0123456789" else False, str))
# print(list1)



# 5.Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive to the new list.

# list1=[10,-20,-30,-40,50,-60,-80,90,70,100,-120,-130,-140]
# list2 = list(filter(lambda x: True if x>0 else False, map(lambda x: x*-1, list1)))
# print(list2)


# ------------------------------------------------------------------------------------------------------------------

from tkinter import*
import tkinter
import random


root=Tk()


logo1=tkinter.PhotoImage(file="1.png")
logo2=tkinter.PhotoImage(file="2.png")
logo3=tkinter.PhotoImage(file="3.png")
logo4=tkinter.PhotoImage(file="4.png")
logo5=tkinter.PhotoImage(file="5.png")
logo6=tkinter.PhotoImage(file="6.png")

w1=Label(root,image=logo1).grid(row=3,column=3,padx=600,pady=150)

def roll():
    x=[logo1,logo2,logo3,logo4,logo5,logo6]
    r=random.choice(x)
    w1=Label(root,image=r).grid(row=3,column=3,padx=600,pady=150)

b1=Button(root,text="--Click me--",command=roll)
b1.grid(row=4,column=3)

root.mainloop()
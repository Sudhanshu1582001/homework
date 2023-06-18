#!/usr/bin/env python
# coding: utf-8

# In[26]:


# Q1 we use def keyword to create a function


def odd_no(x):
    for i in x:
        if i%2!=0:
            print(i)
            
        
    


# In[28]:


x = range(1,25)


# In[29]:


odd_no(x)


# In[44]:


#Q2 *arwgs allows us to put arbitary number of arugments and take them as tuple of value and insted of creating tuple values ** kwargs build dictionary of keys/values pair
def even_no(*args):
    for i in args:
        if i%2==0:
            print(i) 
            
            


# In[45]:


even_no(1,2,3,4,5,6)


# In[47]:


def fruits_n(**kwargs):
    return kwargs


# In[49]:


fruits_n(a='apple',b='banana',c='cheeri')


# In[1]:


#Q3 itrators are those data in which we can itirate like list,tuples. we use iter() to initialise the itrator objects and the use for itration is next()
l=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
def list_n(l):
    for i in l:
        yield l


# In[3]:


t = iter(l)


# In[4]:


next(t)


# In[5]:


next(t)


# In[6]:


next(t)


# In[7]:


next(t)


# In[8]:


next(t)


# In[9]:


#Q4 Generators allow us to generate as we go along, instead of holding everything in memory. yield keyword is used to covert the the object to genrator.
def gencubes(n):
    for num in range(n):
        yield num**3


# In[10]:


for x in gencubes(10):
    print(x)


# In[14]:


#Q5 
def isPrime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
        return True


def primegenerator(n):
    num=2
    while n:
        if isPrime(num):
            yield num
            n-=1
            num+=1
        return       
    


# In[16]:


#Q6
n= int(input())
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci series is: ", end = " ")
while(count <= n):
  count += 1
  print(a, end=" ")
  a = b
  b = sum
  sum = a + b


# In[3]:


#Q7
a = [i for i in 'pwskills']

    


# In[4]:


a


# In[5]:


#Q8
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")


# In[10]:


lst = [x for x in range(100) if x%2!=0]


# In[11]:


lst


# In[ ]:





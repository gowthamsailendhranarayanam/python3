#!/usr/bin/env python
# coding: utf-8

# In[7]:


def isprime(n):
    flag = True
    for i in range(2,n//2+1):
        if n%i ==0:
            flag = False
            return flag
    return flag
isprime(11)


# In[11]:


#function to find prome numbers from 1 to n
def Primecount(n):
    cnt = 0
    for a in range(2,n+1):
        K=0
        for i in range(2,a//2+1):
            if a%i == 0:
                K = K+1
        if(K<=0):
                    cnt = cnt+1
    return cnt
Primecount(10)                


# In[12]:


def div(a):
    if(a%2 == 0 and a%3 == 0 and (a%4)!= 0):
        print("a is divisble:")
    else:
        print("a is not divisble")
    
    
div(6)


# In[ ]:





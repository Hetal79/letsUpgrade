#!/usr/bin/env python
# coding: utf-8

# # Day 3 Assignment
# 

# ## Question 1
# ### You all are pilots, You want to land a plan safely, so altitude required for landing a plane is 1000ft. If it is less than that tell the pilot land the palne, or it is more than that and less than 5000ft ask the pilot to " come down the plane", else if it is more than 5000ft ask the pilot "turn around and try later" .

# In[ ]:



#altitude must be 1000 or grater than that
altitude = int(input())
if altitude > 1000:
    if altitude == 1000:
        print('safe land')
    elif altitude > 1000 and altitude<5000:
        print('Bring down to 1000f')
    else:
        print('turn around')
else:
    print("oops !...... Wrong input. altitude must be grater than 1000..")


# ## Question 2

# ### Using for loop print prime number between 1 to 200 using for loop and range function

# In[5]:


#printing prime numbers
#num = int(input())
print("Prime Numbers Between 1 to 200 are as following")
                
for num in range (1,200):

    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
                print(num)
    else:
       pass


# In[ ]:





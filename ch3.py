#!/usr/bin/env python
# coding: utf-8

# In[1]:


thistuple = ["diary","book","pen","pencil"]
print(thistuple)

# create a tuple
thistuple = ("diary","book","pen","pencil")
#convert the tuple into a list
thislis = list(thistuple)
thislis.pop(0) #removing the first item
thislis.pop(-1) # removing the last item

# converting the list back to a tuple
thistuple = tuple(thislis)

# printing the new tuple
print(thistuple) 



# In[9]:


print(thistuple[0:2])


# In[16]:


thisdict = {"brand":"vitamin","year":2020,"color":"green"}
print(thisdict)


# In[2]:


list1 = [5, 20, 15, 20, 25, 50, 20]

def removeValue(sampleList, val):
   return [value for value in sampleList if value != val]
resList = removeValue(list1, 20)
print(resList)


# In[14]:


A = [1,2,3,4,8,10,12,13,15,17]
Evenlist = []   # create an empty list
oddlist = []    # create an odd list
for i in A:
    if i%2 == 0:
        Evenlist.append(i)
    else :
        oddlist.append(i)
print ("Even numbers", Evenlist)
print ("odd numbers", oddlist)


# In[ ]:





# In[ ]:





# In[ ]:





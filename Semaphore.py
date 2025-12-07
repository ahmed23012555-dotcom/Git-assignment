#!/usr/bin/env python
# coding: utf-8

# In[1]:


import threading
import time


# In[2]:


examinationroom = threading.Semaphore(1)


# In[3]:


def enter_examinationroom(num):
    global examinationroom
    print(f"Patient {num} is waiting for his turn\n")
    
    examinationroom.acquire()
    print(f"Patient {num} is in the examination room\n")
    
    time.sleep(2)
    
    print(f"Patient {num} has left the examination room\n")
    examinationroom.release()
patient = []
for i in range(10):
    t = threading.Thread(target=enter_examinationroom,args=(i,))
    patient.append(t)
    t.start()
    
for t in patient:
    t.join()


# In[ ]:




#checked the code

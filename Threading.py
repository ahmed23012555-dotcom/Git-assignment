#!/usr/bin/env python
# coding: utf-8

# In[5]:


import threading
import time


# In[6]:


def print_1():
    print("starting of a thread:",threading.current_thread().name)
    time.sleep(0.02)
    print("Finishing of a thread:",threading.current_thread().name)
    
def print_2():
    print("starting of a thread:",threading.current_thread().name)
    print("Finishing of a thread:",threading.current_thread().name)
a = threading.Thread(target=print_1,name="Thread-1")
b = threading.Thread(target=print_2,name="Thread-2")
a.start()
b.start()


# In[ ]:




#checked the code
# Final completion commit

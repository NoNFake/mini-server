import random as rnd
import sys
from enum import Enum


class Memmory(Enum):
    stik = "first" 
    sti = "firs" 
    stk = "firt" 
    sik = "fist" 
    tik = "frst" 

# size = sys.getsizeof(Memmory.stik.value)
# size_kb = size / 1024


# print(f"Size: {size_kb} ")


for i in Memmory:
    print(i)

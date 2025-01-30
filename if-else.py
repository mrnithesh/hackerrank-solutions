#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    #elif ladder
    if (n%2==0 and 2<=n<=5):
        print("Not Weird")
    elif (n%2==0 and 6<=n<=20):
        print("Weird")
    elif (n%2==0 and n>20):
        print("Not Weird")
    else:
        print("Weird")
    
    #single if else
    if n%2==1 or 6<=n<=20:
        print("Weird")
    else:
        print("Not Weird")
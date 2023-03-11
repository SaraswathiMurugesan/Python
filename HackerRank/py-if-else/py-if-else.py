#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if ((n % 2) == 0) and (n==range(2, 5)):
        print('Not Weird')
    elif((n % 2) == 0) and (n==range(6, 20)):
        print('Not weird')
    elif((n % 2) == 0) and (n>20):
        print('Not Weird')
    else:
        print('Weird')

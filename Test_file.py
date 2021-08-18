# importing the module
import re
import itertools
from collections import *
import os

# declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
 
# initializing the list object
lst=[]
dst=[]
my_dict={}
sd_dict={}
# opening and reading the file
with open('logfile') as fh:
   fstring = fh.readlines()
 
# function to get unique values
def unique(list1):
     
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    for x in unique_list:
        dst.append(x)

# function to count occurences of unique values        
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


# extracting the IP addresses
for line in fstring:
   lst.append(pattern.search(line)[0])

# finding unique IPs
unique(lst)

#counting occurences of unique IPs
for x in dst:
    a = countX(lst, x)
    my_dict[a] = x


#sorting dictionary
for i in sorted (my_dict.keys()) :
    sd_dict[i] = my_dict[i]

# Printing first N items in dictionary 
out = dict(itertools.islice(sd_dict.items(), 8)) 
for i in sorted (out.keys()) :
    print(out[i], i)

input()
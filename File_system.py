import os
from numpy import *

f=input("Enter a file name:") 
w=input("Enter word without space:")
while (True):
#checking if file with the name exit or not
    if not os.path.isfile(f):#if file name doesn't exit , create new file
        with open(f,'a') as l:
            l.write("\n {}".format(w))
            print("Success")
        break
    else: # if file exist then action performed
        with open(f,'r') as l:
            for line in l:
                if w in line:
                    #creating file with random name
                    k="" #variable having random name of file
                    for i in range(5):
                        j=chr(random.randint(97,123))
                        k+=j
                    with open(k,'a') as l:
                        l.write("\n {}".format(w))
                    print("Your file name is:",k)
                    break
            else:
                with open(f,'a') as l:
                    l.write('\n{}'.format(w))
                    print("Success")
 
        break
    

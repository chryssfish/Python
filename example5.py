import sys
import random
import os

sum = 0
flag = True
print("Σημείωση: Πρέπει ο m > n")
print("Εισάγετε τον αριθμό n")
n = int(input())
print("Εισάγετε τον αριθμό m")
m = int(input())

while (n<m):
    sum = sum + n
    n = n + n
print ("Το άθροισμα των πολλαπλάσιων είναι", sum)
# Author: Song Zhirui zjs5301@psu.edu
# Collaborator: Jack Hillman jsh5719@psu.edu
# Collaborator:  Shrey Hillman sxs6588@psu.edu
# Collaborator: Alexandros Condeelis afc5865@psu.edu
# Section:5

def digit_sum(n):
  if n<10:
    return n
  else:
    return n%10+digit_sum(n//10)

def run():
  n = input ("Enter an int: ")
  n = int(n)
  n1 = digit_sum(n)
  print(f"sum of digits of {n} is {n1}.")

if __name__=="__main__":
    run()
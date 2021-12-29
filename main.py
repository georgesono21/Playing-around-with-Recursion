def search(the_list,target):
  if len(the_list) == 1:
    return False
  if the_list[0] == target:
    return True
  else:
    the_list.pop(0)
    return search(the_list,target)

def binary_search_recurse(the_list,target,counter = 1):
  if len(the_list) == 1 and the_list[0] != target:
    return False
  midpoint = len(the_list)//2
  if target < the_list[midpoint]:
    left = 0
    right = midpoint
    return binary_search_recurse(the_list[left:right],target,counter+1)
  elif target > the_list[midpoint]:
    left = midpoint
    right = len(the_list)
    return binary_search_recurse(the_list[left:right],target,counter+1)
  elif target == the_list[midpoint]:
    print(counter)
    return True
  else:
    return True
    
print(binary_search_recurse([1,2,3,4,5,6,7,8,9,10,11,12],2))

def fib_recurse(n):
  if n <= 2:
    return 1 
  else:
    return fib_recurse(n-1) + fib_recurse(n-2)

def fib_loop(n):
  fib_minus_1, fib_minus_2 = 1,0
  for x in range(n):
    fib = fib_minus_1 + fib_minus_2
    fib_minus_2 = fib_minus_1
    fib_minus_1 = fib

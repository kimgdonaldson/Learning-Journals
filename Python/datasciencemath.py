import math
import numpy

def mean(set):
  total = 0
  for i in set: 
    total += i
  return total / len(set)

def mean_center(set):
  centered_set = []
  m = mean(set)
  for j in set:
    centered_set.append(j - m)
  return centered_set

def variance(set):
  total = 0
  muse = mean(set)
  for x in set:
    total += (x - muse) ** 2
  return math.sqrt(total / len(set))

def distance_formula(x1, y1, x2, y2):
  a = (x2 - x1) ** 2
  b = (y2 - y1) ** 2
  c = math.sqrt(a +b)
  return c

def slope_formula(p1,p2):
  print("{} - {} / {} - {}".format(p2[1], p1[1], p2[0], p1[0]))
  return (p2[1] - p1[1]) / (p2[0] - p1[0])

def npr(n):
  return numpy.math.factorial(n)

def combinations(n, s):
  return npr(s) / (npr(s-n) * npr(n))

def permutations(n, s):
  return npr(s) / npr(s-n) 

def esperado(set):
  total = 0
  c = 0
  for x in set:
    total = total + (c * x)
    c +=1 
  return total  

example = [.03, .07, .13, .17, .17, .2, .07, .07, .03, .03, .03]

print("The Esperado of example set is {}".format(esperado(example)))

print("The number of combinations possible for 4 elements of size 10 = {}".format(combinations(4,10)))
print("The number of permutations possible for 4 elements of size 10 = {}".format(permutations(4,10)))
print("NPR of 4 = {}".format(npr(4)))
point1 = [1,2]
point2 = [3,3]

print("Slope between point1 and point2: {}".format(slope_formula(point1, point2)))

print("Distance between (1,1) and (5,4) = {}".format(distance_formula(1,1,5,4)))

w = [5,6,7]
z = [1,5,12]

print("Mean: {}".format(mean(w)))
print("Mean Centered: {}".format(mean_center(w)))
print("Variance: {}".format(variance(w)))
print("")
print("Mean: {}".format(mean(z)))
print("Mean Centered: {}".format(mean_center(z)))
print("Variance: {}".format(variance(z)))
print("")

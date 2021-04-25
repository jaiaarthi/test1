from functools import reduce
lst=[2,3,4,5,6,7,8,9,10]
#filter with lambda
even= list(filter(lambda n:n%2==0,lst))
print(even)
#map with lambda
doubles=list(map(lambda n:n*2,even))
print(doubles)
#for reduce we have to import functools
#sum of numbers
sum=reduce(lambda a,b:a+b,doubles)
print(sum)
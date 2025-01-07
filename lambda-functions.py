p = [(3, 3), (4, 2), (2, 2), (5, 2), (1, 7)] 

q = sorted(p, key=lambda x: x[0]*x[1]) 
print(q) # [(2, 2), (1, 7), (4, 2), (3, 3), (5, 2)] 

#In-place calling
a = (lambda x: x + 1)(3) 
print (a)


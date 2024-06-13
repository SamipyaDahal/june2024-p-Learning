

def get_second_element(x): # (1,12) 12 1 10 0
    return x[1]

a.sort(key=get_second_element)
print(a) # [(3,0), (4,1), (12,10), (1, 12)]

data = [(1,2,3), (3,1,14), (1,1), (5,2,0)]

#sort the above list based on last item of the each tuple


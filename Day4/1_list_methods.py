



data = [(1,2,3), (3,1,14), (1,1), (5,2,0)]

#sort the above list based on last item of the each tuple

def get_last_element(x):
    return x[-1]

data.sort(key=get_last_element)
print(data) # [(5,2,0), (1,1), (1,2,12), (3,1,14)]

data.sort(key=get_last_element,reverse=True)
print(data) # [(3,1,14), (1,2,12), (1,1), (5,2,0)]

# reverse()
    

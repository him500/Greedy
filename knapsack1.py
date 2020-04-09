# value weight dictionary
cost = {60:10, 100:20, 120:30}
temp={}
def maxval(weight):
    key=(weight)
    if key in temp:
        return temp[key]

    if weight<=0:
        return 0
    max_val=0
    for vals in cost:
        w=cost[vals]
        if w>weight:
            continue

        value=maxval(weight-cost[vals])+vals
        if value>max_val:
            max_val=value
    
    temp[key]=max_val

    return max_val

print("max value carried in backpack ",maxval(50))
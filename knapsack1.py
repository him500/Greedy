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

# weight volume calories
table2=[[240,400,900],[135,400,650],[2800,1500,5000],
          [410,410,950],[182,190,95]]
cash={}
def maxCAL(weight,volume):
    key=(weight,volume)

    if key in cash:
        return cash[key]

    if weight==volume==0:
        return 0
    elif weight<=0 or volume<=0:
        return 0
   
    m=0
    for row in table2:
        if row[0]<=weight and row[1]<=volume:
            cal=maxCAL(weight-row[0],volume-row[1])+row[-1]
            m=max(m,cal)
    cash[key]=m
    return m

r=maxCAL(9500,5500)
print(r)
# print(cash)
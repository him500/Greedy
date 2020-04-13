# weight val table
table=[[5,1],
        [6,3],
        [8,5],
        [5,3]]

def maxVAL(k,u):
    if k==u==0:
        return 0
    elif k==0 and u!=0:
        return -1*float("Inf")
    else:
        m=0
        for row in table:
            if row[0]<u:
                m=max(m,max(maxVAL(k-1,u),maxVAL(k-1,u-row[0])+row[1]))
        return m

print(maxVAL(len(table),12))

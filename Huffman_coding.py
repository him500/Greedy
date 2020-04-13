

class Node:
    def __init__(self,k,v):
        self.key=k
        self.data=v
        self.left=self.right=None

class Huffman_tree:
    def __init__(self,s):
        unique={}
        self.root=None
        for i in range(len(s)):
            if s[i] in unique:
                unique[s[i]]+=1
            elif s[i] not in unique:
                unique[s[i]]=1

        for k,v in sorted(unique.items(),key=lambda item:item[1]):
            self.insert(k,v)
            print(k,v, end =" ")
        del unique

    def insert(self,key,val):
        if self.root==None:
            self.root=Node(key,val)
        else:
            tree=self.root

            self.root=Node(-1,tree.data+val)
            self.root.right=tree
            self.root.left=Node(key,val)
    def printLevelOrder(self): 
        if self.root is None: 
            return
        queue = [] 
        queue.append(self.root) 
    
        while(len(queue) > 0): 
            print ((queue[0].data,queue[0].key)) 
            node = queue.pop(0) 
    
            if node.left is not None: 
                queue.append(node.left) 
    
            if node.right is not None: 
                queue.append(node.right) 
    def return_root(self):
        return self.root

def generate_code(root,key,code=""):
    if root:
        if root.key==key:
            print(code)
            return
        else:
            generate_code(root.left,key,code+str(0))
            generate_code(root.right,key,code+str(1))


s=input()
# s="AABACDACA"
root=Huffman_tree(s)
print()
root.printLevelOrder()
tree=root.return_root()

unique=[]
for i in range(len(s)):
    if s[i] not in unique:
        unique.append(s[i])

for un in unique:
    print(un,end=" ")
    generate_code(tree,un)

    
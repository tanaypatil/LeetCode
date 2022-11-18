#User function Template for python3
from collections import deque, defaultdict


class Solution:
    def minTime(self, root,t):
        # code here
        if not root:
            return 0
            
        parentMap = {root: None}
        
        q = deque()
        q.append(root)
        target = None
        
        while q:
            node = q.popleft()
            if node.data == t:
                target = node
            if node.left:
                parentMap[node.left] = node
                q.append(node.left)
            if node.right:
                parentMap[node.right] = node
                q.append(node.right)
                
        q = deque()
        q.append(target)
        visited = defaultdict(bool)
        c = -1
        while q:
            # t = []
            for _ in range(len(q)):
                node = q.popleft()
                if not visited[node]:
                    visited[node] = True
                    if node.left:
                        q.append(node.left)
                        # t.append(node.left.data)
                    if node.right:
                        q.append(node.right)
                        # t.append(node.right.data)
                    if parentMap[node]:
                        q.append(parentMap[node])
                        # t.append(parentMap[node].data)
            if not q: break
            c += 1
            # print(c, t)
            
        return c if c != -1 else 0



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends
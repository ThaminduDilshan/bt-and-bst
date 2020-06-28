class BTNode:
    def __init__(self, val):
        self.lChild = None
        self.rChild = None
        self.value = val

    def	AddLeftChild (self, NewValue):
        if(self.lChild != None):
            return -1
        self.lChild = BTNode(NewValue)
        return 1

    def	AddRightChild (self, NewValue):
        if(self.rChild != None):
            return -1
        self.rChild = BTNode(NewValue)
        return 1

    def GetLeftChild (self):
        return self.lChild

    def GetRightChild (self):
        return self.rChild

class BinaryTree(object):
    def __init__(self):
        self.root = None

    @staticmethod
    def CreateBinaryTree (ElementList):
        tree=BinaryTree()                                               ##create a new tree
        tree.root=BTNode(ElementList[0])                                ##set first element as the root
        lastRow=[tree.root]                                             ##track the lastly added row by lastRow
        level=1                                                         ##variable for the level
        index=1                                                         ##variable for the index in ElementList
        
        while(True):
            currentRow=[]                                               ##variable for track the row which is currently adding
            temp=[]                                                     ##temporarily track the added nodes
            try:
                for j in range( index,index+(2**level) ):               ##track the row which is currently adding
                    currentRow.append(ElementList[j])
            except Exception:                                           ##ArrayIndex exception throws if the current level doesn't contain all possible nodes
                return null
            finally:
                added=0                                                 ##track the number of added nodes
                nodeID=0                                                ##track the node index, which needed to be added
                for i in range( len(lastRow) ):                         ##iterate through parent nodes
                    for j in range(2):                                  ##iterate through child nodes
                        if(lastRow[i].lChild==None):                    ##adding a left child
                            lastRow[i].AddLeftChild( currentRow[nodeID] )
                            temp.append( lastRow[i].GetLeftChild() )
                            added+=1
                            index+=1
                            nodeID+=1
                        elif(lastRow[i].rChild==None):                  ##adding a right child
                            lastRow[i].AddRightChild( currentRow[nodeID] )
                            temp.append( lastRow[i].GetRightChild() )
                            added+=1
                            index+=1
                            nodeID+=1
                        if(added==len(currentRow)):                     ##if all nodes in the current level are added, break inner
                            break
                    if(added==len(currentRow)):                         ##if all nodes in the current level are added, break outer
                        break
                        
                            
                level+=1                                                ##increase level
                lastRow = temp
                if(currentRow[-1]==ElementList[-1]):                    ##when all elements are added, break the while loop
                    break
            
        return tree

    def ExpandBinaryTree (self, NewElementList):
        level=0
        node=self.root
        while( node.GetLeftChild()!=None ):
            level+=1
            node=node.GetLeftChild()
        
        queue=[]                                                        ##queue for nodes which is not completed
        queue.append(self.root)                                         ##add the root to the queue
        for i in range( 2*level ):
            if( queue[0].GetLeftChild()!=None and queue[0].GetRightChild()!=None ):     ##append left and right childs to the queue if the node has both
                queue.append( queue[0].GetLeftChild() )
                queue.append( queue[0].GetRightChild() )
                queue.pop(0)                                            ##and remove node from the queue
            
        for i in range( len(NewElementList) ):                          ##adding new elements
            if(queue[0].GetLeftChild()==None):                          ##if first element in queue hasn't left child
                queue[0].AddLeftChild(NewElementList[i])                ##add left child
            elif(queue[0].GetRightChild()==None):                       ####if first element in queue hasn't right child
                queue[0].AddRightChild(NewElementList[i])               ##add right child
                queue.append(queue[0].GetLeftChild())
                queue.append(queue[0].GetRightChild())
                queue.pop(0)                                            ##append left and right childs to queue and remove parent node
        
        return self

    def TraverseInOrder(self,root):                                     ##left,node,right
        node=root                                                       ##set the current tree root as the node
        if(node.GetLeftChild()==None):                                  ##if node hasn't a left child print node
            print node.value,
        else:                                                           ##if node has a left child
            self.TraverseInOrder( node.GetLeftChild() )                 ##call Traverse for left sub tree
            print node.value,                                           ##print node after traversing left sub tree
            if(node.GetRightChild()!=None):                             
                self.TraverseInOrder( node.GetRightChild() )            ##call Traverse for right sub tree, if it has

        return None

    def TraversePreOrder(self,root):                                    ##node,left,right
        node=root                                                       ##set the current tree root as the node
        print node.value,                                               ##print node
        if(node.GetLeftChild()!=None):                                  ##if node has a left child, call Traverse for left sub tree
            self.TraversePreOrder( node.GetLeftChild() )
        if(node.GetRightChild()!=None):                                 ##if node has a right child, call Traverse for right sub tree
                self.TraversePreOrder( node.GetRightChild() )

        return None

    def TraversePostOrder(self,root):                                   ##left,right,node
        node=root                                                       ##set the current tree root as the node
        if(node.GetLeftChild()!=None):                                  ##if node has a left child, call Traverse for left sub tree
            self.TraversePostOrder( node.GetLeftChild() )
        if(node.GetRightChild()!=None):                                 ##if node has a right child, call Traverse for right sub tree
            self.TraversePostOrder( node.GetRightChild() )
        print node.value,                                               ##print node after traversing left and right sub trees
        
        return None

from bt import BinaryTree
from bt import BTNode
import copy


class BSTree(BinaryTree):
    def __init__(self):
        super(self.__class__, self).__init__()

    def AddValue (self, NewValue):
        if(self.root==None):                                                ##set first value as the root
            self.root=BTNode(NewValue)
            return 1
        else:
            node=self.root                                                  ##set root as the node at starting
            while(True):
                if( NewValue==node.value ):                                 ##if value already exists in the tree
                    return -1
                elif( NewValue<node.value ):                                ##if value less than node
                    if( node.GetLeftChild()==None ):                        ##set as left child if it empty
                        node.AddLeftChild(NewValue)
                        return 1
                    else:                                                   ##set left child as the node
                        node=node.GetLeftChild()
                else:                                                       ##if value greater than node
                    if( node.GetRightChild()==None ):                       ##set as right child if it empty
                        node.AddRightChild(NewValue)
                        return 1
                    else:                                                   ##set right child as the node
                        node=node.GetRightChild()
        

    def DeleteValue (self, DelValue):
        prevNode=None
        child=0
        node=self.root                                                      ##set root as the node at starting
        while(True):
            if( DelValue==node.value ):                                     ##select the node which is needed to delete
                break
            elif( DelValue<node.value ):                                    ##search in left sub tree
                if( node.GetLeftChild()==None ):                            ##value not in tree
                    return None
                prevNode=node
                child=-1        ##left child
                node=node.GetLeftChild()                                    ##set left child as the node
            else:                                                           ##search in right sub tree
                if( node.GetRightChild()==None ):                           ##value not in tree
                    return None
                prevNode=node
                child=1         ##right child
                node=node.GetRightChild()                                   ##set right child as the node

        if( node.GetLeftChild()==None and node.GetRightChild()==None ):     ##delete node is a leaf node
            if(child==-1):                                                  ##parent's left child
                prevNode.lChild=None
                return node
            if(child==1):                                                   ##parent's right child
                prevNode.rChild=None
                return node
        elif( node.GetLeftChild()!=None and node.GetRightChild()==None ):   ##delete node has only a left child
            if(child==-1):                                                  ##parent's left child
                prevNode.lChild=node.GetLeftChild()
                node.lChild=None
                return node
            if(child==1):                                                   ##parent's right child
                prevNode.rChild=node.GetLeftChild()
                node.lChild=None
                return node
        elif( node.GetLeftChild()==None and node.GetRightChild()!=None ):   ##delete node has only a right child
            if(child==-1):                                                  ##parent's left child
                prevNode.lChild=node.GetRightChild()
                node.rChild=None
                return node
            if(child==1):                                                   ##parent's right child
                prevNode.rChild=node.GetRightChild()
                node.rChild=None
                return node
        else:                                                               ##delete node has both left and right child
            parentEx=node                                                   ##exchange node's parent
            exNode=node.GetLeftChild()                                      ##exchange node
            while(exNode.GetRightChild()!=None):                            ##go to left sub tree and get right most node
                parentEx=exNode
                exNode=exNode.GetRightChild()
            
            if( exNode.GetLeftChild()==None ):                              ##exchange node is a leaf
                temp=copy.deepcopy(node)                                    ##copy a instance of node to temp
                parentEx.rChild=None
                node.value=exNode.value
                temp.lChild=None
                temp.rChild=None
                return temp
            elif( parentEx.value!=node.value ):                             ##exchange node has a left child and parent is not the deleting node
                temp=copy.deepcopy(node)                                    ##copy a instance of node to temp
                parentEx.rChild=exNode.GetLeftChild()
                node.value=exNode.value
                temp.lChild=None
                temp.rChild=None
                return temp
            else:                                                           ##exchange node has a left child and parent is the deleting node
                temp=copy.deepcopy(node)                                    ##copy a instance of node to temp
                parentEx.lChild=exNode.GetLeftChild()
                node.value=exNode.value
                temp.lChild=None
                temp.rChild=None
                return temp

            

    def SearchValue (self, SearchValue):
        node=self.root                                                      ##set root as the node at starting
        while(True):
            if( SearchValue==node.value ):                                  ##if value exists, return node
                return node
            elif( SearchValue<node.value ):                                 ##if value less than node
                if( node.GetLeftChild()==None ):                            ##return None if the left child is empty
                    return None
                node=node.GetLeftChild()                                    ##set left child as the node
            else:                                                           ##if value greater than node
                if( node.GetRightChild()==None ):                           ##return None if the right child is empty
                    return None
                node=node.GetRightChild()                                   ##set right child as the node

    def PrintTree (self):
        tempTree=copy.deepcopy(self)                                        ##get a copy of tree
        queue=[]                                                            ##queue for left sub tree of the root in sorted order
        stack=[]                                                            ##stack for right sub tree of the root in sorted order
        if(tempTree.root.GetLeftChild()!=None):                             ##if the root has a left child
            while(True):
                node=tempTree.root
                while( node.GetLeftChild()!=None ):                         ##get the left most node
                    node=node.GetLeftChild()
                queue.append(node.value)                                    ##add to queue (smallest element)
                tempTree.DeleteValue(node.value)                            ##delete the left most node from the Temp tree
                if( tempTree.root.GetLeftChild()==None ):                   ##break if all left sub tree values are added to the queue
                    break
        queue.append(tempTree.root.value)                                   ##append root to the queue
        if(tempTree.root.GetRightChild()!=None):                            ##if the root has a right child
            while(True):
                node=tempTree.root
                while( node.GetRightChild()!=None ):                        ##get the right most node
                    node=node.GetRightChild()
                stack.append(node.value)                                    ##add to stack (largest element)
                tempTree.DeleteValue(node.value)                            ##delete the right most node from the Temp tree
                if( tempTree.root.GetRightChild()==None ):                  ##break if all right sub tree values are added to the stack
                    break
        
        while( len(queue)!=0 ):                                             ##print the queue element by element
            print queue.pop(0),
        while( len(stack)!=0 ):                                             ##print the stack element by element
            print stack.pop(),
        print ""

    @staticmethod
    def CreateBinaryTree(ElementList):                                      ##overriding CreateBinaryTree method
        tree=BSTree()
        for ele in range( 0,len(ElementList) ):
            tree.AddValue( ElementList[ele] )
        return tree

    def ExpandBinaryTree(self, NewElementList):                             ##overriding ExpandBinaryTree method
        for ele in range( 0,len(NewElementList) ):
            self.AddValue( NewElementList[ele] )

from bt import BinaryTree

tr1 = BinaryTree.CreateBinaryTree( [1,2,3,4,5] )
print "tree : ",tr1
print "In Order Traverse",
tr1.TraverseInOrder(tr1.root)
print "\nPre Order Traverse",
tr1.TraversePreOrder(tr1.root)
print "\nPost Order Traverse",
tr1.TraversePostOrder(tr1.root)

tr1.ExpandBinaryTree([6,7,8,9,10])
print "\nIn Order Traverse",
tr1.TraverseInOrder(tr1.root)

tr1.ExpandBinaryTree([11,12,13,14,15])
print "\nIn Order Traverse",
tr1.TraverseInOrder(tr1.root)
print "\nPre Order Traverse",
tr1.TraversePreOrder(tr1.root)
print "\nPost Order Traverse",
tr1.TraversePostOrder(tr1.root)

print "\n"

tr2 = BinaryTree.CreateBinaryTree( [10,2,14,3,50,12,56,17] )
print "tree : ",tr2
print "In Order Traverse",
tr2.TraverseInOrder(tr2.root)
print "\nPre Order Traverse",
tr2.TraversePreOrder(tr2.root)
print "\nPost Order Traverse",
tr2.TraversePostOrder(tr2.root)

tr2.ExpandBinaryTree([6,57,18,1,3,7,23,200])
print "\nIn Order Traverse",
tr2.TraverseInOrder(tr2.root)

print "\n"

tr3 = BinaryTree().CreateBinaryTree( [1,12,25,34] )
print "tree : ",tr3
print "In Order Traverse",
tr3.TraverseInOrder(tr3.root)

tr3.ExpandBinaryTree([41,53,66,72,83,91,97,100,107,114,126,132,144,150])
print "\nIn Order Traverse",
tr3.TraverseInOrder(tr3.root)

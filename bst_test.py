from bst import BSTree


tr1=BSTree()
print "addition..."
print tr1.AddValue(100)
print tr1.AddValue(50)
print tr1.AddValue(150)
print tr1.AddValue(30)
print tr1.AddValue(60)
print tr1.AddValue(20)
print tr1.AddValue(40)
print tr1.AddValue(55)
print tr1.AddValue(70)
print tr1.AddValue(10)
print tr1.AddValue(33)
print tr1.AddValue(57)
print tr1.AddValue(15)
print tr1.AddValue(35)
print "\nsearch..."
print tr1.SearchValue(10)
print tr1.SearchValue(23)
print tr1.SearchValue(50)
print tr1.SearchValue(12)
print "\nPre order Traverse"
tr1.TraversePreOrder(tr1.root)
print "\n\ndeleting..."
print tr1.DeleteValue(23)
print tr1.DeleteValue(30)
print tr1.DeleteValue(50)
print "\nPre order Traverse"
tr1.TraversePreOrder(tr1.root)
print "\nprinting..."
tr1.PrintTree()

print "-----------------------------------------------------------"
tr2=BSTree()
print "addition..."
print tr2.AddValue(10)
print tr2.AddValue(50)
print tr2.AddValue(15)
print tr2.AddValue(3)
print tr2.AddValue(15)
print tr2.AddValue(6)
print tr2.AddValue(2)
print "\nsearch..."
print tr2.SearchValue(10)
print tr2.SearchValue(3)
print tr2.SearchValue(5)
print tr2.SearchValue(1)
print "\nPre order Traverse"
tr2.TraversePreOrder(tr2.root)
print "\n\ndeleting..."
print tr2.DeleteValue(12)
print tr2.DeleteValue(10)
print "\nPre order Traverse"
tr2.TraversePreOrder(tr2.root)
print "\nprinting..."
tr2.PrintTree()

print "-----------------------------------------------------------"
tr3=BSTree()
print "addition..."
print tr3.AddValue(100)
print tr3.AddValue(50)
print tr3.AddValue(15)
print tr3.AddValue(9)
print tr3.AddValue(5)
print tr3.AddValue(2)
print tr3.AddValue(15)
print "\nsearch..."
print tr3.SearchValue(100)
print tr3.SearchValue(9)
print tr3.SearchValue(15)
print tr3.SearchValue(1)
print "\nPre order Traverse"
tr3.TraversePreOrder(tr3.root)
print "\n\ndeleting..."
print tr3.DeleteValue(10)
print tr3.DeleteValue(11)
print "\nPre order Traverse"
tr3.TraversePreOrder(tr3.root)
print "\nprinting..."
tr3.PrintTree()

print "-----------------------------------------------------------"
tr4=BSTree()
print "addition..."
print tr4.AddValue(1)
print tr4.AddValue(10)
print tr4.AddValue(15)
print tr4.AddValue(50)
print tr4.AddValue(100)
print tr4.AddValue(200)
print tr4.AddValue(15)
print "\nsearch..."
print tr4.SearchValue(100)
print tr4.SearchValue(9)
print tr4.SearchValue(15)
print tr4.SearchValue(1)
print "\nPre order Traverse"
tr4.TraversePreOrder(tr4.root)
print "\n\ndeleting..."
print tr4.DeleteValue(8)
print tr4.DeleteValue(150)
print "\nPre order Traverse"
tr4.TraversePreOrder(tr4.root)
print "\nprinting..."
tr4.PrintTree()


print "-----------------------------------------------------------"
tr5=BSTree.CreateBinaryTree([10,5,15,1,5])
print "tree : ",tr5
print "\nsearch..."
print tr5.SearchValue(5)
print tr5.SearchValue(12)
print "\nPre order Traverse"
tr5.TraversePreOrder(tr5.root)
print ""

tr5.ExpandBinaryTree([2,7,20,12])
print "\nPre order Traverse"
tr5.TraversePreOrder(tr5.root)

print "\n\nsearch..."
print tr5.SearchValue(5)
print tr5.SearchValue(12)
print "\ndeleting..."
print tr5.DeleteValue(5)
print tr5.DeleteValue(12)
print "\nsearch..."
print tr5.SearchValue(5)
print tr5.SearchValue(12)
print "\nPre order Traverse"
tr5.TraversePreOrder(tr5.root)
print "\nprinting..."
tr5.PrintTree()

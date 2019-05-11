class Node():
  
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
    
  def insert(self, data):
    if(data < self.data):    #making a decision to insert to left or right or node
      if(self.left is None):  #if no node, create node
        self.left = Node(data)
      else: #if node, insert data
        self.left.insert(data)
    elif(data > self.data):
      if(self.right is None):
        self.right = Node(data)
      else:
        self.right.insert(data)
        
  def print_inorder(self, root):  #ie left->root->right
    tmp = []
    if root:
      tmp = tmp + self.print_inorder(root.left)
      tmp.append(root.data)
      tmp = tmp + self.print_inorder(root.right)
    return tmp
    
  def print_preorder(self, root):  #ie root->left->right
    tmp = []
    if root:
      tmp.append(root.data)
      tmp = tmp + self.print_preorder(root.left)
      tmp = tmp + self.print_preorder(root.right)
    return tmp
    
  def print_postorder(self, root):  #ie left->right->root
    tmp = []
    if root:
      tmp = tmp + self.print_postorder(root.left)
      tmp = tmp + self.print_postorder(root.right)
      tmp.append(root.data)
    return tmp
    
root = Node(29)
root.insert(12)
root.insert(38)
root.insert(8)
root.insert(20)
root.insert(30)
root.insert(46)
print(root.print_inorder(root))
print(root.print_preorder(root))
print(root.print_postorder(root))
    

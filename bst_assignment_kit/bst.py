#Oscar Gandara
# On my honor as a University of Colorado Student, this code was entirely written by myself with no unauthorized help.
# This class implements a Binary Search Tree Class
# The binary search tree class will include functionality of
#   1. Insert a Node in the Tree.
#   2. Search for a Node in the Tree
#   3. Various traversals including in order, preorder and postorder traversals.
#
#  The binary search tree is made of class Node objects.
#    Each node has three members: key is an integer, left and right child point to nodes.
#    If left is None, then it means that the node has no left child.
#    If right is None then the node has no right child.


class Node:

	def __init__(self, my_key): # Constructor for the Node.
		self.key = my_key       # Set the key to my_key
		self.left = None        # Set left child to None
		self.right = None       # Set right child to None

	def insert(self, key_to_insert):
		
		if self is None:
			self = Node(key_to_insert)
			return self.key
		
		elif (key_to_insert < self.key):
			if self.left is None:
				self.left = Node(key_to_insert)
				return self.left
			else:
				self.left.insert(key_to_insert)
		
		elif (key_to_insert > self.key):
			if self.right is None:
				self.right = Node(key_to_insert)
				return self.right
			else:
				self.right.insert(key_to_insert)
		else:
			return None
	
	def inorder_traversal(self, ret_list):
		#if (self is None):
			#return None
		
		if (self.left is not None):
			self.left.inorder_traversal(ret_list)
		if (self.left is not None and self.right is None):
			ret_list.append(self.key)
		if (self.right is not None):
			ret_list.append(self.key)
			self.right.inorder_traversal(ret_list)
		if (self.left is None and self.right is None):
			ret_list.append(self.key)
			
		return ret_list
			
		
		
		
        # TODO: write an inorder traversal function for the BST.
        # REMOVE the assert below
		

	def get_depth(self):
		leftDepth = 0
		rightDepth = 0
		if self.left is None and self.right is None:
			return 1
		if self.left is not None:
			leftDepth = self.left.get_depth()
		if self.right is not None:
			rightDepth = self.right.get_depth()
		return max(rightDepth , leftDepth)+1
		
        # TODO: write a get_depth function for the BST
        #   Depth of a tree with no children is 1.
        #   Otherwise, depth = 1 + max(depth(left subtree), depth(right subtree))
        # REMOVE the assert below
		

	def key_exists(self, key_to_find):
		
			
		if key_to_find == self.key: 
			return True
		elif self.key < key_to_find and self.right is not None:
			return self.right.key_exists(key_to_find)
		elif self.key > key_to_find and self.left is not None:
			return self.left.key_exists(key_to_find)
		else:
			return False
		
        # return True if the key_to_find is already in the tree,
        #   otherwise return False
        # REMOVE the assert below
		

if __name__ == '__main__':
	print('Please do not call this file directly.')
	print('To run autograder script: please call the test_bst.py')

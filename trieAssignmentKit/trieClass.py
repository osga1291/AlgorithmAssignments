#LastName:Gandara
#FirstName:Oscar
#Email:osga1291@colorado.edu
#Comments:
# Your student ID: 100608478
# On my honor as a University of Colorado student, I acknowledge that
# I did not receive any unauthorized help for this assignment.
# I understand that systems like MOSS can easily detect code plagiarism
from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
	def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
		self.isRoot = isRootNode
		self.isWordEnd = False # is this node a word ending node
		self.isRoot = False # is this a root node
		self.count = 0 # frequency count
		self.next = {} # Dictionary mappng each character from a-z to the child node
	
	def addWord(self,w):
		if len(w) == 0:
			self.isWordEnd = True
			self.count = self.count + 1
			return
	
		
		char = w[0]
		if char not in self.next:
			self.next[char] = MyTrieNode(False)
		self.next[char].addWord(w[1:])
        
       

	def lookupWord(self,w):
		
		
		if len(w) == 0:
			return self.count
		char = w[0]
		if char not in self.next:
			return 0
		return self.next[char].lookupWord(w[1:])
		
	def dfs(self, w, result):
		
		
		if self.isWordEnd: 
			result = ((w,self.count))
			
		char = w[0]
		if char in self.next:
			return self.dfs(w[0:],result)
		return result
	def autoComplete(self,w):
		
		result = []
		
		
		if self.isWordEnd:
			return self.dfs(w,result)
		char = w[0]
		if char not in self.next:
			return []
		
		return self.next[char].autoComplete(w[0:])
		
    
    
            

if (__name__ == '__main__'):
	t= MyTrieNode(True)
	lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

	for w in lst1:
		t.addWord(w)

	j = t.lookupWord('testy') # should return 0
	j2 = t.lookupWord('telltale') # should return 0\
	j3 = t.lookupWord ('testing') # should return 2
	lst3 = t.autoComplete('pi')
	print(j)
	print(j2)
	print(j3)
	print('Completions for \"pi\" are : ')
	print(lst3)
	lst4 = t.autoComplete('tes')
	print('Completions for \"tes\" are : ')
	print(lst4)
 
    	
    
     

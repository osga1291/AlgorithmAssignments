import random
from bst import Node
import matplotlib.pyplot as plt


# Function: test_random_sequences creates a randomly ordered list of n elements
#           inserts the random sequence into a binary search tree and gets the
#           depth of the resulting tree.
def test_random_sequences(n, n_trials, depths_list):
    # Inputs: n = number of elements to be inserted into the tree.
    # n_trials: number of samples to generate
    # depths_list: list of tree depths for each run/sample.

    # 1. Create an array of elements from 0 to n-1
    a = [i for i in range(0,n)]
    # 2. Now create random shuffles of a and insert into the tree.
    for j in range(0, n_trials):
        # Shuffle this array randomly
        random.shuffle(a)
        # Insert the elements of the array one by one into a tree
        r = Node(a[0]) #Create a root
        # Insert the rest of the elements
        for k in range(1, n):
            r.insert(a[k])
        # Compute the depth and append to the list of samples
        depths_list.append(r.get_depth())
    avg = sum(depths_list)/len(depths_list)
    return avg




d_list=[]
test_random_sequences(100, 10000, d_list)
n = 100
fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.hist(d_list, 10, normed=True,  facecolor='red')
ax1.set_xlabel('Tree Depth')
ax1.set_ylabel('Probability')
ax1.set_title('Histogram of tree depths for n = %d'%n)
ax1.grid(True)


avg_list = []
num_list=[]
for i in range(10, 200, 5):
    avg = test_random_sequences(i, 20*i, [])
    avg_list.append(avg)
    num_list.append(i)
    print(i, avg)


ax2.plot(num_list, avg_list, 'bo')
ax2.set_xlabel('n')
ax2.set_ylabel('Avg. Tree Depth')
ax2.set_title('Avg. Tree Depth vs. n')
plt.show()









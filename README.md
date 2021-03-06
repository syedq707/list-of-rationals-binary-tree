# list-of-rationals-binary-tree
Here's a way to construct a list containing every positive rational number:  
Build a binary tree where each node is a rational and the root is 1/1, 
with the following rules for creating the nodes below:  

The value of the left-hand node below a/b is a/a+b. 
The value of the right-hand node below a/b is a+b/b. 
So the tree will look like this: 

                         1/1             
                     /           \             
                1/2                 2/1         
              /    \              /     \        
          1/3        3/2        2/3       3/1      
         /   \      /   \      /   \     /   \    
      1/4    4/3  3/5   5/2  2/5   5/3  3/4   4/1  
      ...
      
Now traverse the tree, breadth first, to get a list of rationals.
      
    [ 1/1, 1/2, 2/1, 1/3, 3/2, 2/3, 3/1, 1/4, 4/3, 3/5, 5/2, .. ]
      


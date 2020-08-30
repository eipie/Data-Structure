# AVL Tree

1. Balanced 
    - Binary search trees support insert, delete, min, max, next_Large and next_Smaller
    in O(h) time, where h is the height of the tree 
    - h is between log(n) and n
    - Balanced BST maintains h = O(log(n)) => all operations run at O(log(n)) time

2. AVL trees
    - for every node, require heights of left and right children to differ by at most +- 1
    - treat nill tree as height -1
    - each node stores its height

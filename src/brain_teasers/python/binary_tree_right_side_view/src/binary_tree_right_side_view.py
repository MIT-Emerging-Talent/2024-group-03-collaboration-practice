from typing import List

class TreeNode:
    def __init__(self, value: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right

def right_side_view(root: TreeNode) -> List[int]:
    # Handle edge case: if the tree is empty, return an empty list
    if not root:
        return []

    # Initialize a queue and a result list
    queue = [root]
    result = []

    # Process nodes level by level using BFS
    while queue:
        # Get the size of the queue (number of nodes at the current level)
        size = len(queue)

        # Iterate through all the nodes at the current level
        for i in range(size):
            # Dequeue the first node from the queue
            node = queue.pop(0)

            # If this is the last node in the current level, add its value to the result list
            if i == size - 1:
                result.append(node.value)

            # Enqueue the left child if it exists
            if node.left:
                queue.append(node.left)

            # Enqueue the right child if it exists
            if node.right:
                queue.append(node.right)

    # Return the result list containing the values of the rightmost nodes at each level
    return result
# Problem 18 - Maximum Path Sum 1
print "Problem 18 - Maximum Path Sum 1"

triangle = (\
(75, 0),\
(95, 64),\
(17, 47, 82),\
(18, 35, 87, 10),\
(20, 04, 82, 47, 65),\
(19, 01, 23, 75, 03, 34),\
(88, 02, 77, 73, 07, 63, 67),\
(99, 65, 04, 28, 06, 16, 70, 92),\
(41, 41, 26, 56, 83, 40, 80, 70, 33),\
(41, 48, 72, 33, 47, 32, 37, 16, 94, 29),\
(53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14),\
(70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57),\
(91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48),\
(63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31),\
(04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23))

# We need a recursive function and a binary tree
# Binary Tree Node
class BTNode:
    def __init__(self, left, val, right):
	self.left = left
	self.val = val
	self.right = right

def create_BT(row_num, row_index):
    if row_num < 14:
	new_BT = BTNode(create_BT(row_num + 1, row_index),\
	    triangle[row_num][row_index],\
	    create_BT(row_num + 1, row_index + 1))
    else:
	new_BT = BTNode(None, triangle[row_num][row_index], None)
    return new_BT

def find_max_path(node):
    if node.left is None and node.right is None:
	return node.val
    else:
	left_branch = find_max_path(node.left)
	right_branch = find_max_path(node.right)
	if left_branch > right_branch:
	    return left_branch + node.val
	else:
	    return right_branch + node.val

triangle_BT = create_BT(0, 0)
print find_max_path(triangle_BT)

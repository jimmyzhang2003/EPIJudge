from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def dfs(left, right):
        if not left and not right:
            return True
        
        if not left and right or left and not right:
            return False

        return left.data == right.data and dfs(left.left, right.right) and dfs(left.right, right.left)

    return not tree or dfs(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))

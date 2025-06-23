from typing import Optional, List
from collections import deque

# Definisi struktur TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Fungsi utama menghitung jumlah daun kiri
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total = 0

        if root.left:
            if not root.left.left and not root.left.right:
                total += root.left.val

        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)

        return total

# Fungsi untuk membangun pohon dari input list level-order
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

# ==== Bagian Input dan Eksekusi ====

input_str = input("Masukkan level-order tree (contoh: 3 9 20 null null 15 7): ")
input_list = [
    int(x) if x != "null" else None
    for x in input_str.strip().split()
]

tree_root = build_tree(input_list)
sol = Solution()
hasil = sol.sumOfLeftLeaves(tree_root)

print("Jumlah daun kiri adalah:", hasil)

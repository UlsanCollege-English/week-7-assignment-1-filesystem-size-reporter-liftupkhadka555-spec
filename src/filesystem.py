# src/filesystem.py

class Node:
    def __init__(self, name, size=0, children=None):
        """
        Node represents a file or folder.
        - name: string, the name of the file/folder
        - size: int, size in whatever units (files have non-zero size, folders can be 0)
        - children: list of Node objects (empty or None for files)
        """
        self.name = name
        self.size = size
        self.children = children or []

def total_size(node):
    """
    Recursively calculate the total size of a node (file or folder),
    including all its children.
    Returns 0 if node is None.
    """
    if node is None:
        return 0
    total = node.size
    for child in node.children:
        total += total_size(child)
    return total

def folder_sizes(node):
    """
    Returns a dictionary mapping folder names to their total sizes.
    Files (nodes without children) are ignored.
    """
    if node is None or not node.children:
        return {}  # files do not count as folders
    sizes = {node.name: total_size(node)}
    for child in node.children:
        sizes.update(folder_sizes(child))
    return sizes

def level_order(node):
    """
    Returns a list of lists of node names, level by level (BFS traversal).
    Returns empty list if node is None.
    """
    if node is None:
        return []
    
    result = []
    queue = [node]
    
    while queue:
        level_names = [n.name for n in queue]
        result.append(level_names)
        next_level = []
        for n in queue:
            next_level.extend(n.children)
        queue = next_level
    
    return result

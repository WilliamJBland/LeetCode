"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        old_new_node_map = {}

        def dfs(old_node):
            new_node = old_new_node_map.get(old_node, Node(old_node.val))
            if old_node not in old_new_node_map:
                old_new_node_map[old_node] = new_node
            for n in old_node.neighbors:
                if n in old_new_node_map:
                    if old_new_node_map[n] not in new_node.neighbors:
                        new_node.neighbors.append(old_new_node_map[n])
                    if new_node not in old_new_node_map[n].neighbors:
                        old_new_node_map[n].neighbors.append(new_node)
                else:
                    dfs(n)
        dfs(node)
        return old_new_node_map[node]


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        old_new_node_map = {}

        def dfs(old_node):
            if old_node in old_new_node_map:
                return old_new_node_map[old_node]
            new_node = Node(old_node.val)
            old_new_node_map[old_node] = new_node
            for n in old_node.neighbors:
                new_node.neighbors.append(dfs(n))
            return new_node

        return dfs(node)

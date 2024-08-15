class Solution:
    def canCross(self, stones) -> bool:
        self.stone_lookup = set(stones)
        self.last = stones[-1]
        self.visited = set()
        return self.dfs(1, 0)

    def dfs(self, jump, current_stone):
        if jump == 0:
            return False
        if current_stone + jump not in self.stone_lookup:
            return False
        if current_stone + jump == self.last:
            return True
        if (jump, current_stone) in self.visited:
            return False
        # jump to the stone
        current_stone += jump
        # check if I can reach the end from this stone
        x = self.dfs(jump + 1, current_stone) or self.dfs(jump, current_stone) or self.dfs(jump - 1, current_stone)
        if not x:
            self.visited.add((jump, current_stone))
        return x
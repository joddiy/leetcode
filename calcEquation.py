class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        i = 0
        char_set = set([char for item in equations for char in item])
        map_hash = dict((char, i) for i, char in enumerate(char_set))
        print(map_hash)
        matrix = [[0 for i in range(len(map_hash))] for j in range(len(map_hash))]
        print(matrix)
        for id, item in enumerate(equations):
            matrix[map_hash[item[0]]][map_hash[item[1]]] = values[id]
            matrix[map_hash[item[1]]][map_hash[item[0]]] = 1/values[id]
        print(matrix)
        # for char_x in range(len(map_hash)):
            # for char_y in range(len(map_hash)):
                # matrix[char_x][char_y] = 0


Solution().calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [
    ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])

import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        n = len(bank)
        all_genes = [startGene] + bank
        distance_map = defaultdict(list)
        for i in range(len(all_genes)):
            for j in range(1, len(all_genes)):
                a, b = all_genes[i], all_genes[j]
                sum_ = sum(1 for x in range(len(a)) if a[x] != b[x])
                if sum_ == 1:
                    distance_map[a].append(b)
                    distance_map[b].append(a)

        array = [(startGene, 0)]
        visited = set(startGene)
        while array:
            gene, path = array.pop(0)
            if gene == endGene:
                return path
            else:
                for next_gene in distance_map[gene]:
                    if next_gene not in visited:
                        array.append((next_gene, path + 1))
                        visited.add(next_gene)
        return -1


solution = Solution().minMutation
solution(startGene="AACCGGTT", endGene="AACCGGTA", bank=["AACCGGTA"])
solution(startGene="AACCGGTT", endGene="AAACGGTA", bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"])

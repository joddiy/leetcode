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
        gen_len = len(startGene)
        bank = bank + [startGene]
        nei_ = defaultdict(set)
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                b_i = bank[i]
                b_j = bank[j]
                dis_ = sum(0 if b_i[k] == b_j[k] else 1 for k in range(gen_len))
                if dis_ == 1:
                    nei_[b_i].add(b_j)
                    nei_[b_j].add(b_i)
        array = [(startGene, 0)]
        visited = set(startGene)
        while array:
            gene, path = array.pop(0)
            visited.add(gene)
            if gene == endGene:
                return path
            else:
                for next_gene in nei_[gene]:
                    if next_gene not in visited:
                        array.append((next_gene, path + 1))
        return -1


solution = Solution().minMutation
solution(startGene="AACCGGTT", endGene="AACCGGTA", bank=["AACCGGTA"])
solution(startGene="AACCGGTT", endGene="AAACGGTA", bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"])

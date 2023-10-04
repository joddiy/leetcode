import math
import pprint
import sys

from tools import *
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
        n = len(startGene)
        all_genes = [startGene] + bank
        distance_map = defaultdict(list)  # if a mutates to b in single path, then record map[a] = [b]
        for i in range(len(all_genes)):
            for j in range(i + 1, len(all_genes)):
                gene_a = all_genes[i]
                gene_b = all_genes[j]
                c = sum([1 if gene_a[k] != gene_b[k] else 0 for k in range(n)])
                if c == 1:
                    distance_map[gene_a].append(gene_b)
                    distance_map[gene_b].append(gene_a)

        visited = set()
        array = [(startGene, 0)]
        visited.add(startGene)
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
# solution(startGene="AACCGGTT", endGene="AACCGGTA", bank=["AACCGGTA"])
# solution(startGene="AACCGGTT", endGene="AAACGGTA", bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"])
# solution(startGene="AACCGGTT", endGene="AACCGGTA", bank=[])

solution(startGene="AACCGGTT", endGene="AATTCCGG", bank=["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"])

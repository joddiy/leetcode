import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """


solution = Solution().snakesAndLadders
solution(startGene="AACCGGTT", endGene="AACCGGTA", bank=["AACCGGTA"])
solution(startGene="AACCGGTT", endGene="AAACGGTA", bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"])

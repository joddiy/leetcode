# -*- coding: utf-8 -*-
# file: reconstructQueue.py
# author: joddiyzhang@gmail.com
# time: 2018/11/22 9:21 PM
# ------------------------------------------------------------------------

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        q_size = len(people)
        output = [[0] * 2] * q_size
        res = list(range(q_size))

        q_map = {}
        for i in range(q_size):
            t_people = people[i]
            if t_people[0] not in q_map:
                q_map[t_people[0]] = set()
            q_map[t_people[0]].add(t_people[1])

        while q_map:
            i = min(q_map.keys())
            while q_map[i]:
                j = max(q_map[i])
                q_map[i].remove(j)
                output[res[j]] = [i, j]
                del res[j]
            del q_map[i]
        return output

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        print(people)
        # print people
        result = []
        for p in people:
            result.insert(p[1], p)
        return result


print(Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))

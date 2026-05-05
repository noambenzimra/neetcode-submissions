class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # my_map = {}

        # for s in strs:
        #     key = tuple(sorted(s))
        #     if key not in my_map:
        #         my_map[key] = [s]
        #     else:
        #         my_map[key].append(s)
        # return list(my_map.values())

        my_map = defaultdict(list)

        for s in strs:

            count = [0]*26

            for c in s:
                count[ord(c) - ord('a')] += 1
            my_map[tuple(count)].append(s)

        return list(my_map.values())
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # dump characters into dict, add count for letters (as keys), increase their value if seen, if not def 1
        d = {}

        # iter magazine for dict
        for i in magazine:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        # sub chars for ransomNote
        for j in ransomNote:
            if j in d and d[j] > 0:
                d[j] -= 1

            else:
                return False

        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dict_s = self.count_words(s)
        dict_t = self.count_words(t)

        for key in dict_s:
            if key not in dict_t or dict_s[key] != dict_t[key]:
                return False

        return True

    def count_words(self, s: str) -> dict:
        dict_s = dict()

        for word in s:
            if word in dict_s:
                dict_s[word] += 1
            else:
                dict_s[word] = 1
        return dict_s

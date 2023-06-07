def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = ""
        count = 0
        max = 0
        for i in range(len(s)):
            if s:
                if s[i] in res:
                    count = 1
                    res = s[i]
                else:
                    res = res + s[i]
                    count += 1
                
                if count > max:
                    max = count

            print(f"{res} - {max}")

        return max  
                  

result = lengthOfLongestSubstring(lengthOfLongestSubstring, "dvdf")
print(result)
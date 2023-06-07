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
                    print("Работает if 1")
                    res = res[1:] + s[i]
                    count = len(res)
                else:
                    print("Работает else 1")
                    res = res + s[i]
                    count += 1
                    print(count)
                
                # if count > max:
                #     print("Работает if 2")
                #     max = count
            max = len(res)
            print(f"{res} - {max}")

        return max  
                  

result = lengthOfLongestSubstring(lengthOfLongestSubstring, "pwwkew")
print(result)
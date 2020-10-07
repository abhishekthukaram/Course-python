class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        out = 0
        i= 0
        values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        while i <len(s):
            if i+1 < len(s) and values[s[i]] < values[s[i+1]]:
                temp = values[s[i+1]]-values[s[i]]
                out+=temp
                i+=2
            else:
                out+=values[s[i]]
                i+=1
        return out
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = ''
        for i in s:
            if len(a) > 0:
                if i != '#':
                    a += i
                else:
                    a = a[:-1]
            else:
                if i != '#':
                    a += i
        
        b = ''
        for i in t:
            if len(b) > 0:
                if i != '#':
                    b += i
                else:
                    b = b[:-1]
            else:
                if i != '#':
                    b += i
        return a == b
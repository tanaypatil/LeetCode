class Solution:
    def myAtoi(self, string: str) -> int:
        string = string.strip()
        neg = False
        if not string:
            return 0
        if string[0] == "-":
            neg = True
            string = string[1:]
        elif string[0] == "+":
            string = string[1:]
        if not string:
            return 0
        # print(string)
        if not string[0].isnumeric():
            return 0
        ns = ""
        for c in string:
            if c.isnumeric():
                ns += c
            else: break
        string = ns
        if not string:
            return 0
        n = len(string)
        s = 0
        for i in range(n-1, -1, -1):
            if not string[i].isnumeric():
                return -1
            s += int(string[i]) * (10**(n-1-i))
            if s > 2**31 -1 and not neg: return 2**31 -1
            if s > 2**31 and neg: return -2**31
        return -s if neg else s

        
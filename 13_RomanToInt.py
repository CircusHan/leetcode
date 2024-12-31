class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        roman_d = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        for i in range(len(s)) :
            if i+1 < len(s) and roman_d[s[i]] < roman_d[s[i+1]]:
                sum -= roman_d[s[i]]
            else :
                sum += roman_d[s[i]]
        return sum

    def test(self):
        return

# Python - IDE, Editor, Compiler, Interpreter
#used python online beta IDE
#convert roman number to integer
class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        i = 1
        num = 0
#rom_dic contains standard romans 
        rom_dict = {"I": 1, "V": 5, "X":10, "L": 50, "C": 100, "D":
500, "M": 1000}
        num += rom_dict[s[0]]
#check every roman and assign interger value
        while (i<n):
            if rom_dict[s[i-1]] < rom_dict[s[i]]:
                num += rom_dict[s[i]] - 2 * rom_dict[s[i-1]]
            else:
                num += rom_dict[s[i]]
            i += 1
        return num
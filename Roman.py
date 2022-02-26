
#This class converts integer numbers to roman numbers

class IntegerToClass:
    def IntegrToRomanConversion(self, num: int) -> str:
        #creating dictionary containing standard roman numbers
        dictionary = {
                0:"",1:"I",2:"II",3:"III",4:"IV",5:"V",9:"IX",10:"X",40:"XL",
                50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"
               }
        # if a given number is part of the dictionary element, return the respective roman number
        if num in dictionary.keys():
            return dictionary[num]
        number = num
        # Otherwise check every digit at units place, tenth's place etc and assign respected roman symbol
        result = ""
        while number > 0:
            for keys in sorted(dictionary.keys(),reverse=True):
                if number > keys:
                    div, number = divmod(number, keys)
                    result += dictionary[keys] * div
                elif number == keys:
                    result += dictionary[keys]
                    num -= keys
        return result

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

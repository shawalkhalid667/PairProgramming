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
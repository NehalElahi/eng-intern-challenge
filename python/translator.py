import sys

class BrailleTranslator:
    def __init__(self, input_str):
            self.output_arr = []
            self.BRAILLE_CHARACTER_LENGTH = 6
            self.NUM_CHECK = False
            self.CAPITAL_CHECK = False
            self.input_str = input_str

            self.BRAILLE_TO_ENGLISH = {
                "O.....":"a", "O.O...":"b", "OO....":"c", "OO.O..":"d", "O..O..":"e",
                "OOO...":"f", "OOOO..":"g", "O.OO..":"h", ".OO...":"i", ".OOO..":"j",
                "O...O.":"k", "O.O.O.":"l", "OO..O.":"m", "OO.OO.":"n", "O..OO.":"o",
                "OOO.O.":"p", "OOOOO.":"q", "O.OOO.":"r", ".OO.O.":"s", ".OOOO.":"t",
                "O...OO":"u", "O.O.OO":"v", ".OOO.O":"w", "OO..OO":"x", "OO.OOO":"y",
                "O..OOO":"z", "......":" ", ".....O":"capital", ".O...O":".", ".O.OOO":"num"
            }

            self.BRAILLE_TO_NUM = {
                "O.....":"1", "O.O...":"2", "OO....":"3", "OO.O..":"4", "O..O..":"5",
                "OOO...":"6", "OOOO..":"7", "O.OO..":"8", ".OO...":"9", ".OOO..":"0",
                "......":" "
            }

            self.ENGLISH_TO_BRAILLE = {
                "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
                "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
                "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
                "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
                "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
                "z": "O..OOO", " ": "......", ".": ".O...O", "1": "O.....", "2": "O.O...",
                "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..",
                "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
            }
    def isBraille(self): 
          return set(self.input_str[1]).issubset('O.') and len(sys.argv) == 2
    
    def translateToEnglish(self):
        self.output_arr = [self.input_str[1][i:i+self.BRAILLE_CHARACTER_LENGTH] for i in range(0, len(self.input_str[1]), self.BRAILLE_CHARACTER_LENGTH)]
        for braille_char in self.output_arr:
            if self.BRAILLE_TO_ENGLISH[braille_char] == "capital":
                self.CAPITAL_CHECK = True
                continue
            elif self.BRAILLE_TO_ENGLISH[braille_char] == "num": 
                self.NUM_CHECK = True
                continue

            if self.CAPITAL_CHECK:
                print(self.BRAILLE_TO_ENGLISH[braille_char].upper(), end="")
                self.CAPITAL_CHECK = False    

            elif self.NUM_CHECK:
                print(self.BRAILLE_TO_NUM[braille_char], end="")
                if self.BRAILLE_TO_ENGLISH[braille_char] == " ":
                    self.NUM_CHECK = False
            else:
                print(self.BRAILLE_TO_ENGLISH[braille_char], end="")                
           
    def translateToBraille(self):
        self.output_arr = [' '.join(sys.argv[1:(len(sys.argv))])]
        self.output_arr = [*self.output_arr[0]]
        for char in self.output_arr:
            if char == " ":
                self.NUM_CHECK = False
            elif char.isnumeric() and not self.NUM_CHECK:
                print(".O.OOO", end="")
                self.NUM_CHECK = True
            elif char.isupper():
                print(".....O", end="")
            print(self.ENGLISH_TO_BRAILLE[char.lower()], end="")   

if __name__ == "__main__" :
    translator = BrailleTranslator(sys.argv)

    if translator.isBraille():
        translator.translateToEnglish()
    else:
        translator.translateToBraille()

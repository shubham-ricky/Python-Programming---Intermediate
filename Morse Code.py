"""
Given a dot is represented by one ‘1’ byte (1), a dash is represented by two ‘1’ bytes   (11), a pause between each dot or dash is separated by one ‘0’ byte (0), a pause between each letter from the Morse code is separated by two ‘0’ bytes (00), a pause between each word is separated by four ‘0’ bytes (0000), as shown below.

i.	Read all the binaries representing the Morse codes from a given data file c1059c_cwf_q1.dat and use them as input. 
ii.	Convert these Morse codes into plaintext. If you use a function, please provide flowchart for the function as well. 
iii.	Display all translated text on screen as output. 


"""

import textwrap             #...Using this library only for proper display of the output, this library can also be excluded and we can get the same output in one line

file = open("c1059c_cwf_q1.dat", "r")               #...Task ai): Read all the binaries representing the Morse Codes
data = file.read()                                  #...Task aii): Use the binaries as input


morse = data.replace('11','-').replace('1','.').replace('000000','  ').replace('00',' ').replace('0','').replace('\n',' ')            #...Convert binaries to Morse Codes

print()
print("The Morse Codes converted from given binaries are: \n")
print(morse)                                        #...Display Morse Codes
print()

MORSE_CODE_DICTIONARY = { ' ':'', 'A':'.-', 'B':'-...',        #...Initialize dictionary with letters as keys and corresponding Morse Codes as values
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'} 


def MorseCode_to_Text():                                    #...Task aii): Function to convert Morse codes into plaintext
    code = [k for i in morse.split(' ') for k,v in MORSE_CODE_DICTIONARY.items() if i==v]     
    text = ''.join(code)
    wrap_text = textwrap.fill(text, 40)
    return wrap_text
    
print("The translated text from the Morse Codes is: \n")
print(MorseCode_to_Text())                                  #...Task aiii): Display all translated text on screen as output

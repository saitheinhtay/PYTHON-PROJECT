_1to9 = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
'5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
'9': 'nine'}
_10to19 = {'0': 'ten', '1': 'eleven', '2': 'twelve',
'3': 'thirteen', '4': 'fourteen', '5': 'fifteen',
'6': 'sixteen', '7': 'seventeen', '8': 'eighteen',
'9': 'nineteen'}
_20to90 = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
'6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}
_magnitude_list = [(0, ''), (3, ' thousand '), (6, ' million '),
(9, ' billion '), (12, ' trillion '),(15, '')]
def numtoword(numstring):
    if numstring == '0':
        return 'Zero'
    numstring = numstring.replace(',','')
    numLength = len(numstring)
    maxDigit = _magnitude_list[-1][0]
    if numLength > maxDigit:
        return f"Sorry! can't handle number more than {maxDigit}"

    numstring = '00' + numstring
    wordString = ''
    for mag, name in _magnitude_list:
        if mag >= numLength:
            return wordString
        else:
            hundreds, tens,ones = numstring[-mag-3],numstring[-mag-2],numstring[-mag-1]
            if not (hundreds == tens == ones == '0'):
                wordString = handle1to999(hundreds, tens, ones) + name + wordString


def handle1to99(tens, ones):
    if tens == '0':
        return _1to9[ones]
    if tens == '1':
        return _10to19[ones]
    else:
        return _20to90[tens] + ' '+ _1to9[ones]

def handle1to999(hundreds, tens, ones):
    if hundreds == '0':
        return  handle1to99(tens, ones)
    else:
        return _1to9[hundreds] + ' ' + 'hundred' + ' ' +  handle1to99(tens, ones)
def main():
    while True:
        num = input('Enter numbers : ')
        if num == 'q': return
        result = numtoword(num)
        print(f'For {num}, say {result}')

if __name__ == '__main__':
    main()
else:
    print('load as module')


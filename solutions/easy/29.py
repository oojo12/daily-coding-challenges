string = 'AAAABBBCCDAA'
def encode_string(string):
    count = 1
    encoding = ''
    for i in range(len(string)):
        if i == 0:
            ele = string[0]
        else:
            if string[i] == ele and i != len(string)-1:
                count += 1
            elif string[i] != ele and i != len(string)-1:
                encoding += f'{count}{ele}'
                ele = string[i]
                count = 1
            elif string[i] != ele and i == len(string)-1:
                count += 1
                encoding += f'{count}{ele}'
            else:
                count += 1
                encoding += f'{count}{ele}'
    return encoding

def decode_string(encoding):
    decoding = ''
    for i in range(0, len(encoding), 2):
        decoding += int(encoding[i]) * encoding[i+1]
    return decoding

assert encode_string(string) == '4A3B2C1D2A'
assert decode_string(encode_string(string)) == string

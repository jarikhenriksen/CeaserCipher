

def encodeOrDecode(word, cypher):
    cypher = int(cypher)
    codedWord = ''
    codedWordInList = []

    if start == 'encode':       #encodes word based off given cypher
        for letter in word:
            codedWordInList.append(chr(ord(letter) + cypher))      #changes each letter in word by given cypher, adds it to list
        codedWord = ''.join([str(i) for i in codedWordInList])      #Takes letters in list and joins them into a string
        return codedWord

    elif start == 'decode':     #decodes word based of given cypher
        for letter in word:
            codedWordInList.append(chr(ord(letter) - cypher))       #changes each letter in word by given cypher, adds it to list
        codedWord = ''.join([str(i) for i in codedWordInList])      #Takes letters in list and joins them into a string
        return codedWord


start = input('would you like to encode a message, or decode a message? ')
if start == 'encode':
    message = input('what message are we sending? ')

    shift = input('What are we shifting these by? ')
    print(encodeOrDecode(message, shift))

elif start == 'decode':
    message = input('What are we decoding? ')
    shift = input('What are we shifting this by? ')
    print(encodeOrDecode(message, shift))

else:
    print('please type "encode" or "decode" ')

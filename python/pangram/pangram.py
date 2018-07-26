import string
def is_pangram(sentence):
    # Determine if a sentence is a pangram
    # The alphabet used consists of ASCII letters a to z, inclusive, and is case insensitive
    # every letter of the alphabet at least once
    #
    sentence = sentence.lower()
    sentence = sentence.translate(None, string.digits) # or filter(lambda x: x.isalpha(), sentence)
    sentence = filter(lambda x:x not in string.punctuation, sentence)
    alphabet = map(chr, range(97, 123)) #  or simply alphabet = list('abcdefghijklmonpqrstuwxyz')
    return set(alphabet) <= set(sentence)
    

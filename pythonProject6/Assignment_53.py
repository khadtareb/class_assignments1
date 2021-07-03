# Python | Swap commas and dots in a String

s='vdf........n.jgf,'

def Replace(s):
    s=s.replace('.','?')
    s=s.replace(',','.')
    s=s.replace('?',',')
    return s
print(Replace(s))


def Replace(str1):
    maketrans = str1.maketrans
    final = str1.translate(maketrans(',.', '.,', ' '))
    return final.replace(',', ", ")


# Driving Code
string = "14, 625, 498.002"
print(Replace(string))
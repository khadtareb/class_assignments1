#51. Python | Find all close matches of input string from a list
from difflib import get_close_matches
def close_matches(patterns,word):
    print(get_close_matches(patterns,word))

close_matches('ban',['apple','banana','peru'])
#. Python | Sort Python Dictionaries by Key or Value Handling missing keys in
#using get
d={'India':'091','bengal':'342'}
# print(d.get('India','Not found'))
# print(d.get('Pakistan','Not found'))

#using select defualt
# d1=d.setdefault('Japan','086')
# print(d)

# defualt dict
import collections

def_dict=collections.defaultdict(lambda :'key not ')
def_dict['a']=1
def_dict['b']=2
print(def_dict['c'])
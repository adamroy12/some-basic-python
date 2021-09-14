# Dictionaries are like hashes in ruby. They consist of Key and Value pairs.

acronyms = {'LOL':'Laugh out loud',
            'IDK':"I don't know,",
            'TBH':'to be honest'}


print(acronyms['LOL'])

acronyms['Skibbidop'] = 'Scat Jazz is the best'

print(acronyms)

del acronyms['LOL']

print(acronyms)

# Getting an value that might not exist.
# Trying to use a key that doesn't exist using acronym['NO-KEY'] will cause
# an error. To avoid this use .get, like this:

definition = acronyms.get('NO-KEY')
print(definition)

# None is the absence of a value, the same as nil.

sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)
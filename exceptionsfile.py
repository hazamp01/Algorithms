try:
    text = input('Enter some text my man:  ')
except EOFError:
    print 'Common man its an EOFError'
else:
    print ('This is the text you entered {} :'.format(text))
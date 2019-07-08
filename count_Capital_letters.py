#finding count of how many uppercase letters in a text file
filename = '/Users/mohanpraveenhazaru/Desktop/testtext.txt'
with open(filename,'rb') as f:
    count = 0
    data =f.readlines()
    for word in data:
        if word.isupper():
            count =count+1
            print count


class birds():
    count = 0
    def __init__(self, name):
        self.name= name
        birds.count += 1

    def speak(self):
        print ('This bird {} speaks very well and the coount is {}'.format(self.name,self.count))


rover = birds("Rover")
spot = birds("Spot")
rover.speak()
spot.speak()
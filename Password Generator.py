import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

print ("Choose from these!")
print ("Random String is ", randomString() )
print ("Random String is ", randomString(10) )
print ("Random String is ", randomString(8) )

import random

for i in range(1,10):
    print random.randint(1,100)*5

import uuid

print uuid.uuid4()

def random_filename(size,filename,file_content):
    rand=''.join([str(uuid.uuid4().hex[:6]),filename])
    with open(rand,'w') as f:
        f.write(str(file_content)*size)
    return rand
random_filename(300,'mohan.txt','f')
import Message
import pickle
from sets import Set

users = Set([])

with open('data.txt','r') as file:
    while 1:
        try:
            m = pickle.load(file)
            users.add(m.getUID())
        except:
            break

with open('userList.txt', 'w') as file:
    for uid in users:
        file.write(str(uid)+"\n")


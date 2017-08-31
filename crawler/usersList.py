import Message
import pickle

users = []

with open('data.txt','r') as file:
    while 1:
        try:
            m = pickle.load(file)
            users.append(m.getUID())
        except:
            break

with open('userList.txt', 'w') as file:
    for uid in users:
        file.write(str(uid)+"\n")


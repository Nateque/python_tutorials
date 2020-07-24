import pickle

# # Pickling a python object

# names = ['nateq', 'ahmed', 'asef']
# with open('filename.pkl', 'wb') as fileobj:
#     pickle.dump(names, fileobj)

# Di-pickling object

with open('filename.pkl', 'rb') as fileobj:
    names = pickle.load(fileobj)
print(names)
print(type(names))
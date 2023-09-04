# Save the data from the form
import pickle

try:
    with open('form.pickle', 'rb') as handle:
        name, age, address = pickle.load(handle)
        if(name):
            print('Enter your name: ',name)
        else:
            name = input('Enter your name: ')

        if(age):
            print('Enter your age: ',age)
        else:
            age = input('Enter your age: ')

        if(address):
            print('Enter your adress: ',address)
        else:
            address = input('Enter your adress: ')

        with open('form.pickle', 'wb') as handle:
            pickle.dump((name, age, address), handle)
except:
    name = input('Enter your name: ')
    age = input('Enter your age: ')
    address = input('Enter your address: ')
    with open('form.pickle', 'wb') as handle:
        pickle.dump((name, age, address), handle)

import random


while True:
    user = input("\nSelect(r for Rock , s for scissors , p for paper , q to quit):")

    select = ['r','s','p']

    comp = random.choice(select)
    if user == 'q':
        exit()
    if user == comp:
        print('\nTie (comp :',comp,')')

    if user == select[0] and comp == select[1]:
        print('\nYou Won (comp :',comp,')')

    if user == select[1] and comp == select[0]:
        print('\nYou lose (comp :',comp,')')

    if user == select[2] and comp == select[1]:
        print('\nYou lose (comp :',comp,')')

    if user == select[1] and comp == select[2]:
        print('\nYou Won (comp :',comp,')')

    if user == select[0] and comp == select[2]:
        print('\nYou lose (comp :',comp,')')

    if user == select[2] and comp == select[0]:
        print('\nYou Won (comp :',comp,')')                               
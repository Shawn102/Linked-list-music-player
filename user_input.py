#!/usr/bin/env python
import SongApp

List = SongApp.Linked_list()
print("Welcome to your personal music library! Please enter a command." + '\n'
    "Commands are I(insert), D(delete), S(search by song name), P(print), Q(quit)")

while True:
    inp = input("\nCommand--> ")
    if inp == 'I' or inp == 'i':
        List.insert(SongApp.Song(input('Song name --> '), input('Artist --> '), input('Genre --> ')))
    elif inp == 'S' or inp == 's':
        List.search(input('Enter the name of the song to search for --> '))
    elif inp == 'D' or inp == 'd':
        List.delete(input('Enter the name of the song to be deleted --> '))
    elif inp == 'Q' or inp == 'q':
        List.deleteAll()
        break
    elif inp == 'P' or inp == 'p':
        List.printList() 
    else:
        print("Invalid Command !")
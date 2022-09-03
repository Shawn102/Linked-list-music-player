class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Song:        
    def __init__(self, title_, artist, genre):
        self.title_ = title_
        self.artist = artist
        self.genre = genre
    def __str__(self):
        return f'{self.title_}\n{self.artist}\n{self.genre}\n'
    
class Linked_list:
    def __init__(self):
        self.head = None

    def insert(self, new_data):
        #check to see if a song already exist:
        current = self.head
        found = False
        new_node = Node(new_data)
        while current != None and not found:
            if current.data.title_ == new_data.title_:
                found = True
            else:
                current = current.next
        if found:
                print("A song with the name " + "'" + new_data.title_ + "'" + " is already in the music library. No new song entered")
        else:
            new_node.next = self.head
            self.head = new_node
            

    def search(self, data):
        current = self.head
        found = False
        while current != None and not found:
            if current.data.title_ == data:
                print("The song name " + "'" + current.data.title_ + "'" + " was found in the music library")
                found = True
            else:
                current = current.next
        if not found:
            print("The song name " + "'" + data + "'" + " was not found in the music library" )

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.data.title_ == data:
                found = True
            else:
                previous = current
                current = current.next
        if found and previous == None:
            print("Deleting a song with name " + "'" + current.data.title_ + "'" + " from the music library")
            self.head = current.next
        elif found:
            previous.next = current.next
            print("Deleting a song with name " + "'" + current.data.title_ + "'" + " from the music library")
        else:
            print("The song name " + "'" + data + "'" + " not found in the music library")

    def deleteAll(self):
        current = self.head
        while current != None:
            print("Deleting a song with name " + "'" + str(current.data.title_) + "'" + " from the music library")
            current = current.next
            self.head = current
        print("The music library is empty")

    def printList(self):
        temp = self.head
        if temp == None:
            print("The music library is empty.")
        else:
            print("My Personal Music Library: ")
        while(temp):
            print(str(temp.data))
            temp = temp.next

if __name__=='__main__':
    List = Linked_list()

    #insertion:
    song1 = Song('I want to break free', 'Queen', 'Rock')
    List.insert(song1)
    song2 = Song('Dark necessities', 'Red Hot Chilli Peppers', 'Punk Rock')
    List.insert(song2)
    song3 = Song('Hey Jude', 'The Beatles', 'Rock')
    List.insert(song3)
    song4 = Song('Photograph', 'Ed Sheeran', 'Pop')
    List.insert(song4)
    song5 = Song('Circles', 'Post Malone', 'Pop rock')
    List.insert(song5)

    #Deletion:
    #List.deleteAll()
    #List.delete('Circle')

    #searching:
    #List.search('I want to break free')
    
    #list printing:
    List.printList()


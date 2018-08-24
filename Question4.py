'''
Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
Make methods to 
1. Display-Display the details. 
2. Add- Add the movie details.
'''

class MovieDetails:
    
    def __init__(self, Artist_Name, Yr_of_rel, Rating):
        
        self.Artist_Name = Artist_Name
        self.Yr_of_rel = Yr_of_rel
        self.Rating = Rating

    def AddDetails(self):
        self.Artist_Name = input("Enter artist's name: ")
        self.Yr_of_rel = input("Enter the Year of Release: ")
        self.Rating = input("Enter rating for the movie (Out of 10): ")

    def Display(self):
        print(" ")
        print("MOVIE DETAILS:")
        print("\tArtist's Name: ", self.Artist_Name)
        print("\tYear of release: ", self.Yr_of_rel)
        print("\tMovie Rating: ", self.Rating)

md1 = MovieDetails('x', 2000, 5)

md1.AddDetails()
md1.Display()
        
        

        

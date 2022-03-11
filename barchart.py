
from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]


plt.bar(range(len(movies)), num_oscars)      #plot x axis as movies name and heights as num_oscars

plt.title("My Favourite Movies ")            #add a title

plt.ylabel("# of Academy Awards")            #add label 

                                            
#label x axis with movie names as bar's centers.
plt.xticks(range(len(movies)), movies)

plt.show()


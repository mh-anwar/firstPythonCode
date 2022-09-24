import matplotlib.pyplot as plt
plt.title("Favourite music types (ages 12-18)") 

music_types = ["Rock","Rap","Talk","Country","Top 40"]
numpeople = [100,200,50,50,100]

plt.pie(numpeople, labels = music_types)

plt.show()

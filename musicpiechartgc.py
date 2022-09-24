import matplotlib.pyplot as plt
plt.title("Favourite Music Types (Kids Ages 12-18)") 

music_types = ["Rock","Rap","Talk","Country","Top 40"]
numpeople = [100,200,50,50,100]

plt.pie(numpeople, labels = music_types,colors =['royalblue','navy','lightsteelblue','cornflowerblue','indigo'], autopct="%1.1f%%")
plt.axis('equal')
plt.show()

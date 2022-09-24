import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,5))


musictypes = ["Rock", "Rap", "Top 40", "Talk","Country"]

likes = [80,160,70,140,50]
positions = [0,1,2,3,4]
plt.bar(positions, likes, width=0.5, color='0.75')
plt.yticks(color="grey",fontsize=12)
plt.xticks(positions, musictypes, color="grey",fontsize=12)
plt.grid()

plt.xlabel("Music Types",fontsize=16)
plt.ylabel("Number of kids",fontsize=16)

plt.title("Favorite Music Types (Kids, Ages 12-18)",fontsize=18)
plt.show()

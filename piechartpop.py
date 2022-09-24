import matplotlib.pyplot as plt
plt.title("Student Population Growth R.M.P.S")

years = [2010,2011,2012,2013,2014,2015,2016,2017,2018]
population = [534,562,582,596,617,631,654,695,725]

plt.pie(population, labels = years, colors =
['royalblue','navy','lightsteelblue','cornflowerblue','indigo','slateblue','blue','mediumblue','mediumslateblue'],startangle= 90, autopct = "%1.1f%%")
plt.axis('equal')

plt.show()

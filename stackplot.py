import matplotlib.pyplot as plt

plt.title("Student Population Growth R.M.P.S", fontsize = 20,color = 'r')
plt.xlabel("Year",fontsize = 20,color = 'r')
plt.ylabel("Population", fontsize = 20, color = 'r')

year = [2010,2011,2012,2013,2014,2015,2016,2017,2018]

school_pop = [534,562,582,596,617,631,654,695,725]

plt.stackplot(year,school_pop, color =['c'])
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

points = [
    (0, 2010),
    (200, 2012),
    (400,2012),
    (600,2014),
    (800,2016),
]
plt.yticks(range(0, 800, 50))
plt.xticks(range(min(year) , max(year)+1, 1))
#x = list(map(lambda x: x[0], points))
#y = list(map(lambda x: x[1], po)

plt.grid()

plt.rc('font', **font)
plt.show()

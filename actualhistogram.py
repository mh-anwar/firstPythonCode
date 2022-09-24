import matplotlib.pyplot as plt
import numpy as np

heights =['100-120','121-140','141-160','161-180','181-200','201-220','221-240','241-260','261-280','281-300','301-320','321-340']

heights = np.arange(100,340)

plt.hist(heights,bins=20)

plt.show()

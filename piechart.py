import matplotlib.pyplot as plt 
plt.title("Student Population Growth R.M.P.S", fontsize = 20,color = 'r')

height1 = [121-140]
height2 = [141-160]
height3 = [161-180]
height4 = [181-200]
height5 = [201-220]
height6 = [221-240]
height7 = [241-260]
height8 = [261-280]
height9 = [281-300]
height10 = [301-320]
height11 = [321-340]

frequency = [4,5,7,5,5,6,9,10,5,9,12,11]
heights =['100-120','121-140','141-160','161-180','181-200','201-220','221-240','241-260','261-280','281-300','301-320','321-340']


plt.pie(heights, labels= frequency)

plt.show()

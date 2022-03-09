from matplotlib import pyplot as plt

from collections import Counter
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

#bucket grades by decile put them 100 as 90's.

histogram =  Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x+5 for x in histogram.keys()], histogram.values() , 10, edgecolor = (0,0,0))

 # Give each bar its correct height . Give each bar a width of 10 .Black edges for each bar

plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])         # x-axis from -5 to 105,
                                                # y-axis from 0 to 5

plt.xlabel("decile")

plt.ylabel("# of students")

plt.title("distribution of Exam 1 grades")


plt.show()

plt.savefig(histogram)
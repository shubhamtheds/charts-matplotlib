from matplotlib import pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

ax.set_title("SQUARES", fontsize=20)
ax.set_xlabel("values", fontsize=14)
ax.set_ylabel("squares of values", fontsize=14)

ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 1100, 0, 1100000])

plt.savefig('squares.png', bbox_inches='tight')



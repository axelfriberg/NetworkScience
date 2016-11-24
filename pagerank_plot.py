import matplotlib.pyplot as plt

y = [0.25, 0.25, 0.25, 0.25]
N = len(y)
x = range(N)
plt.bar(x, y, align='center', width=0.5)
ticks = ['A', 'B', 'C', 'D']
plt.xticks(x, ticks)
plt.ylim(0, 1)
plt.savefig("PageRankInitialValues.png")
plt.clf()

y = [0.75, 0.125, 0, 0.125]
plt.bar(x, y, align='center', width=0.5)
plt.xticks(x, ticks)
plt.ylim(0, 1)
plt.savefig("PageRankIteration1Values.png")

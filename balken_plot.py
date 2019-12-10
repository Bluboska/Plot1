import matplotlib.pyplot as plt
import numpy as np

objects = ('Target', 'Target', 'Target', 'Target', 'Target', 'Target', 'Target')
y_pos = np.arange(len(objects))
performance = [240,200,175,160,140,135,120]
x_ticks = np.linspace(0, 500,5)

plt.barh(y_pos, performance, align='center', alpha=0.5, color='green')
plt.yticks(y_pos, objects)
plt.xticks(x_ticks)
plt.xlabel('Usage')
plt.title('Programming language usage')

plt.show()

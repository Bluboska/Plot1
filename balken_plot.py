import matplotlib.pyplot as plt
import numpy as np

objects = ('Target', 'Target', 'Target', 'Target', 'Target', 'Target', 'Target')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1,7]

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Usage')
plt.title('Programming language usage')

plt.show()

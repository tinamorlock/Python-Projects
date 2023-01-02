import numpy as np
cleaning_tasks = ['dishes', 'laundry', 'dusting', 'vaccuuming']
for i in cleaning_tasks:
    print('Have you done the {} today?'.format(i))
print('You only need to do the {} {} time(s) today.'.format(cleaning_tasks[0], cleaning_tasks.count(cleaning_tasks[0])))

print(np.sort(cleaning_tasks))

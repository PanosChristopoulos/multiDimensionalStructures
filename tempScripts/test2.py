import matplotlib.pyplot as plt

data = {'KDTree': 0.0004134178161621094, 'Quad Tree': 0.004954338073730469, 'Range Tree': 0.007526874542236328, 'R Tree': 0.002845287322998047}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Insert Speed')


plt.show()


data = {'KDTree': 0.25925925925925924, 'Quad Tree': 0.16129032258064516, 'Range Tree': 0.2692307692307692, 'R Tree': 0.3333333333333333}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('LSH Similarity')


plt.show()


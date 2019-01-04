import numpy as np
np.random.seed(123) #so that the result is reproducible
#random generators
print(np.random.rand()) #a float number between 0 and 1
print(np.random.randint(1,7)) #an integer between 1 and 6

#random walk experiment
all_walks = []
# Simulate random walk 10 times
for i in range(1000):
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(step - 1, 0) #step can't go below 0
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        fallchance = np.random.rand()
        if fallchance <= 0.001:
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

#visualize it
import matplotlib.pyplot as plt
np_aw = np.array(all_walks)
np_aw_t = np.transpose(np_aw) #переворачивает массив, теперь его первый список состоит из первых элементов изначальных списков, второй -из вторых и т.д.
#это нужно, потому что по дефолту в графике на оси y индексы, значит, одно наблюдение будет состоять из элементов одного индекса, принадлежащих разным спискам
plt.plot(np_aw_t)
plt.show()

#visualize the last step
ends = np_aw_t[-1] #список с последними шагами
plt.hist(ends)
plt.show()

#chance of getting 60 steps up or higher
np.mean(ends >= 60)

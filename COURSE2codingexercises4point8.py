import matplotlib.pyplot as plt

country = east_asia['Country']

population = east_asia['Population(2020)']

fig = plt.figure(figsize=(16,10))

plt.barh(country,population)
plt.title('2020 Population by country (EAST ASIA')

plt.show()
    
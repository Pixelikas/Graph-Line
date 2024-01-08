import matplotlib.pyplot as plt

dataOne = [3, 6, 5, 8]
dataTwo = [2, 6, 2, 7]

fig, simple_chart = plt.subplots()

plt.title('Intenções de Voto')

plt.xlabel("Dias")
plt.ylabel("Pecentual Votos")

simple_chart.plot(dataOne)
simple_chart.plot(dataTwo)

plt.show()
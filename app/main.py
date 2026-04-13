import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(cases):
        # Simulamos lanzar la moneda 10 veces (True=Cara, False=Cruz)
        heads_count = sum(random.random() < 0.5 for _ in range(10))
        results[heads_count] += 1

    # Convertimos las frecuencias en porcentajes
    return {k: (v / cases) * 100 for k, v in results.items()}


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    # Preparamos los datos para el gráfico
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.plot(x_values, y_values, marker="o")

    # Añadimos etiquetas y título
    plt.title("Coin Toss Gaussian Distribution")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(True)

    plt.show()

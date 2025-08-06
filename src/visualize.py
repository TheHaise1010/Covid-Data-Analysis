import matplotlib.pyplot as plt
import seaborn as sns


def plot_country_trend(df, countries):
    sns.set(style="whitegrid")
    plt.figure(figsize=(12, 6))

    for country in countries:
        plt.plot(df.index, df[country], label=country)

    plt.xlabel("Fecha")
    plt.ylabel("Casos confirmados")
    plt.title("Evolución de casos COVID-19")
    plt.legend()
    plt.tight_layout()
    plt.savefig("outputs/casos_covid19.png")
    plt.show()

import numpy as np


def intensywność(t):
    """Funkcja intensywności od argumentu t."""
    return 1 / (t + 1)


def czas_oczekiwania(lambdaa=1, T=2 * np.pi):
    """Generowanie czasów oczekiwania niejednorodnego procesu Poissona metodą rozrzedzania."""

    s = []  # deklaracja wartości początkowych
    t = 0
    i = 0
    while True:  # algorytm rozrzedzania
        u1 = np.random.random()
        t -= np.log(u1) / lambdaa
        if t > T:
            break
        u2 = np.random.random()
        if u2 <= intensywność(t):
            i += 1
            s = np.append(s, t)
    return s  # zwracanie czasów oczekiwania


if __name__ == "__main__":
    wynik = czas_oczekiwania()  # generowanie czasów oczekiwania
    print(wynik)  # wyświetlanie wyników na ekran

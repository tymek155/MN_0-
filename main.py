import math

def metoda_prostokatow(f, przedzial, liczba_przedz):
    b = przedzial[1]
    a = przedzial[0]
    elem_s = ((b-a)/liczba_przedz)

    wynik = 0;
    x = a
    for i in range(liczba_przedz):
        wynik += f(x + 0.5*elem_s)
        x += elem_s

    return elem_s * wynik

def metoda_trapezow(f, przedzial, liczba_przedz):
    b = przedzial[1]
    a = przedzial[0]
    elem_s = ((b-a)/liczba_przedz)
    kroki = []
    kroki.append(a)
    for i in range(liczba_przedz):
        a += elem_s
        kroki.append(a)

    wynik = 0
    for n in range(liczba_przedz):
        h = kroki[n+1]- kroki[n]
        podstawy = (f(kroki[n])+ f(kroki[n+1]))
        wynik += h*podstawy*0.5
    return wynik

def metoda_simpsona(f, przedzial):
    b = przedzial[1]
    a = przedzial[0]

    return (((b-a)/6)*(f(a)+4*f((a+b)/2)+f(b)))

def f1(x):
    return math.sin(x)

def f2(x):
    return x*x + 2*x + 5

def f3(x):
    return math.exp(x)


def main():
    przedzial_calk = [0.5,5]
    liczba_przedz = 4
    print(f"Przedzial calkowania: {przedzial_calk}")
    print(f"Liczba przedzialow: {liczba_przedz}")
    print(f"Wynik metoda prostokatow: {metoda_prostokatow(f3, przedzial_calk, liczba_przedz)}")
    print(f"Wynik metoda trapezow: {metoda_trapezow(f3, przedzial_calk, liczba_przedz)}")
    print(f"Wynik metoda Simpsona: {metoda_simpsona(f3, przedzial_calk)}")


if __name__ == '__main__':
    main()
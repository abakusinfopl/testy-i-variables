def task1(a,b):
    """
    Function that calculates sum of two argument values

    Input: two integers
    Output: one integers
    """
    if type(a) == str and type(b) == str:
        a = int(a)
        b = int(b)
    return int(a+b)


def task2(a):
    """
    Function that calculates square value of argument

    Input: one integer
    Output: one integer
    """
    return a**2

    #return iloczyn


def task3(s1, s2):
    """
    Functions which accepts two numbers as string (separated by comma) and generates a string with the result of
    their addition.

    Input: n,m -> strings
    Output: string
    """
    liczba_1 = int(s1)
    liczba_2 = int(s2)
    wynik = liczba_1 + liczba_2
    wynik_str = str(wynik)
    return wynik_str


def task4(m: int, n: int) -> str:
    """
    Functions which accepts a two numbers as int and generates a string with their concatination (e.g.  3,4 -> 34)

    Input: two integers
    Output: string
    """
    m_str = str(m)
    n_str = str(n)
    mn_str = m_str + n_str
    return mn_str


def task5(b: float) -> str:
    """
    Function that calculates area of an equilateral triangle. Suare root of 3 is 1.732. It returns the area as string
    that has two numbers after comma.

    Input: N -> float number
    Output: area of triangle as string such as: "1.23"
    """
    pole = (1.732/2) * b ** 2
    pole_str = f"{pole:.2f}"
    return pole_str

def dzielenie(a,b):
    return a/b

def task7(a: float, b: float) -> str:
    """
    Function that calculates an area of a right triangle with two sides - a and b (just like Pitagoras triangle).
    Return the area as string that has two numbers after comma.

    Input: a,b -> int numbers
    Output: area of triangle as string such as: "1.23"
    """
    pole = a * b / 2
    pole_str = f"{pole:.2f}"
    return pole_str


def task8(lancuch: str) -> bool:
    """
    Function that receives a sequence of space separated 4 single digits (e.g. '1 2 3 4') as input and then check
    whether they as one number (1234) is divisible by 5 or not.

    Input: string with 4 digits
    Output: Boolean value (True or False)
    """
    pierwsza = lancuch[0] #"1"
    druga = lancuch[2]    #"2"
    trzecia = lancuch[4]
    czwarta = lancuch[6]
    razem = pierwsza + druga + trzecia + trzecia + czwarta # "1234"
    razem_liczba = int(razem)
    if razem_liczba % 5 == 0:
        return True
    else:
        return False



def task9(a: int) -> int:
    """
    Function that computes the value of a+aa+aaa+aaaa with a given digit as the value of a

    Input: digit as integer
    Output: number as integer
    """
    pierwsza = a
    druga = int(str(a)*2)
    trzecia = int(str(a) * 3)
    czwarta = int(str(a) * 4)
    wynik = pierwsza + druga + trzecia + czwarta
    return wynik


def task10(number: int) -> None:
    """
    Function that take an integer number as string and print the "It is an even number" if the number is even,
    otherwise print "It is an odd number".

    Input: number
    Output: None
    """
    if number % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
    return None


if __name__ == '__main__':
    cyfra = 1
    wynik = task9(cyfra)
    print(f"Wynik to: {wynik}")
    print(type(wynik))

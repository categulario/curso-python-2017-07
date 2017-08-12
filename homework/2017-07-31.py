def decorador(otrafuncion):
    def envoltura(x, y):
        print('antes')
        valor = otrafuncion((x+5), y)
        print('despues')
        return valor

    return envoltura

@decorador
def f(x, y):
    return x + y

if __name__ == '__main__':
    assert f(5, 0) == 10
    assert f(5, -5) == 5
    assert f(8, 2) == 15

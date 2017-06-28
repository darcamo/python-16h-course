


# Preços de água para cada faixa de consumo
agua_residencial_normal = {10: 2.79,
                           15:3.61,
                           20:3.92,
                           50:6.71,
                           "inf": 11.86}
esgoto_residencial_normal = {10: 3.09,
                             15:3.97,
                             20:4.30,
                             50:7.38,
                             "inf": 13.04}



def dobra(x):
    """
    Dobra o valor da entrada

    Parâmetros
    ----------
    x : número
        O valor a ser dobrado

    Retorno
    -------
    número
        O dobro da entrada
    """
    return 2*x



def calc_faixas_consumo(consumo):
    """
    Quebra um consumo total nas 5 faixas de consumo (valores inteiros)
    definidas pela Cagece.

    As faixas são:
        0  < x <= 10
        11 < x <= 15
        15 < x <= 20
        20 < x <= 50
        x > 50

    Parâmetros
    ----------
    consumo : int
        O consumo que deve ser quebrado em faixas

    Retorno
    -------
    list[int]
        Uma lista contendo os valores de consumo em cada faixa.
    """
    return [0] * 5


def calc_custo_agua(consumo):
    """Calcula o valor a ser pago de água

    Parâmetros
    ----------
    consumo : int
        O consumo de água em metros cúbicos (inteiros)

    Retorno
    -------
    float
        O valor a ser pago pela água"""
    return 0


def calc_custo_esgoto(consumo):
    """
    Calcula o valor a ser pago de esgoto.

    O consumo de esgoto em metros cúbicos é calculado como 80% do consumo de
    água. Após isso, o consumo é quebrado nas mesmas faixas que o consumo de
    água, mas os valores cobrados são diferentes.

    Parâmetros
    ----------
    consumo : int
        O consumo de água em metros cúbicos (inteiros)

    Retorno
    -------
    float
        O valor a ser pago pela água
    """
    consumo_esgoto = (0.8 * consumo)

    return 0

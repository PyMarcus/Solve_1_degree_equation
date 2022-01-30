import multiprocessing


class Solve:
    """Classe para resoluçao de equacoes de 1 ordem"""
    @staticmethod
    def equ(equacao: str) -> list:
        """Informe a equaçao na forma de strings. ex: 2x + 1 = 3x + 2"""
        expressao: list = equacao.split()
        lado_esquerdo: list = [expressao[termo] for termo in range(expressao.index('=')) if expressao[termo] != '+' and expressao[termo] != '-' and expressao[termo] != '*' and expressao[termo] != '/']
        lado_direito: list = [expressao[termo] for termo in range(expressao.index('=') + 1, len(expressao)) if expressao[termo] != '+' and expressao[termo] != '-' and expressao[termo] != '*' and expressao[termo] != '/']
        icognita: list = list()
        coeficientes: list = list()
        for termo in lado_direito:
            if 'x' in termo and '-' not in termo:
                icognita.append('-' + termo)
            elif 'x' in termo and '-' in termo:
                icognita.append(termo.replace('-', ''))
        for termo in lado_esquerdo:
            if 'x' in termo:
                icognita.append(termo)
            elif 'x' in termo:
                icognita.append(termo)
        # coeficientes
        for termo in lado_direito:
            if 'x' not in termo:
                coeficientes.append(float(termo))
            elif 'x' not in termo:
                coeficientes.append(float(termo))
        for termo in lado_esquerdo:
            if 'x' not in termo and '-' not in termo:
                coeficientes.append(float('-' + termo))
            elif 'x' not in termo and '-' in termo:
                coeficientes.append(float(termo.replace('-', '')))
        return icognita, coeficientes

    @staticmethod
    def sum_(equacao: str) -> None:
        icognitas, coeficientes = Solve.equ(equacao)
        numeros: list = [float(termo.replace('x', '')) for termo in icognitas]
        resultado: float = sum(coeficientes) / sum(numeros)
        print(f"= {resultado}")

    @staticmethod
    def solve(equacao: str) -> list:
        mp = multiprocessing.Process(target=Solve.sum_, args=(equacao,))
        mp.start()
        mp.join()


if __name__ == '__main__':
    Solve.solve(input('Informe a equação: '))

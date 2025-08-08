##  Wyctor Fogos da Rocha ##
import sys

def load_text_content():
    ## Carregamento dos dados via stdin
    return sys.stdin.read()

def preprocessing_data(data_context: str):
    lines = data_context.strip().split("\n")
    n, t = map(int, lines[0].split())
    a = list(map(int, lines[1].split()))
    return n, t, a

def verifyCondition(n, m):
    ''''
        Verificar a conexidade do grafo, pois o problema pode ser representado como um grafo completamente conexo
    '''
    if ((n<0) or (n>100)):
        print("O 'n' está além dos limites!\n")
        return False
    # Verificação 
    if ((m<0) and (m>((n*(n-1))/2))):
        print("O 'm' está além dos limites!\n")
        return False
    return True


def can_reach_target(n, t, a):
    pos = 1
    while pos < t:
        pos += a[pos - 1]  # a[0] é salto da célula 1
    return "YES" if pos == t else "NO"

if __name__ == "__main__":
    raw_data = load_text_content()
    n, t, a = preprocessing_data(raw_data)
    result = can_reach_target(n, t, a)
    sys.stdout.write(str(result) + '\n')
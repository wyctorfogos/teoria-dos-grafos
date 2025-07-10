def load_text_content(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def preprocessing_data(data_context: str):
    lines = data_context.strip().split("\n")
    n, t = map(int, lines[0].split())
    a = list(map(int, lines[1].split()))
    return n, t, a

def can_reach_target(n, t, a):
    pos = 1
    while pos < t:
        pos += a[pos - 1]  # a[0] é salto da célula 1
    return "YES" if pos == t else "NO"

if __name__ == "__main__":
    file_path = "./trabalho-2/questoes/data/questao_2/input_1.txt"
    raw_data = load_text_content(file_path)
    n, t, a = preprocessing_data(raw_data)
    result = can_reach_target(n, t, a)
    print(result)

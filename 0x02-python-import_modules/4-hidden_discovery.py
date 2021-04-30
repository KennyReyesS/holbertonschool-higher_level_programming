#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lista = dir(hidden_4)
    for i in range(0, len(lista)):
        if str(lista[i])[:1] == '_':
            print(end="")
        else:
            print(lista[i])

def fatorial(n):
    resultado = n
    if(n == 1):
        return resultado
    else:
        resultado += fatorial(n - 1)
    return resultado 

def main():
    print(fatorial(6))

if __name__ == "__main__":
    main()
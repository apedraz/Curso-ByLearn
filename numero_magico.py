def main():

    n_escolhido = 2
    n_usuario = int(input("Escolha um número de 1 a 5: "))

    if n_escolhido < n_usuario:
        print('Você essou! Escolha um número menor.')
    elif n_escolhido > n_usuario:
        print('Você essou! Escolha um número maior.')
    else:
        print('Você acertou!')

main()
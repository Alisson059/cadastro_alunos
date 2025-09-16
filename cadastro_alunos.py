# Programa de cadastro de alunos em uma escola
# Permite adicionar alunos, calcular a média das notas, excluir alunos e visualizar todos os alunos cadastrados
# Utiliza listas e dicionários para armazenar os dados dos alunos



escola = [] # Lista que armazenará todos os alunos cadastrados

while True:
    pessoa = input("Digite adicionar, exluir ou sair: ").lower() # Pergunta ação do usuário

    if pessoa == "adicionar":

        while True: # Loop para adicionar múltiplos alunos consecutivamente

            aluno = {} # Dicionário para armazenar os dados de cada aluno

            aluno["nome"] = input("Digite o nome: ").lower()
            aluno["sexo"] = input("Digite o sexo: ").lower()
            aluno["idade"] = int(input("Digite o idade: "))

            # Pergunta se deseja calcular a média do aluno
            pro = input("Deseja Calcular a media do aluno? [S/N] ").lower()

            if pro == "s":
                notas = {} # Dicionário para armazenar as notas do aluno

                notas["portugues"] = float(input("Digite a notas do aluno na materia de portugues: "))
                notas["matematica"] = float(input("Digite a notas do aluno na materia de Matematica: "))
                notas["história"] = float(input("Digite a notas do aluno na materia de História "))
                notas["geografia"] = float(input("Digite a notas do aluno na materia de Geografia: "))
                notas["física"] = float(input("Digite a notas do aluno na materia de Física: "))
                notas["química"] = float(input("Digite a notas do aluno na materia de Química: "))
                notas["educação Física"] = float(input("Digite a notas do aluno na materia de Educação Física: "))

                aluno["notas"] = notas # Adiciona o dicionário de notas ao aluno
                aluno["media"] = sum(notas.values()) / len(notas) # Calcula a média das notas

                escola.append(aluno) # Adiciona o aluno à lista da escola

                print(f"A média do aluno[a] {aluno['nome']} é {aluno['media']:.2f}")

            # Pergunta se deseja adicionar outro aluno
            continuar = input("Deseja adicionar outra pessoa? (s/n): ").lower()
            if continuar == "n":
                break

    elif pessoa == "excluir":
        # Solicita o nome do aluno que deseja remover
        aluno_remover = input("Digite o nome do aluno que deseja excluir: ").lower()

        # Procura o aluno na lista
        for aluno in escola:
            if aluno["nome"] == aluno_remover:
                escola.remove(aluno)# Remove o aluno encontrado
                print(f"{aluno_remover} removido com sucesso!")
                break
        else:
            # Caso nenhum aluno seja encontrado com o nome digitado
            print("Aluno não encontrado!")

    elif pessoa == "sair":
        # Encerra o programa
        print("Encerrando o programa... ")

        print("\n--- Lista de pessoas cadastradas ---")
        for lista_escola in escola:

            # Mostra todos os dados do aluno, incluindo a média caso exista
            media = lista_escola.get("media", "Não calculada") # Usa get para evitar erro se não tiver média
            print(f"nome: {lista_escola['nome']}, sexo: {lista_escola['sexo']} ,"
                  f"idade: {lista_escola['idade']}, nota: {lista_escola['media']:.2f}")
        break

    else:
        # Caso o usuário digite uma opção inválida
        print("Opção inválida! Digite 'adicionar', 'excluir' ou 'sair'.")

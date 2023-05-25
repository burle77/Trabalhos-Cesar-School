import os

BancoDados = "transacoes.csv"

moedas = {}


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def ler_transacoes():
    try:
        with open(BancoDados, "r") as arquivo:
            linhas = arquivo.readlines()
            transacoes = [linha.strip().split(",") for linha in linhas]
        return transacoes
    except FileNotFoundError:
        return []
    except IOError:
        print("Erro ao ler o arquivo de transações.")
        return []


def escrever_transacoes(transacoes):
    try:
        with open(BancoDados, "w") as arquivo:
            for transacao in transacoes:
                linha = ",".join(transacao)
                arquivo.write(linha + "\n")
    except IOError:
        print("Erro ao escrever no arquivo de transações.")


def adicionar_transacao():
    try:
        nome = input("Nome da transação: ")
        categoria = input("Categoria da transação: ")
        valor = input("Valor da transação: ")

        transacoes = ler_transacoes()
        transacoes.append([nome, categoria, valor])
        escrever_transacoes(transacoes)

        print("Transação adicionada com sucesso!")
    except ValueError:
        print("Valor inválido para a transação. Certifique-se de inserir um número válido.")
    except IOError:
        print("Erro de E/S ao ler ou escrever no arquivo de transações.")
    except Exception as e:
        print("Ocorreu um erro ao adicionar a transação:", str(e))


def listar_transacoes():
    try:
        transacoes = ler_transacoes()

        if not transacoes:
            print("Nenhuma transação encontrada.")
            return

        print("\nTransações:")
        for transacao in transacoes:
            nome, categoria, valor = transacao
            print(f"Nome: {nome}\tCategoria: {categoria}\tValor: {valor}")
    except FileNotFoundError:
        print("Arquivo de transações não encontrado.")
    except IOError:
        print("Erro de E/S ao ler o arquivo de transações.")
    except Exception as e:
        print("Ocorreu um erro ao listar as transações:", str(e))

def deletar_transacao():
    try:
        nome = input("Nome da transação a ser deletada: ")

        transacoes = ler_transacoes()
        transacoes = [transacao for transacao in transacoes if transacao[0] != nome]
        escrever_transacoes(transacoes)

        print("Transação deletada com sucesso!")
    except FileNotFoundError:
        print("Arquivo de transações não encontrado.")
    except IOError:
        print("Erro de E/S ao ler ou escrever no arquivo de transações.")
    except Exception as e:
        print("Ocorreu um erro ao deletar a transação:", str(e))


def filtrar_transacoes_por_categoria():
    try:
        categoria = input("Digite a categoria para filtrar as transações: ")

        transacoes = ler_transacoes()
        transacoes_filtradas = [transacao for transacao in transacoes if transacao[1] == categoria]

        if not transacoes_filtradas:
            print("Nenhuma transação encontrada nessa categoria.")
            return

        print(f"\nTransações da categoria '{categoria}':")
        for transacao in transacoes_filtradas:
            nome, _, valor = transacao
            print(f"Nome: {nome}\tValor: {valor}")
    except Exception as e:
        print("Ocorreu um erro ao filtrar as transações por categoria:", str(e))


def mostrar_extrato():
    try:
        transacoes = ler_transacoes()

        if not transacoes:
            print("Nenhuma transação encontrada.")
            return

        extrato = {}

        for transacao in transacoes:
            _, categoria, valor = transacao
            if categoria not in extrato:
                extrato[categoria] = 0
            extrato[categoria] += float(valor)

        print("\nExtrato por categoria:")
        for categoria, valor_total in extrato.items():
            print(f"Categoria: {categoria}\tTotal: {valor_total}")
    except FileNotFoundError:
        print("Arquivo de transações não encontrado.")
    except IOError:
        print("Erro de E/S ao ler o arquivo de transações.")
    except Exception as e:
        print("Ocorreu um erro ao mostrar o extrato:", str(e))


def adicionar_taxa_cambio():
    try:
        moeda = input("Digite o código da moeda: ")
        taxa = float(input(f"Digite a taxa de câmbio para {moeda}: "))
        moedas[moeda] = taxa
    except ValueError:
        print("Valor inválido para a taxa de câmbio. Certifique-se de inserir um número válido.")


def mostrar_extrato_em_moeda():
    try:
        transacoes = ler_transacoes()

        if not transacoes:
            print("Nenhuma transação encontrada.")
            return

        extrato = {}

        for transacao in transacoes:
            _, categoria, valor = transacao
            if categoria not in extrato:
                extrato[categoria] = 0
            extrato[categoria] += float(valor)

        print("\nExtrato bancário por categoria:")
        for categoria, valor_total in extrato.items():
            valor_convertido = converter_moeda(valor_total)
            print(f"Categoria: {categoria}\tTotal: {valor_convertido:.2f}")
    except FileNotFoundError:
        print("Arquivo de transações não encontrado.")
    except IOError:
        print("Erro de E/S ao ler o arquivo de transações.")
    except Exception as e:
        print("Ocorreu um erro ao mostrar o extrato em moeda:", str(e))


def converter_moeda(valor):
    moeda = input("Digite a moeda desejada para conversão: ")
    taxa_cambio = moedas.get(moeda)

    if taxa_cambio is None:
        print("Moeda não suportada.")
        return valor

    try:
        valor_convertido = valor / taxa_cambio
        return valor_convertido
    except ZeroDivisionError:
        print("Erro ao converter a moeda. Certifique-se de que a taxa de câmbio seja diferente de zero.")
        return valor


def menu():
    while True:
        try:
            limpar_tela()
            print("== Rastreamento de Despesas Pessoais ==")
            print("1. Adicionar transação")
            print("2. Listar transações")
            print("3. Deletar transação")
            print("4. Filtrar transações por categoria")
            print("5. Mostrar extrato por categoria")
            print("7. Adicionar taxa de câmbio")  
            print("6. Mostrar extrato bancário por categoria em outra moeda") 
            print("0. Sair do programa")

            opcao = input("\nDigite a opção desejada: ")

            if opcao == "1":
                limpar_tela()
                adicionar_transacao()
            elif opcao == "2":
                limpar_tela()
                listar_transacoes()
            elif opcao == "3":
                limpar_tela()
                deletar_transacao()
            elif opcao == "4":
                limpar_tela()
                filtrar_transacoes_por_categoria()
            elif opcao == "5":
                limpar_tela()
                mostrar_extrato()
            elif opcao == "6":  # Alterado para 6
                limpar_tela()
                mostrar_extrato_em_moeda()
            elif opcao == "7":  # Alterado para 7
                limpar_tela()
                adicionar_taxa_cambio()
            elif opcao == "0":
                break
            else:
                print("Opção inválida! Digite novamente.")

            input("\nPressione Enter para continuar...")
        except KeyboardInterrupt:
            print("Operação interrompida pelo usuário.")
            break
        except ValueError:
            print("Valor inválido. Certifique-se de inserir um valor válido.")
        except FileNotFoundError:
            print("Arquivo de transações não encontrado.")
        except IOError:
            print("Erro de E/S ao ler ou escrever no arquivo de transações.")
        except Exception as e:
            print("Ocorreu um erro:", str(e))

    print("Encerrando o programa...")



if __name__ == "__main__":
    menu()

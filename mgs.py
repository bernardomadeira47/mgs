class Empregado:
    def __init__(self, identificador, nome, sobrenome, telefone, email, alergias, problemas_medicos):
        self.identificador = identificador
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.email = email
        self.alergias = alergias
        self.problemas_medicos = problemas_medicos

    def __str__(self):
        return (f"ID: {self.identificador}\n"
                f"Nome: {self.nome} {self.sobrenome}\n"
                f"Telefone: {self.telefone}\n"
                f"Email: {self.email}\n"
                f"Alergias: {self.alergias}\n"
                f"Problemas Médicos: {self.problemas_medicos}\n")

class SistemaMGS:
    def __init__(self):
        self.empregados = {}

    def adicionar_empregado(self, empregado):
        self.empregados[empregado.identificador] = empregado

    def obter_empregado(self, identificador):
        empregado = self.empregados.get(identificador)
        if empregado:
            return empregado
        else:
            return "Empregado não encontrado."

def coletar_informacoes():
    identificador = input("Identificador: ")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    alergias = input("Alergias: ")
    problemas_medicos = input("Problemas Médicos: ")
    return Empregado(identificador, nome, sobrenome, telefone, email, alergias, problemas_medicos)

def main():
    sistema = SistemaMGS()
    while True:
        print("Escolha uma opção:")
        print("1. Adicionar empregado")
        print("2. Consultar empregado")
        print("3. Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            empregado = coletar_informacoes()
            sistema.adicionar_empregado(empregado)
            print("Empregado adicionado com sucesso!")
        elif opcao == "2":
            identificador = input("Digite o identificador do empregado: ")
            empregado = sistema.obter_empregado(identificador)
            print(empregado)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

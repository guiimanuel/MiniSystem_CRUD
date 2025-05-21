import json
import os

aluno= []
materia1 = []
professor = []

def salvar_dados():
    with open("aluno.json","w") as f:
        json.dump(aluno, f, indent=3)
    with open("materia1.json","w") as f:
        json.dump(materia1, f, indent=3)
    with open("professor.json","w") as f:
        json.dump(professor, f, indent=4)

def carregar_dados():
  global aluno, materia1, professor
  if os.path.exists("aluno.json"):
    with open("aluno.json", "r") as f:
      aluno= json.load(f)
  else:
    aluno=[]

  if os.path.exists("materia1.json"):
    with open("materia1.json", "r") as f:
      materia1= json.load(f)
  else:
    materia1=[]

  if os.path.exists("professor.json"):
    with open("professor.json", "r") as f:
      professor= json.load(f)
  else:
    professor=[]



def exibir_menu():
    print('''
    Sistema Estudantes e Notas
    Escolha uma opção:
    1. Cadastrar um estudante
    2. Listar estudantes cadastrados
    3. Procurar dados de um estudante
    4. Alterar dados de um estudante
    5. Excluir dados de um estudante
    6. Cadastrar materias e notas do aluno
    7. Listar materias e notas dos alunos
    8. Buscar materias e notas do aluno
    9. Excluir materias e notas do aluno
    10. Alterar materias e notas do aluno
    11. Conselho de Classe
    12. ALterar situação do conselho do aluno
    13. Exibir situações dos alunos
    14. Excluir situação do aluno
    0. Sair
    ''')


#cadastrar alunos
def cadastrar(aluno):
    matricula = input('Matricula? ')
    nome = input('Nome completo? ')
    idade = input('Idade? ')
    aluno.append((matricula, nome, idade))
    salvar_dados()

#listar aluno cadastrado
def listar(aluno):
    if len(aluno) == 0:
        print('Nenhuma estudante cadastrado!')
    else:
        for pessoa in aluno:
            matricula, nome, idade = pessoa
            print(f'Nome: {nome} / Matricula: {matricula} / Idade: {idade}')


#procurar dados do aluno
def buscar(aluno):
    matricula_desejada = input('Matricula? ')
    for pessoa in aluno:
        matricula, nome, idade = pessoa
        if matricula == matricula_desejada:
            print(f'Nome: {nome} / Idade: {idade} / Matricula: {matricula}')
            break
    else:
        print(f'Estudante com matricula {matricula_desejada} não encontrada')


#excluir aluno
def excluir(aluno):
    matricula_desejada = input('Matricula? ')
    for pessoa in aluno:
        matricula, nome, idade = pessoa
        if matricula == matricula_desejada:
            print(f'Nome: {nome} / Idade: {idade} / Matricula: {matricula}')
            excluir = int(input('Para excluir, digite 1 ou 0 para ignorar? '))
            if excluir == 1:
                del aluno[aluno.index(pessoa)]
                print(f'Estudante com matricula {matricula_desejada} excluido com sucesso!')
            break
    else:
        print(f'Estudante com matricula {matricula_desejada} não encontrada')


#alterar dados do aluno
def alterar(aluno):
    matricula_desejada = input('Matricula? ')
    for pessoa in aluno:
        matricula, nome, idade = pessoa
        if matricula == matricula_desejada:
            print(f'Nome: {nome} / idade: {idade} / Matricula: {matricula}')
            novonome = input('Novo Nome? ')
            novaidade = int(input('Nova idade? '))


            confirma = int(input('Para alterar, digite 1 ou 0 para ignorar? '))
            if confirma == 1:
                aluno[aluno.index(pessoa)] = matricula, novonome, novaidade
                print(f'Nome: {novonome} / idade: {novaidade} / Matricula: {matricula}')
            break
        else:
            print(f'Estudante com matricula {matricula_desejada} não encontrado')


#Cadastrar materias e notas do aluno

def cadastrarmateria(materia1):
    matricula = input('Matricula? ')
    materia = input('Materia? ')
    nota = input('Nota? ')
    nota = int(nota)
    materia1.append((matricula, materia, nota))
    salvar_dados()
#listar materias do aluno


def listarmateria(materia1):
    if len(materia1) == 0:
        print('Nenhuma matéria cadastrada!')
    else:
        for pessoa in materia1:
            matricula, materia, nota = pessoa
            print(f'Matricula: {matricula} / Matéria: {materia} / Nota: {nota}')

def buscarmateria(materia1):
    matricula_desejada = input('Matricula? ')
    for pessoa in materia1:
        matricula, materia, nota = pessoa
        if matricula == matricula_desejada:
            print(f'Matricula: {matricula} / Matéria: {materia} / Nota: {nota}')
            break
    else:
        print(f'Estudante com matricula {matricula_desejada} não encontrada')


#excluir aluno
def excluirmateria(materia1):
    matricula_desejada = input('Matricula? ')
    for pessoa in materia1:
        matricula, materia, nota = pessoa
        if matricula == matricula_desejada:
            print(f'Matricula: {matricula} / Materia: {materia} / Nota: {nota}')
            excluir = int(input('Para excluir, digite 1 ou 0 para ignorar? '))
            if excluir == 1:
                del materia1[materia1.index(pessoa)]
                print(f'Materia do estudante de matrícula: {matricula_desejada} excluida com sucesso!')
            break
    else:
        print(f'Estudante com matricula {matricula_desejada} não encontrada')

def alterarmateria(materia1):
    matricula_desejada = input('Matricula? ')
    for pessoa in materia1:
        matricula, materia, nota = pessoa
        if matricula == matricula_desejada:
            print(f'Matricula: {matricula} / Matéria: {materia} / Nota: {nota}')
            novamateria = input('Nova matéria? ')
            novanota = int(input('Nova nota? '))


            confirma = int(input('Para alterar, digite 1 ou 0 para ignorar? '))
            if confirma == 1:
                materia1[materia1.index(pessoa)] = matricula, novamateria, novanota
                print(f'Matricula: {matricula} / Matéria: {novamateria} / Nota: {novanota}')
            break
        else:
            print(f'Estudante com matricula {matricula_desejada} não encontrado')

def Cclasse(professor, materia1, aluno):
    matriculap = input('Escolha a matricula ')
    aluno1= ""
    materia2=""
    s = ""

    for pessoa in aluno:
        matricula, nome, idade = pessoa
    
        if matriculap == matricula:
            aluno1=pessoa
    for a in materia1:
        matricula, materia, nota = a
        if matriculap == matricula:
            materia2=a
        if nota >= 6:
            a = "Aprovado"
        else:
            c = input("A nota do aluno é menor que 6, você deseja aprovar o aluno? ")
            if c == "sim":
                a = "Aprovado"
            else: 
                a = "Reprovado"
            
    n_situacao= len(professor)+1
    professor.append((aluno1, materia2, a, n_situacao))

    print(f'Aluno: {aluno1} / Materia: {materia2} / Situação do aluno: {a} / Numero de situação: {n_situacao}')
    salvar_dados()

#ALterar situação do aluno
def alterarprof(professor, materia1, aluno):  
  n_situacao2 = input('Digite o seu número de situação para confirmar qual situação de aluno deseja alterar: ')
  n_situacao2 = int(n_situacao2)
  for i in professor:
    aluno1, materia2, a, n_situacao = i
    if n_situacao2 == n_situacao:
      print(f'Aluno: {aluno1} / Materia: {materia2} / Situação do aluno: {a} / Numero de situação: {n_situacao}')
      nmatriculap = input('Digite um novo número de matrícula:')
      nmatriculap = int(nmatriculap)
      naluno1= ""
      nmateria2=""
      nn_situacao= n_situacao2
      for pessoa in aluno:
            matricula, nome, idade = pessoa
            if nmatriculap == matricula:
                naluno1=pessoa
    for a in materia1:
        matricula, materia, nota = a
        if nmatriculap == matricula:
            nmateria2=a
        if nota >= 6:
            n_a = "Aprovado"
        else:
            n_c = input("A nota do aluno é menor que 6, você deseja aprovar o aluno? ")
            if n_c == "sim":
                n_a = "Aprovado"
            else: 
                n_a = "Reprovado"
    confirma = input('Para alterar digite 1, para ignorar a alteração digite 0: ')
    confirma = int(confirma)
    if confirma == 1:
        professor[professor.index(i)] = naluno1, nmateria2, n_a, nn_situacao
        print(f'Aluno: {aluno1} / Materia: {nmateria2} / Situação do aluno: {n_a} / Numero de situação: {nn_situacao}')
        break
    else:
        print(f'Número de situação {nn_situacao} não encontrado')

def exibirSI(professor, materia1, aluno):
  if len(professor) == 0:
    print('Nenhuma situação realizada!')
  else:
    for i in professor:
      aluno1, materia2, a, n_situacao = i
      print(f'Aluno: {aluno1} / Materia: {materia2} / Situação do aluno: {a} / Numero de situação: {n_situacao}')

def excluirSI(professor, materia1, aluno):
  situacao = input('Digite o número da situação que deseja excluir: ')
  situacao=int(situacao)
  for i in professor:
    aluno1, materia2, a, n_situacao = i
    if situacao == n_situacao:
      print(f'Aluno: {aluno1} / Materia: {materia2} / Situação do aluno: {a} / Numero de situação: {n_situacao}')
      excluir = input('Para excluir digite 1, para ignorar digite 0: ')
      excluir=int(excluir)
      if excluir == 1:
        del professor[professor.index(i)]
        print(f'A situação de número {situacao} foi excluida com sucesso!')
      break
  else:
    print(f'A situação de número {situacao} não foi encontrada')

def main():
    carregar_dados()
    #professor = []
    #materia1 = []
    #aluno = []
    opcao = 1
    while opcao != 0:
        exibir_menu()
        opcao = int(input('Opção? '))
        if opcao == 1:
            cadastrar(aluno)
        elif opcao == 2:
            listar(aluno)
        elif opcao == 3:
            buscar(aluno)
        elif opcao == 4:
            alterar(aluno)
        elif opcao == 5:
            excluir(aluno)
        elif opcao == 6:
            cadastrarmateria(materia1)
        elif opcao == 7:
            listarmateria(materia1)
        elif opcao == 8:
            buscarmateria(materia1)
        elif opcao == 9:
            excluirmateria(materia1)
        elif opcao == 10:
            alterarmateria(materia1)
        elif opcao == 11:
            Cclasse(professor, materia1, aluno)
        elif opcao == 12:
            alterarprof(professor, materia1, aluno)
        elif opcao == 13:
            exibirSI(professor, materia1, aluno)
        elif opcao == 14:
            excluirSI(professor, materia1, aluno)
        elif opcao == 0:
            break
        else:
            print('Opção inválida')


if __name__ == '__main__':
    main()






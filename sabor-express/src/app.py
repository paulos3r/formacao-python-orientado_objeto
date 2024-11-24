import os

def display_options():
  print('1 CADASTRAR RESTAURANTE')
  print('2 LISTAR RESTAURANTE')
  print('3 SAIR \n')

def cloose_options():
  options = int( input('Escolha opção: ') )

  if options==1:
    print('Cadastrar restaurante')
  elif options==2:
    print('Listar restaurante')
  else:
    end_app()

def end_app():
  os.system('clear')
  print('Sair')

def main():
  display_options()
  cloose_options()

if __name__ == '__main__':
  main()
import os

restaurants=['pizza','suchi']

def display_options():
  print('1 CADASTRAR RESTAURANTE')
  print('2 LISTAR RESTAURANTE')
  print('3 SAIR \n')

def options_invalid():
  input('Escolha opção valida: ')
  main()

def return_main_manu():
  main()

def display_subtitle(texto):
  os.system('clear')
  print(texto)
  print()

def register_new_restaurant():
  
  display_subtitle('Cadastrar novo restorante')
  name_restaurant = input('\nDigite nome do restorante: ')
  restaurants.append(name_restaurant)
  print(f'\no restourante foi cadastrado {name_restaurant}')

  input('\ndigite uma tecla para retoranar menu principal: ')
  main()

def list_restaurant():
  display_subtitle('Lista de restaurantes')

  for restaurant in restaurants:
    print(f'\nRestaurante {restaurant}')

  input('\ndigite uma tecla para retoranar menu principal: ')
  main()



def cloose_options():
  try:
    options = int(input('Escolha opção: '))
    if options==1:
      register_new_restaurant()
    elif options==2:
      list_restaurant()
    elif options==3:
      end_app()
    else:
      options_invalid()
  except:
    print('variavem inadequada')
    options_invalid()


def end_app():
  display_subtitle('Sair')

def main():
  display_subtitle('')
  display_options()
  cloose_options()

if __name__ == '__main__':
  main()
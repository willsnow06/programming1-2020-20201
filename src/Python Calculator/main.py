print('Welcom to the calculator. Type any number for your first and second number, and then choose from +, -, /, or *.')

run = True
while run:

  num1 = int(input('type your first number here:\n'))
  op = input('type your operator here:\n')
  num2 = int(input('type your second number here:\n'))
  answer = 0
  if op == '+':
    answer = num1 + num2
    print(f'\n {answer}')
  elif op == '-':
    answer = num1 - num2
    print(f'\n {answer}')
  elif op == '*':
    answer = num1 * num2
    print(f'\n {answer}')
  elif op == '/':
    answer = num1 / num2
    print(f'\n {answer}')
  else:
    print('improper operator.\n')
  yn = input('would you like to go again? y/n\n')
  if yn == 'n':
    run = False

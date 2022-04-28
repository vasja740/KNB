import random
print('введите Ваш выбор')
user_inp = input().lower()
cmnds = ['камень', 'ножницы', 'бумага']
prog_inp = random.choice(cmnds)
print("мой выбор:", prog_inp)
if user_inp == prog_inp:
	print('хо-хо, ничья!')
elif user_inp == 'камень'and prog_inp == 'бумага':
	print('хе-хе, я выиграл!')
elif user_inp == 'ножницы'and prog_inp == 'камень':
	print('хе-хе, я выиграл!')
elif user_inp == 'бумага'and prog_inp == 'ножницы':
	print('хе-хе, я выиграл!')
else:
	print('Вы победили!')
import random

print('Lets Play Rock Paper Scissors Game!!')
player_name = input('Enter Player Name: ')

i = 0
player_count = 0
computer_count = 0
for i in range(5):
	hand = {'Rock':0, 'Paper':1, 'Scissors':2}
	comp_hand = ['Rock', 'Paper', 'Scissors']
	player_hand = input(player_name + ' select your hand (Rock, Paper or Scissors): ')
	player_num = hand[player_hand]
	computer_num = random.randint(0,2)
	computer_hand = comp_hand[computer_num]
	print('Computer selects ' + computer_hand)
	if player_hand == computer_hand:
		print('Draw')
	elif player_num == 0 and computer_num == 2:
		print('Congratulations! You Win')
		player_count = player_count + 1
	elif player_num == 1 and computer_num == 0:
		print('Congratulations! You Win')
		player_count = player_count + 1
	elif player_num == 2 and computer_num == 1:
		print('Congratulations! You Win')
		player_count = player_count + 1
	else:
		print('Hard Luck, Computer Win')
		computer_count = computer_count + 1
	i += 1
print('-----------------------------------------------------------------')
if player_count > computer_count:
	print(player_name + ' won the game!!!')
elif computer_count > player_count:
	print('Computer won the game')
else:
	print('Its a Draw')

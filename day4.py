rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
lulu=[rock,scissors,paper]
ai=random.choice(lulu)
meong=input('Pick a stance. (rock,scissors,paper)\n')
if meong=='rock':
    cc=0
elif meong=='scissors':
    cc=1
elif meong=='paper':
    cc=2

print(f'Opponent pick {ai}')
print(f'You pick {lulu[cc]}')

if ai==lulu[cc]:
    print('It\s a tie')
if ai==rock:
    if lulu[cc]==scissors:
        print('You lose')
    elif lulu[cc]==paper:
        print('You win')
if ai==scissors:
    if lulu[cc]==paper:
        print('You lose')
    elif lulu[cc]==rock:
        print('You win')
if ai==paper:
    if lulu[cc]==scissors:
        print('You win')
    elif lulu[cc]==rock:
        print('You lose')




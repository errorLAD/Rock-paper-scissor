

while True:
    p1 = input('player 1:please type of choice : rock,paper or scisscors')

    p2 = input('player 2: plz type of choicr:rock ,paper or scisscors')

    if p1 == p2:
        print('draw game' )
    elif p1 == 'rock' and p2 == 'paper':
        print('p2 2 wins')
    elif p1 == 'rock' and p2 == 'scisscors':
        print('p1 is win')
    elif p1 == 'paper' and p2  == 'rock':
        print('p1 is win')
    elif p2 == 'paper'  and p2 =='scisscors':
        print('p2 is win')
    elif p1 == 'scisscors' and p2 == 'rock':
        print('p1 win')
    elif p1 == 'scisscors' and p2 == 'paper':
        print('p2 win')
    else:
        print('wrong ans')

    ans = input('Do you want to start a new game? (Yes or No)')
    if ans == 'Yes':
        print("new games is start")
    elif ans =='No':
        stop = True
        print('Thank You,GAME over ')
    else:
        print('wrong ans,plx type yes and no in next attempt')

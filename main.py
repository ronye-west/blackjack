
# package import
# from xmlrpc.server import DocCGIXMLRPCRequestHandler
import helper as hp

# game code
print('*********************************************************')
print('starting game...')

# intitialize objects
game_deck = hp.deck()
game_dealer = hp.dealer()
game_player = hp.player()

# dealer first draw
game_dealer.turn_1(game_deck)
print('the dealer has {} and {} ({})'.format(game_dealer.current_deck[0], game_dealer.current_deck[1], game_dealer.total))

# player second draw
game_player.draw(game_deck)
game_player.draw(game_deck)
holding = False
double = False

while game_player.bust == False and game_player.blackjack == False and holding == False and double == False:
    print('you have {} and {} ({})'.format(game_player.current_deck[0], game_player.current_deck[1], game_player.total))
    action_invalid = True

    while action_invalid == True and double == False:
        if len(game_player.current_deck) == 2:
            action = str(input('please enter \'hit\' or \'hold\' or \'double\': '))
        else:
            action = str(input('please enter \'hit\' or \'hold\': '))
        if type(action) == str:
            if action.lower() in ['hit', 'hold']:
                action_invalid = False
            elif action.lower() == 'double' and len(game_player.current_deck) == 2:
                game_player.draw(game_deck)
                double = True
            else:
                print('invalid input')
        else:
            print('invalid input')
    if action == 'hit':
        game_player.draw(game_deck)
    elif action == 'hold':
        holding = True

if game_player.bust == True:
    print('you lose...your total exceeded 21 ({})'.format(game_player.total))
else:
    # dealer third draw
    game_dealer.turn_2(game_deck)
    if game_dealer.bust == False:
        if game_dealer.total > game_player.total:
            print('the dealer wins...the dealer had a higher total ({}) than you ({})'.format(game_dealer.total, game_player.total))
        elif game_dealer.total < game_player.total:
            print('you win! you had a higher total ({}) than the dealer ({})'.format(game_player.total, game_dealer.total))
        else:
            print('tie! you and the dealer both had a total of {}'.format(game_dealer.total))
    else:
        print('you win! the dealers total exceeded 21 ({})'.format(game_dealer.total))

print('your final deck: {} ({})'.format(game_player.current_deck, game_player.total))
print('the dealers final deck {} ({})'.format(game_dealer.current_deck, game_dealer.total))
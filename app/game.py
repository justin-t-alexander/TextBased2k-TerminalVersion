class Player:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating


        
player1 = Player("Player 1", 80)
player2 = Player("Player 2", 85)
player3 = Player("Player 3", 75)

# List of players
players = [player1, player2, player3]


def select_players(players):
    print("Select two players to play:")
    for i, player in enumerate(players):
        print(f"{i+1}. {player.name} (Rating: {player.rating})")
    
    # Get user input
    while True:
        try:
            index1 = int(input("Enter number of Player 1: ")) - 1
            index2 = int(input("Enter number of Player 2: ")) - 1
            
            # Check if indices are valid
            if 0 <= index1 < len(players) and 0 <= index2 < len(players) and index1 != index2:
                return players[index1], players[index2]
            else:
                print("Invalid input. Please enter valid indices.")
        except ValueError:
            print("Invalid input. Please enter integers.")
        
def simulate_game(player1, player2):
            if player1.rating > player2.rating:
                return player1
            elif player2.rating > player1.rating:
                return player2
            else:
                return None  # It's a tie


if __name__ == "__main__":
    # Create players
    player1 = Player("Player 1", 80)
    player2 = Player("Player 2", 85)
    player3 = Player("Player 3", 75)
    
    players = [player1, player2, player3]
    
    # Select players
    selected_player1, selected_player2 = select_players(players)
    
    # Simulate game
    winner = simulate_game(selected_player1, selected_player2)
    
    # Display winner
    if winner:
        print(f"{winner.name} wins!")
    else:
        print("It's a tie!")



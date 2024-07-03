document.addEventListener("DOMContentLoaded", function() {
    const player1Select = document.getElementById('player1');
    const player2Select = document.getElementById('player2');
    const simulateButton = document.getElementById('simulate-button');
    const resetButton = document.getElementById('reset-button');

    player1Select.addEventListener('change', function() {
        displaySelectedPlayer(player1Select, 'Player 1');
    });

    player2Select.addEventListener('change', function() {
        displaySelectedPlayer(player2Select, 'Player 2');
    });

    simulateButton.addEventListener('click', function() {
        const winner = simulateGame(player1Select.value, player2Select.value);
        if (winner) {
            console.log(`${winner} wins!`);
            document.getElementById('winner-message').textContent = `${winner} wins!`;
        } else {
            console.log("It's a tie!");
            document.getElementById('winner-message').textContent = "It's a tie!";
        }
    });

    resetButton.addEventListener('click', function() {
        player1Select.selectedIndex = 0;
        player2Select.selectedIndex = 0;
        document.getElementById('winner-message').textContent = '';
    });

    function displaySelectedPlayer(selectElement, playerLabel) {
        const selectedPlayer = selectElement.options[selectElement.selectedIndex].text;
        const playerRating = selectElement.value; // Assuming value contains player rating
        console.log(`${playerLabel} selected: ${selectedPlayer} (Rating: ${playerRating})`);
        document.getElementById(`${playerLabel.toLowerCase()}-rating`).textContent = `Rating: ${playerRating}`;
    }

    function simulateGame(player1Name, player2Name) {
        const player1Rating = parseInt(player1Select.value); // Assuming value is the rating
        const player2Rating = parseInt(player2Select.value); // Assuming value is the rating

        if (player1Rating > player2Rating) {
            return player1Name;
        } else if (player2Rating > player1Rating) {
            return player2Name;
        } else {
            return null; // It's a tie
        }
    }
});

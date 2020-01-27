var nextPlayer = 'O';
// Restart Game Button
var btn = document.querySelector('#restart');
// Grabs all the squares
var boxes = document.querySelectorAll("td");
// Clear all the squares
function restart(){
    for (box of boxes){
        box.textContent = '';
        nextPlayer = 'O';
    }
}

btn.addEventListener("click", restart)

// Check the square marker

function tictac(){
    if (this.textContent === ''){
        this.textContent = nextPlayer;
        if (nextPlayer === 'O'){
            nextPlayer = 'X';
        } else {
            nextPlayer = 'O';
        }
    }
}
// For loop to add enevt listeners to all the squares

for (box of boxes){
    box.addEventListener("click", tictac);
}





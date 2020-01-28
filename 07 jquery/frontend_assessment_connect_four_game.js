var playerOne = prompt("Player One: Enter your name, you will be Blue.");
var playerTwo = prompt("Player Two: Enter your name, you will be Red.");
playerOne = {name: playerOne, color: 'blue'};
playerTwo = {name: playerTwo, color: 'red'};
var currentPlayer = null;
nextPlayer();
gameOn = true;


var isFilledArr = [];
for(var i=0; i<6; i++){
    isFilledArr.push([0, 0, 0, 0, 0, 0, 0]);
}

function nextPlayer(){
    if(currentPlayer === playerOne){
        currentPlayer = playerTwo;
    }else {
        currentPlayer = playerOne;
    }
    $('#illustrate').text(currentPlayer.name + ": it is your turn, please pick a column to drop your " + 
                        currentPlayer.color + " chip");
}

function checkWin(row, col){
    count = 0;
    isWin = false;
    for (var i=0; i<isFilledArr.length; i++) {
        if (isFilledArr[i][col] === isFilledArr[row][col]){
            count ++;
            if (count === 4){
                isWin = true;
            }
        } else {
            count = 0;
        }
    }

    count = 0;
    for (var i=0; i<isFilledArr[0].length; i++) {
        if (isFilledArr[row][i] === isFilledArr[row][col]){
            count ++;
            if (count === 4){
                isWin = true;
            }
        } else {
            count = 0;
        }
    }

    count = 0;
    for (var i=0; i<4; i++){
        if (row+i < isFilledArr.length && col-i >=0){
            if (isFilledArr[row+i][col-i] === isFilledArr[row][col]){
                count ++;
                if (count === 4){
                    isWin = true;
                }
            } else {
                count = 0;
            }
        }
    }

    count = 0;
    for (var i=0; i<4; i++){
        if (row+i < isFilledArr.length && col+i < isFilledArr[0].length){
            if (isFilledArr[row+i][col+i] === isFilledArr[row][col]){
                count ++;
                if (count === 4){
                    isWin = true;
                }
            } else {
                count = 0;
            }
        }
    }
    

    if (isWin){
        gameOn = false;
        $('#illustrate').text("Congratulations!!! " + currentPlayer.name + " you won!");
    } else{
        nextPlayer();
    }
    
}

function fillColor(){
    if(!gameOn){return;}

    var col = $(this).index();
    for(var i=5; i>=0; i--){
        if(!isFilledArr[i][col]){
            $('td').eq(i*7 + col).toggleClass(currentPlayer.color);
            isFilledArr[i][col] = currentPlayer.color;
            checkWin(i, col);
            break;
        }
    }
}

$('td').on('click', fillColor)

const boardElement = document.getElementById("board");

// Initialize board
let board = [["","","",],["","",""],["", "", ""]]
let player = "X";
let opponent = "Person";
let difficulty = "Easy";
function renderBoard() {
    boardElement.innerHTML = "";
    board.forEach((row, rowIndex) => {
        row.forEach((cell, colIndex) => {
            const cellElement = document.createElement("div");
            cellElement.textContent = cell;
            cellElement.className = "cell"
            if(cell === "X"){
                cellElement.style.color = "red";
            }else if(cell === "O"){
                cellElement.style.color = "blue";
            }
            cellElement.addEventListener("click", () => makeMove(rowIndex, colIndex))
            boardElement.appendChild(cellElement);
        });
    });
}
function renderStats(wins, ties, losses){
    const statsDisplay = document.getElementById("stats");
    if(opponent === "Person")
        statsDisplay.innerText= "Player(X): "+wins+"\t"+ "Ties: " + ties +"\t" + "Player(O): " + losses;
    if(opponent === "Robot")
        statsDisplay.innerText= "Player(X): "+wins+"\t"+ "Ties: " + ties +"\t" + "Bot: " + losses;
}

async function makeMove(row, col) {
    const response = await fetch("/move", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ row, col, player}),
    });
    const data = await response.json();
    if (data.status === "success"){
        board = data.board;
        renderBoard();
        if(opponent === "Person"){
            if(player === "X")
                player ="O";
            else
                player = "X";
        }   
        else{
            player = "X"
            botMove();
        }
    } else if (data.status === "winner"){
        board = data.board;
        renderBoard();
        renderStats(data.stats.wins, data.stats.ties, data.stats.losses);
        resetBoard(1000);
    } else {
        alert(data.message);
    }
}
// Function to make a bot move

async function botMove() {
    const response = await fetch("/botMove", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(difficulty),
    });
    const data = await response.json();
    if (data.status === "success") {
        board = data.board;
        renderBoard();
    }
    else if (data.status === "winner") {
        board = data.board;
        renderBoard();
        renderStats(data.stats.wins, data.stats.ties, data.stats.losses);
        resetBoard(1500);
    }else if (data.status === "tie") {
        board = data.board;
        renderBoard();
        renderStats(data.stats.wins, data.stats.ties, data.stats.losses);
        resetBoard(1500);
    }else {
        alert(data.message);
    }
}

reset.addEventListener("click", async () => {
    resetBoard(0);
});

function resetBoard(timeout){
    player = "X"
    setTimeout(async () => {
        const response = await fetch("/reset", {
            method: "POST",
        });
        const data = await response.json();
        if (data.status === "success") {
            board = data.board;
            renderBoard();
        } else {
            alert("Failed to reset the game.");
        }
    }, timeout);
}

async function resetStats(){
    const response = await fetch("/resetStats", {
        method: "POST",
    });
    const data = await response.json();
    if (data.status === "success") {
        renderStats(data.stats.wins, data.stats.ties, data.stats.losses);
    } else {
        alert("Failed to reset the stats.");
    }
}

const opponentSelector = document.getElementById("opponentSelector");
opponentSelector.addEventListener("click", async () => {
    opponent = opponent === "Robot" ? "Person" : "Robot";
    resetBoard(0);
    resetStats();
    // Update the button text to match the variable
    opponentSelector.innerText = "Opponent: " + opponent;
});

const difficultySelector =document.getElementById("difficulty")
difficultySelector.addEventListener("click", async () =>{
    resetBoard(0);
    resetStats();
    if(difficulty === "Easy"){
        difficulty = "Medium";
    }else if(difficulty === "Medium"){
        difficulty = "Hard";
    }else
        difficulty = "Easy"
    difficultySelector.innerText = "Difficulty: " + difficulty;
});

renderBoard();

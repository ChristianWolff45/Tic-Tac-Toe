from flask import Flask, render_template, request, jsonify
from botMoves import easy_bot_moves, hard_bot_moves, medium_bot_moves
import copy
app = Flask(__name__)
board = [["", "", ""], ["", "", ""], ["", "", ""]]
stats = {"wins": 0, "ties": 0, "losses": 0}

@app.route("/", methods=["GET"])
def home():
    """Render the game board."""
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    print("move")
    data = request.get_json()
    row, col, player = data["row"], data["col"], data["player"]

    # Check if the move is valid
    if board[row][col] != "":
        return jsonify({"status": "error", "message": "Cell already occupied"}), 400

    # Update the board
    board[row][col] = player


    if winner(player) != None:
        if player == "O":
            stats["losses"] = stats["losses"] +1
        if player == "X":
            stats["wins"] = stats["wins"] +1
        return jsonify({"status": "winner", "stats" : stats, "board": board})

    return jsonify({"status": "success", "board": board})

def winner(player):
    if(board[1][1]==player):
        if(board[0][0]==player and board[2][2]==player):
            return True
        if(board[0][1]==player and board[2][1]==player):
            return True
        if(board[0][2]==player and board[2][0]==player):
            return True
        if(board[1][0]==player and board[1][2]==player):
            return True
    if(board[0][0]==player):
        if(board[0][1]==player and board[0][2]==player):
            return True
        if(board[1][0]==player and board[2][0]==player):
            return True
    if(board[2][2]==player):
        if(board[1][2]==player and board[0][2]==player):
            return True
        if(board[2][1]==player and board[2][0]==player):
            return True
        
@app.route("/botMove", methods=["POST"])
def botmove():
    """Handle the bot's move."""
    global board
    if all(cell != "" for row in board for cell in row):
        stats["ties"] = stats["ties"] +1
        return jsonify({"status": "tie", "stats" : stats, "board": board})
    # Find all empty cells
    tempBoard = copy.deepcopy(board)

    difficulty = request.get_json()

    if difficulty == "Easy":
        row, col = easy_bot_moves(tempBoard)
    if difficulty == "Medium":
        row, col = medium_bot_moves(tempBoard)
    if difficulty == "Hard":
        row, col = hard_bot_moves(tempBoard)

    print(difficulty)

    board[row][col] = "O"
    # Check if bot wins
    if winner("O"):
        stats["losses"] = stats["losses"] +1
        return jsonify({"status": "winner", "stats" : stats, "board": board})

    # Check for a tie
    

    return jsonify({"status": "success", "board": board})


@app.route("/reset", methods =["POST"])
def reset():
    global board
    board = [["","","",],["","",""],["", "", ""]]
    return jsonify({"status": "success", "board": board})

@app.route("/resetStats", methods =["POST"])
def resetStats():
    stats["wins"] = 0
    stats["losses"] = 0
    stats["ties"] = 0

    return jsonify({"status": "success", "stats": stats})

if __name__ == "__main__":
    app.run(debug=True)

# Tic-Tac-Toe Web App

A simple Tic-Tac-Toe game built with Python (Flask), HTML and Javascript. The game contains uses a minimax algorithm for an unbeatable hard bot option.

## Features
- Classic 3x3 Tic-Tac-Toe grid
- Player vs Player mode
- Player vs three levels of bots

## Getting Started

### Prerequisites
Make sure you have the following installed:
- **Python 3.x**
- **pip** (Python package installer)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the App
1. **Start the Flask server:**
   ```bash
   flask run
   ```
   By default, the app will be accessible at `http://127.0.0.1:5000/`.

2. **Play the game:**
   Open the URL in your web browser and enjoy playing Tic-Tac-Toe!

## Project Structure
```
├── static/
│   └── js/
│       └── game.js
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
```

- **`app.py`**: Main Flask application.
- **`templates/index.html`**: HTML structure of the game.
- **`static/js/game.js`**: JavaScript for game logic and interactivity.
- **`requirements.txt`**: Lists Python dependencies.

## Dependencies
- Flask

## License
This project is open-source and free to use under the MIT License.

## Acknowledgments
Special thanks to everyone who supported the development of this project!



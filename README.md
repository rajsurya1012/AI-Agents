# AI Game Agents Repository

Welcome to my AI Game Agents repository! This is a collection of AI agents I've developed to play various games, each showcasing different AI techniques and strategies. Below is a guide to the repository's structure, the games included, and instructions on running the AI agents.

## Repository Structure

- **`randothello.py`**: Implements the RandOthello game with AI players such as RandomPlayer, MinimaxPlayer, and AlphaBetaPlayer.
- **`eight_puzzle.py`**: Contains the Eight Puzzle game, featuring search algorithms like Breadth-First Search, Iterative Deepening, and A* Search[1].
- **`game_schedule.py`**: Includes a scheduling problem tackled with optimization techniques like Hill Climbing and Simulated Annealing[2].
- **`clue_game_reasoner.py`**: Implements a propositional reasoner for the game of Clue, focusing on logical deduction to solve the mystery[3].

## Games Included

1. **RandOthello**
   - A variant of the classic Othello game with random blocked positions.
   - **AI Players**:
     - **RandomPlayer**: Chooses moves randomly.
     - **MinimaxPlayer**: Utilizes the Minimax algorithm for strategic decision-making.
     - **AlphaBetaPlayer**: Optimizes the Minimax algorithm using Alpha-Beta Pruning.

2. **Eight Puzzle**
   - A sliding puzzle consisting of a 3x3 grid with tiles numbered 1 to 8 and one empty space.
   - **Search Algorithms**:
     - **Breadth-First Search**: Explores all nodes at the present depth before moving on to nodes at the next depth level.
     - **Iterative Deepening**: Combines the space efficiency of Depth-First Search with the optimality of Breadth-First Search.
     - **A* Search**: Uses heuristics to efficiently find the shortest path to the goal state.

3. **Game Scheduling Problem**
   - A problem involving scheduling games between players to optimize certain criteria.
   - **Optimization Techniques**:
     - **Hill Climbing**: Iteratively improves the solution by making local changes.
     - **Simulated Annealing**: Probabilistically accepts worse solutions to escape local optima and find a global optimum.

4. **Clue**
   - A classic deduction game where players aim to solve a murder mystery by determining the suspect, weapon, and location.
   - **AI Reasoner**: Uses propositional logic to track game information and deduce the solution.

## Getting Started

### Prerequisites

- Python 3.x
- Additional libraries may be required for specific games; these will be listed in the respective game files.

### Running the Games

1. **RandOthello**
   - To play RandOthello between two AI agents, execute:
     ```bash
     python randothello.py
     ```
   - The `main()` function sets up games with different AI player configurations.

2. **Eight Puzzle**
   - To solve the Eight Puzzle using different search algorithms, run:
     ```bash
     python eight_puzzle.py <initial_state>
     ```
   - Replace `<initial_state>` with the starting configuration of the puzzle.

3. **Game Scheduling Problem**
   - To execute the scheduling optimization, run:
     ```bash
     python game_schedule.py
     ```
   - This will apply optimization techniques to generate a game schedule.

4. **Clue**
   - To run the Clue game reasoner, execute:
     ```bash
     python clue_game_reasoner.py
     ```
   - This will simulate a game of Clue using logical deductions to solve the mystery.

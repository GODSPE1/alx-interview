# ALX Interview Preparation

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow.svg)
![ALX](https://img.shields.io/badge/ALX-Interview_Prep-orange.svg)

This repository contains a collection of algorithm and data structure challenges designed for technical interview preparation. Each project focuses on specific computer science concepts and problem-solving techniques commonly encountered in technical interviews.

## 📋 Table of Contents

- [About](#about)
- [Projects](#projects)
- [Technologies](#technologies)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Author](#author)

## 🎯 About

This repository is part of the ALX Software Engineering program's interview preparation curriculum. It covers fundamental to advanced algorithmic problems, focusing on:

- **Algorithm Design**: Greedy algorithms, dynamic programming, backtracking
- **Data Structures**: Arrays, matrices, lists, and their manipulations
- **Problem-Solving**: Mathematical problems, optimization, pattern recognition
- **Coding Skills**: Clean code, efficient solutions, edge case handling

## 📚 Projects

### [0x00. Pascal's Triangle](./0x00-pascal_triangle)
Generate Pascal's triangle using Python lists and list comprehensions.

**Concepts**: Lists, algorithms, mathematical patterns

### [0x03. Log Parsing](./0x03-log_parsing)
Parse and process log data in real-time from standard input.

**Concepts**: File I/O, data parsing, regular expressions, signal handling

### [0x04. UTF-8 Validation](./0x04-utf8_validation)
Validate whether a given dataset represents valid UTF-8 encoding.

**Concepts**: Bitwise operations, encoding schemes, data representation

### [0x05. N Queens](./0x05-nqueens)
Solve the classic N Queens puzzle using backtracking algorithm.

**Concepts**: Backtracking, recursion, constraint satisfaction problems

### [0x06. Star Wars API](./0x06-starwars_api)
Fetch and display Star Wars character information using an external API.

**Concepts**: API interaction, asynchronous programming, HTTP requests (JavaScript/Node.js)

### [0x07. Rotate 2D Matrix](./0x07-rotate_2d_matrix)
Rotate an n×n 2D matrix by 90 degrees clockwise in-place.

**Concepts**: Matrix manipulation, in-place operations, space optimization

### [0x08. Making Change](./0x08-making_change)
Determine the minimum number of coins needed to make a given amount.

**Concepts**: Dynamic programming, greedy algorithms, optimization

### [0x09. Island Perimeter](./0x09-island_perimeter)
Calculate the perimeter of an island in a grid.

**Concepts**: 2D arrays, conditional logic, grid traversal

### [0x0A. Prime Game](./0x0A-primegame)
Determine the winner of a game involving prime numbers using game theory.

**Concepts**: Prime numbers, game theory, optimal play, Sieve of Eratosthenes

## 🛠 Technologies

- **Python 3.x**: Primary language for most challenges
- **JavaScript (Node.js)**: Used for API interaction challenges
- **Git**: Version control

## 📋 Requirements

### Python Projects
- Ubuntu 20.04 LTS or later
- Python 3.4.3 or later
- PEP 8 style (version 1.7.x)

### JavaScript Projects
- Ubuntu 20.04 LTS
- Node.js 10.14.x or later
- Semi-standard code style

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/GODSPE1/alx-interview.git
cd alx-interview
```

2. For Python projects:
```bash
# Python is typically pre-installed on Ubuntu
python3 --version
```

3. For JavaScript projects:
```bash
# Install Node.js if needed
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## 💻 Usage

Each project directory contains its own README with specific instructions. Generally:

### Python Projects
```bash
cd 0x00-pascal_triangle
chmod +x 0-pascal_triangle.py
./0-main.py  # If main file exists
```

### JavaScript Projects
```bash
cd 0x06-starwars_api
chmod +x 0-starwars_characters.js
./0-starwars_characters.js [movie_id]
```

## 📁 Project Structure

```
alx-interview/
├── 0x00-pascal_triangle/       # Pascal's Triangle generation
├── 0x03-log_parsing/            # Log parsing and statistics
├── 0x04-utf8_validation/        # UTF-8 encoding validation
├── 0x05-nqueens/                # N Queens problem solver
├── 0x06-starwars_api/           # Star Wars API character fetcher
├── 0x07-rotate_2d_matrix/       # 2D matrix rotation
├── 0x08-making_change/          # Coin change problem (DP/Greedy)
├── 0x09-island_perimeter/       # Island perimeter calculation
├── 0x0A-primegame/              # Prime number game theory
└── README.md                    # This file
```

Each subdirectory contains:
- Solution file(s) (`.py` or `.js`)
- `README.md` with problem description and concepts
- Test files (where applicable)

## 🎓 Learning Objectives

Through these projects, you will learn to:

- Apply various algorithm design techniques
- Work with different data structures efficiently
- Handle edge cases and optimize solutions
- Write clean, readable, and maintainable code
- Solve problems within time and space complexity constraints
- Debug and test algorithmic solutions

## 🤝 Contributing

This is an educational repository. While it's primarily for personal learning:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## ✍️ Author

**GODSPE1**
- GitHub: [@GODSPE1](https://github.com/GODSPE1)

## 📝 License

This project is part of the ALX Software Engineering program curriculum.

## 🙏 Acknowledgments

- ALX Africa for the curriculum and project requirements
- The broader software engineering community for algorithmic knowledge sharing

---

*This repository is maintained as part of the ALX Software Engineering program interview preparation track.*

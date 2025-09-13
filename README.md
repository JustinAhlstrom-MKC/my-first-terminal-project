# My First Terminal Project

A beginner-friendly Python project featuring two simple terminal-based applications for learning Python development fundamentals.

## Project Overview

This project contains two Python scripts that demonstrate basic terminal programming concepts:

1. **Hello Terminal** - An interactive greeting application
2. **GitHub User Info Fetcher** - A tool to retrieve and display GitHub user information

## Scripts

### hello_terminal.py
A simple interactive script that:
- Displays a welcome message
- Shows the script's file path
- Prompts for user input
- Provides a personalized greeting

```bash
python hello_terminal.py
```

### fetch_data.py
A GitHub API client that:
- Prompts for a GitHub username
- Fetches user data from the GitHub API
- Displays user information including name, bio, public repos, and followers
- Handles errors for non-existent users

```bash
python fetch_data.py
```

## Requirements

- Python 3.6+
- requests library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/JustinAhlstrom-MKC/my-first-terminal-project.git
cd my-first-terminal-project
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run either script directly:

```bash
# Interactive greeting
python hello_terminal.py

# GitHub user lookup
python fetch_data.py
```

## Learning Objectives

This project demonstrates:
- Basic Python syntax and structure
- User input handling
- HTTP API requests using the `requests` library
- Error handling and validation
- Terminal-based user interfaces
- Virtual environment usage
- Git version control

## Dependencies

- `requests==2.32.5` - For making HTTP requests to the GitHub API
- `certifi==2025.8.3` - SSL certificate verification
- `charset-normalizer==3.4.3` - Character encoding detection
- `idna==3.10` - Internationalized domain names
- `urllib3==2.5.0` - HTTP client library

## Contributing

This is a learning project, but suggestions and improvements are welcome!

## License

This project is open source and available under the MIT License.
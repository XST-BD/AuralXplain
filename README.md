<h1 align="center">AuralXplain</h1>

<p align="center">AI-powered audio summarizer</p>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/XST-BD/AuralXplain.svg)](https://github.com/XST-BD/AuralXplain/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/XST-BD/AuralXplain.svg)](https://github.com/XST-BD/AuralXplain/pulls)

</div>

---

## Table of Contents

- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Setup before 1st Run](#setup-before-1st-run)
    - [Setup before Every Run](#setup-before-every-run)
    - [Run the Application](#run-the-application)
- [Usage](#usage)
- [Built With](#built-with)
- [Authors](#authors)

## Getting Started

Follow these instructions to set up and run the application on your local machine.

### Prerequisites

- Python
- pip (Python package installer)

### Setup before 1st Run

1. Clone the repository
    ```bash
    git clone https://github.com/XST-BD/AuralXplain.git
    ````
2. Navigate to the project directory
    ```bash
    cd path/to/folder/AuralXplain
    ```
3. Set up a virtual environment (optional but recommended)
    ```bash
    python -m venv .venv
    ```
4. Activate the virtual environment
   - On Windows
       ```bash
       venv\Scripts\activate
       ```
   - On macOS / Linux
       ```bash
       source venv/bin/activate
       ```
5. Install the required dependencies
    ```bash
    pip install textual
    ```

### Setup before Every Run
1. Navigate to the project directory
    ```bash
    cd path/to/folder/AuralXplain
    ```
2. Activate the virtual environment
   - On Windows
       ```bash
       venv\Scripts\activate
       ```
   - On macOS / Linux
       ```bash
       source venv/bin/activate
       ```

### Run the Application

#### Windows
```bash
python main.py
```

#### macOS / Linux
```bash
python3 main.py
```

## Usage

- Enter the absolute path of the audio file you want to summarize.
- Press the "Generate" button to generate the summary.
- View the generated summary in the designated area.

## Built With

- **Python** - Core Language
- **Textual** - TUI Framework

## Authors

- [**Atia Farha**](https://github.com/Atia-Farha) - Frontend Developer
- [**S.M Nazmus Sadat**](https://github.com/smsadat-dev) - Backend Developer
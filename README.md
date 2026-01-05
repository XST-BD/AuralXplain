<h1 align="center">MediaXplain</h1>

<p align="center">AI-powered Audio & Video Summarizer</p>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/XST-BD/MediaXplain.svg)](https://github.com/XST-BD/MediaXplain/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/XST-BD/MediaXplain.svg)](https://github.com/XST-BD/MediaXplain/pulls)

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

- Python -> [Installation Guide](/docs/PYTHON-INSTALLATION.md)
- FFmpeg -> [Installation Guide](/docs/FFMPEG-INSTALLATION.md)
- Git (for cloning the repository)

### Setup before 1st Run

1. Clone the repository
    ```bash
    git clone https://github.com/XST-BD/MediaXplain.git
    ````
2. Navigate to the project directory
    ```bash
    cd path/to/folder/MediaXplain
    ```
3. Set up a virtual environment (optional but recommended)
    ```bash
    python -m venv .venv
    ```
4. Activate the virtual environment
    - On Windows
        ```bash
        .venv\Scripts\activate
        ```
    - On macOS / Linux
        ```bash
        source .venv/bin/activate
        ```
5. Install the required dependencies
    ```bash
    pip install transformers torch textual faster-whisper
    ```

### Setup before Every Run

1. Navigate to the project directory
    ```bash
    cd path/to/folder/MediaXplain
    ```
2. Activate the virtual environment
    - On Windows
        ```bash
        .venv\Scripts\activate
        ```
    - On macOS / Linux
        ```bash
        source .venv/bin/activate
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

- Enter the absolute path of a audio or a video file you want to summarize.
- Press the "Generate" button to generate the summary.
- View the generated summary in the designated area.

> Currently only **English** audio and video files are supported with accuracy.

## Built With

- **Python** - Core Language
- **Textual** - TUI Framework
- **Transformers** - NLP Library
- **Torch** - Deep Learning Framework
- **Faster Whisper** - Speech-to-Text Model
- **FFmpeg** - Media Processing

## Authors

- [**Atia Farha**](https://github.com/Atia-Farha) - Frontend Developer
- [**S.M Nazmus Sadat**](https://github.com/smsadat-dev) - Backend Developer

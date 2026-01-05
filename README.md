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

### Setup before 1st Run

1. Download the preferred version (latest is recommended) of compressed source folder (`zip` or `tar.gz`) from [the repository releases](https://github.com/XST-BD/MediaXplain/releases).
2. Extract the downloaded folder.
3. Open a terminal and navigate to the project directory
    ```bash
    cd path/to/folder/MediaXplain-x.x.x
    ```
4. Set up a virtual environment (optional but recommended)
    ```bash
    python -m venv .venv
    ```
5. Activate the virtual environment
    - On Windows
        ```bash
        .venv\Scripts\activate
        ```
    - On macOS / Linux
        ```bash
        source .venv/bin/activate
        ```
6. Install the required dependencies
    ```bash
    pip install transformers torch textual faster-whisper
    ```

### Setup before Every Run

1. Navigate to the project directory
    ```bash
    cd path/to/folder/MediaXplain-x.x.x
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

- Enter the absolute path of an audio or a video file you want to summarize.
- Press the "Generate" button to generate the summary.
- View the generated summary in the designated area.
- Copy the summary to clipboard by pressing the "Copy to Clipboard" button.
- Save the summary to a `.txt` file by pressing the "Save to File" button.

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

# 🔇 Audio Remover

A simple Python utility that removes audio from video files and saves a separate muted copy, without modifying the original video.

Part of the [Tools](../README.md) repository — a collection of small, practical tools built one day at a time.

## ✨ Features

- Remove audio from video files.
- Preserve the original video file.
- Automatically save the muted video in the same directory.
- Generate an output filename with `_muted` appended.
- Simple Python script with minimal setup.

## 🛠️ Tech Stack

- **Language:** Python
- **Library:** [MoviePy](https://pypi.org/project/moviepy/)

## 📋 Prerequisites

- Python 3.9 or later, compatible with your installed MoviePy version.
- `pip` installed and available in your terminal.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Kumayl-Lokhandwala/Tools.git
cd Tools/audio-remover
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Usage

### 1. Configure the input video

Open `audio_remover.py` and update the input file path:

```python
from pathlib import Path

input_file = Path(r"C:\Users\YourName\Videos\input.mp4")
```

Replace the example path with the location of your video file.

### 2. Run the script

```bash
python audio_remover.py
```

### 3. Find the output

If your original video is named `input.mp4`, the script creates:

```text
input_muted.mp4
```

The output is saved in the same directory as the input video.

## 📁 Project Structure

```text
audio-remover/
├── README.md
├── audio_remover.py
└── requirements.txt
```

The virtual environment is created locally and is not included in the repository.

## ⚠️ Notes

- The original video remains unchanged.
- Video processing time depends on the file size, duration, and system performance.
- The output may be re-encoded, which can affect file size and video quality slightly.
- Use a valid path to a video file supported by MoviePy.

## 🤝 Contributing

Found a bug or have an idea for improvement? Feel free to open an issue or submit a pull request.

## 📜 License

Refer to the license in the root of the repository.

---

**Built to keep things simple.** 🛠️

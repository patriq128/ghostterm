# ghostterm

A lightweight, always-on-top AI terminal assistant powered by [tgpt](https://github.com/aandrew-me/tgpt) with optional text-to-speech output.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Linux-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## What it does

`ghostterm` sits quietly in the corner of your screen — a small black terminal window that stays on top of everything. Type a question, get an AI answer. It can even read the response aloud.

![screenshot placeholder](screenshot.png)

---

## Features

- 🖥️ Minimal always-on-top floating window
- 🤖 Powered by `tgpt` (no API key needed by default)
- 🔊 Optional `espeak` text-to-speech for every response
- 🌀 Spinner/noise characters filtered from output
- 🎨 Dark terminal aesthetic with color-coded input/output
- `-s` flag support for shell command generation mode

---

## Requirements

- Python 3.7+
- [`tgpt`](https://github.com/aandrew-me/tgpt) installed and available in `$PATH`
- `espeak` (optional, for text-to-speech)
- `tkinter` (usually bundled with Python)

### Install dependencies

```bash
# tgpt (Linux)
curl -sSL https://raw.githubusercontent.com/aandrew-me/tgpt/main/install | bash

# espeak (optional)
sudo apt install espeak      # Debian/Ubuntu
sudo pacman -S espeak        # Arch
```

---

## Usage

```bash
python3 ghostterm.py
```

The window appears in the top-right corner of your screen. Type your prompt and press **Enter**.

### Special syntax

| Input | Behavior |
|-------|----------|
| `your question` | Ask tgpt anything |
| `-s your task` | Shell mode — generates a shell command |
| `exit` / `quit` | Close the app |

---

## Configuration

At the top of `ghostterm.py` you can tweak:

```python
speach = True   # Set to False to disable text-to-speech
```

Window size and position:
```python
root.geometry("400x200+500+0")  # widthxheight+x+y
```

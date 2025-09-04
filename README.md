# 🎙️ AI Audio Interview Coach (Web)

An end-to-end **audio interview training** app with a **Flask web UI** that:
- Generates **context-aware questions** (uses your **Job Title**, **Job Description**, **Résumé**, **Experience Level**).
- Lets you **answer by voice** (**Malayalam / English / Kannada**).
- **Cleans & enhances audio** (noise reduction → **WPE** dereverb → band‑pass → **LUFS** normalization → *(optional)* deep speech enhancement).
- **Detects language** (Whisper) and **transcribes** with OpenAI (preserves **filler words**, hesitations, `...` pauses).
- **Translates** non-English answers to English for comparable feedback.
- **Analyzes delivery** (**WPM**, **filler ratio**, long pauses via **MFA** alignment) and provides **AI feedback** vs a model answer.
- Supports **Live mode** (continuous Q&A) and **Recorded mode** (retry takes and keep the best).

> The web UI **wraps the original single-notebook pipeline**. The legacy notebook flow remains available (see **Legacy (Optional)** below).

---

## 📚 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Quick Start (Web UI)](#-quick-start-web-ui)
- [Repository Structure](#-repository-structure)
- [Requirements](#-requirements)
  - [1) Python & OS](#1-python--os)
  - [2) Python Packages](#2-python-packages)
  - [Notes](#notes)
  - [3) External Tools](#3-external-tools)
  - [4) Environment Variables / PATH](#4-environment-variables--path)
  - [5) API Keys](#5-api-keys)
- [Download the Code](#-download-the-code)
- [Run (Web UI)](#-run-web-ui)
- [Legacy (Optional): Notebook Flow](#-legacy-optional-notebook-flow)
- [Config You May Need to Edit](#-config-you-may-need-to-edit)
- [Outputs](#-outputs)
- [Optional: MFA Alignment](#-optional-mfa-alignment)
- [Troubleshooting](#-troubleshooting)
- [Security Note](#-security-note)
- [Sample requirements.txt](#-sample-requirementstxt)

---

## 🔎 Overview
This repository provides a **Flask web application** for realistic, **voice-based interview practice**. The browser UI collects inputs (Job Title, JD, résumé, language, mode), captures/receives audio, and the server runs the **same robust audio + LLM pipeline** used in the notebook version (cleaning → transcription → optional translation → analytics → AI feedback).

---

## ✨ Features
- **Languages:** `en`, `ml`, `kn` (Whisper LID + GPT verification fallback)  
- **Audio pipeline:** `noisereduce` → **WPE** (`nara_wpe`) → **band‑pass** (≈300–3400 Hz) → **−23 LUFS** → *(optional)* DL enhancement (`hyperpyyaml`)  
- **Transcription:** OpenAI (preserves fillers & pauses)  
- **Translation:** `deep-translator` (Malayalam/Kannada → English)  
- **TTS (optional):** `pyttsx3` can read questions/model answers aloud  
- **Résumé parsing:** `PyMuPDF (fitz)`  
- **Analytics:** WPM, filler ratio/count, pause counts/durations (**MFA JSON**)  
- **Modes:** **Live** and **Recorded**  
- **Persistence:** `history.json`

---

## ▶️ Quick Start (Web UI)

1. **Clone**
    ```
    git clone https://github.com/<your-account>/<your-repo>.git
    cd <your-repo>
    ```

2. **Create & activate a virtualenv**, then **install deps** (see **Requirements** below).

3. **Set environment variables**
   - `OPENAI_API_KEY`  
   - Ensure **FFmpeg** on `PATH`  
   - *(Optional)* **MFA** on `PATH` for pause/phone analytics  

4. **Run the server**
    ```
    python app.py
    ```

5. **Open** `http://127.0.0.1:5000/` and start your session.

---

## 📁 Repository Structure

```
<repo>/
├─ app.py # Flask routes / API endpoints
├─ pipeline.py # Core audio+LLM pipeline (used by web & legacy)
├─ templates/
│ └─ index.html # Web UI
├─ static/ # (optional) CSS/JS/assets
├─ requirements.txt # (optional) mirrors your install list
└─ README.md
```



**Typical routes**  
- `GET /` → render **index.html**  
- `POST /start` → init session (Job Title, JD, résumé)  
- `GET /next_question` → fetch next question  
- `POST /answer` → upload audio → run pipeline → return feedback + metrics  

---

## ✅ Requirements
> **As requested:** the installation details & package commands are **preserved unchanged**.

### 1) Python & OS
- **Python:** 3.9 – 3.11 recommended  
- **OS:** Windows / macOS / Linux  
- **Microphone:** required (`sounddevice` / PortAudio)  
- **GPU (optional):** for Torch/Whisper speedups (install CUDA-matching wheels)

### 2) Python Packages
Create a virtual environment and install dependencies:

    # Create and activate (choose one)
    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # macOS/Linux:
    source .venv/bin/activate

    # Upgrade pip
    pip install -U pip

    # PyTorch/torchaudio (CPU baseline; see https://pytorch.org for CUDA builds)
    pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu

    # Core packages
    pip install -U \
      openai-whisper openai sounddevice scipy numpy pyttsx3 librosa pydub \
      pymupdf deep-translator soundfile noisereduce pyloudnorm nara_wpe \
      torchaudio hyperpyyaml ipython

### Notes
- `openai-whisper` requires FFmpeg on PATH.
- `pyttsx3` uses OS TTS backends (Windows=SAPI5, macOS=NSSpeech, Linux=eSpeak).
- `nara_wpe` provides dereverberation (WPE).
- If using GPU, install `torch/torchaudio` per your CUDA version from the official site.

### 3) External Tools
- **FFmpeg** — required by Whisper/PyDub/Librosa
    - Windows: add `...\ffmpeg\bin` to PATH
    - macOS: `brew install ffmpeg`
    - Linux: `sudo apt-get install -y ffmpeg`
- **PortAudio** — backend for `sounddevice`
    - macOS: `brew install portaudio`
    - Linux: `sudo apt-get install -y portaudio19-dev`
- **Montréal Forced Aligner (MFA)** — robust pause/phone timings  
    - Install MFA + acoustic model(s); ensure `mfa` is on PATH

### 4) Environment Variables / PATH

**macOS / Linux (bash/zsh):**

    # Recommended: headless plotting backend
    export MPLBACKEND="Agg"

    # OpenAI key (see section 5)
    export OPENAI_API_KEY="sk-..."

    # FFmpeg
    export PATH="/usr/local/bin:$PATH"           # if brew installed ffmpeg
    # or if you extracted ffmpeg to a custom dir, add its 'bin':
    export PATH="$HOME/tools/ffmpeg/bin:$PATH"

    # (Optional) MFA
    export MFA_ROOT_DIR="$HOME/.local/share/mfa"
    export PATH="$HOME/miniconda3/envs/mfa/bin:$PATH"   # adjust to your install

**Windows (PowerShell):**

    # Headless plotting backend
    setx MPLBACKEND "Agg"

    # OpenAI key (see section 5)
    setx OPENAI_API_KEY "sk-..."

    # FFmpeg (example path)
    setx PATH "C:\tools\ffmpeg\bin;%PATH%"

    # (Optional) MFA (examples; adjust to your install)
    setx MFA_ROOT_DIR "C:\Users\<you>\Documents\MFA"
    setx PATH "C:\code_projects\MFA\Library\bin;%PATH%"
    # If using a specific exe path in code, ensure it exists (see config section)

Notebook-style PATH samples you may see:
`C:\code_projects\MFA\Library\bin`  
`C:\code_projects\ffmpeg_release_full\ffmpeg-7.1.1-full_build\bin`  
Update for your machine, or add `mfa/ffmpeg` globally to `PATH`.

### 5) API Keys

**OpenAI** — required for transcription, Q&A and feedback.

**macOS / Linux:**

    export OPENAI_API_KEY="sk-..."

**Windows (PowerShell):**

    setx OPENAI_API_KEY "sk-..."

**In code, prefer:**

    from openai import OpenAI
    client = OpenAI()  # reads OPENAI_API_KEY from env

(The notebook originally uses `OpenAI(api_key="YOUR_GPT_API_KEY")`; you can replace that with the snippet above.)

---

## ⬇️ Download the Code

Clone this repo or download the ZIP:

    # Using git
    git clone https://github.com/<your-account>/<your-repo>.git
    cd <your-repo>

    # OR download ZIP from GitHub and extract it

Main legacy file: `Audio_Interview.ipynb` (the end-to-end pipeline).

---

## ▶️ Run (Web UI)

    # From the repo folder, with venv active and deps installed
    python app.py
    # Then visit http://127.0.0.1:5000/

During a session you’ll be asked for:
- **Job Title** (required)
- **Job Description** (optional)
- **Upload Résumé?** (yes/no → provide PDF path; parsed via PyMuPDF)
- **Experience Level:** Fresher / Fresher with Internship / Work Experience
- **Interview Type:** choose predefined (Behavioral/Technical/…) or custom
- **Mode:** live or recorded
- **Language:** `ml`, `en`, or `kn`

---

## 🧪 Legacy (Optional): Notebook Flow

**Option A — Run in Jupyter**

    # From the repo folder
    jupyter lab     # or: jupyter notebook

Open `Audio_Interview.ipynb`, run cells top‑to‑bottom, then execute the final cell to start prompts.

**Option B — Export to Script and Run**

    jupyter nbconvert --to script Audio_Interview.ipynb
    python Audio_Interview_converted.py

---

## ⚙️ Config You May Need to Edit
- **OpenAI client:** prefer `client = OpenAI()` (reads env var) vs hardcoding.  
- **Whisper LID model:** default `"small"`; switch to `"base"/"medium"` for tradeoffs.  
- **MFA path (Windows example):** notebook invoked `C:\code_projects\MFA\Scripts\mfa.exe`; if `mfa` is on PATH, call `"mfa"` directly.  
- **Acoustic model IDs:** e.g., `"english_mfa"`, `"tamil_cv"` — ensure they exist in your MFA install.  
- **Deep enhancement model dir:** e.g.:

        C:/code_projects/RP2/pretrained_models/enhance

    Required libs:

        pip install torch torchaudio soundfile speechbrain pyyaml

    Directory should include `hyperparams.yaml` and `enhance_model.ckpt`.  
    Update `preprocess_audio_pipeline(voice_file, model_dir="...")` or temporarily disable enhancement.

---

## 📤 Outputs
- **Temp audio:** `response.wav`, `temp_cleaned.wav`, `voice_after_cleaning.wav`, per-question takes (e.g., `answer_2_try1.wav`)  
- **Session history:** `history.json` (questions, answers, metrics)  
- **UI panes:** **Reference model answer** (optional), **AI feedback**, **Delivery feedback**, **Suggestions**

---

## ⏱ Optional: MFA Alignment

    # 1) Create & activate Conda env
    conda create -n mfa_env python=3.10 -y
    conda activate mfa_env

    # 2) Install MFA from conda-forge
    conda install -c conda-forge montreal-forced-aligner -y

    # 3) Verify
    mfa version

    # 4) Download example models
    mfa model download acoustic english
    mfa model download dictionary english_us_arpa

To compute accurate pause counts/durations & word timings:
1) Install MFA + suitable acoustic model & dictionary.  
2) Ensure `mfa` is callable (PATH or explicit path).  
3) Pipeline writes transcripts and calls MFA to produce JSON alignment.  
4) Analyzer expects phone entries to compute pause durations (silences ≥ threshold).  
**If MFA isn’t installed, choose “no” for voice analysis.**

---

## 🧩 Troubleshooting

- **FFmpeg not found**

      OSError: [Errno 2] No such file or directory: 'ffmpeg'

  Install FFmpeg and ensure its `bin` is on `PATH`.

- **Microphone / PortAudio errors**

      sounddevice.PortAudioError: Error opening InputStream

  Allow mic permissions; verify input device exists.  
  Install PortAudio (`brew install portaudio` or `sudo apt-get install portaudio19-dev`).

- **TTS silent on Linux**

      pyttsx3 did not speak

  Install `espeak` / `espeak-ng`.

- **CUDA/Torch mismatch**
  - Install the correct `torch/torchaudio` for your CUDA from https://pytorch.org.  
  - For CPU-only, use the `--index-url` shown in **Requirements**.

- **MFA alignment fails / JSON missing**
  - Ensure `mfa` is on `PATH` or update the hard-coded path.  
  - Verify installed model names match code (e.g., `english_mfa`).  
  - Skip MFA by selecting “no” if not needed.

- **OpenAI authentication**

      openai.AuthenticationError / No API key provided

  Set `OPENAI_API_KEY` and use `client = OpenAI()`.

- **Port already in use**
  - Stop other servers, or run the app on a different port (if you added a `--port` flag).

---

## 🔐 Security Note
Do **not** hardcode API keys. Prefer environment variables or a `.env` (git-ignored).  
Remove temp WAVs and `history.json` if you don’t want to keep local artifacts.

---

## 📄 Sample requirements.txt

    openai-whisper
    openai>=1.30.0
    sounddevice
    numpy
    scipy
    pyttsx3
    librosa
    pydub
    PyMuPDF
    deep-translator
    soundfile
    noisereduce
    pyloudnorm
    nara-wpe
    torch
    torchaudio
    hyperpyyaml
    ipython

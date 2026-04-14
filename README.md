# Speech-to-text-Translation

Simple speech-to-text translation using OpenAI Whisper, with an included n8n workflow export.

## What this project does

- Takes an audio file as input
- Uses Whisper to translate speech to English text
- Prints a JSON response with:
  - `text`: translated text
  - `language`: detected source language name (for known language codes)

## Repository contents

- `transcribe_translate.py` — Python script for transcription + translation
- `Whisper-texttospeech.json` — n8n workflow export
- `Hindi-test-audio.wav` — sample audio file

## Requirements

- Python 3.8+
- `openai-whisper` Python package
- `ffmpeg` installed on your system (required by Whisper)

## Setup

1. Install Whisper:

```bash
pip install -U openai-whisper
```

2. Install FFmpeg (platform-specific):
   - macOS: `brew install ffmpeg`
   - Ubuntu/Debian: `sudo apt install ffmpeg`
   - Windows: install FFmpeg and add it to `PATH`

## Run the script

```bash
python3 transcribe_translate.py "/absolute/path/to/audio.wav"
```

Example:

```bash
python3 transcribe_translate.py "./Hindi-test-audio.wav"
```

## Expected output

```json
{"text":"...translated text...","language":"Hindi"}
```

## n8n usage

1. Import `Whisper-texttospeech.json` into n8n.
2. Update file paths in the **Execute Command** node to match your machine.
3. Run the workflow manually.

## Notes

- The script currently uses Whisper model `base` (`MODEL_NAME = "base"`).
- SSL verification is bypassed in the script (`BYPASS_SSL = True`). For production use, set it to `False`.

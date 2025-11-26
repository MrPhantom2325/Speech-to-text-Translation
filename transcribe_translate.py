#!/usr/bin/env python3
import os, sys, json, ssl, whisper

MODEL_NAME = "base"
BYPASS_SSL = True

if BYPASS_SSL:
    ssl._create_default_https_context = ssl._create_unverified_context

if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
    sys.exit(1)

audio = sys.argv[1]
model = whisper.load_model(MODEL_NAME)
res = model.transcribe(audio, task="translate")

lang_map = {
    "hi": "Hindi",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    # extend as needed
}

code = res.get("language", "")
language_name = lang_map.get(code, code)

print(json.dumps({"text": res.get("text", ""), "language": language_name}))

import os
import uuid
from subprocess import run
from faster_whisper import WhisperModel

_MODEL_CACHE = {}

def get_model(mode: str) -> WhisperModel:
    if mode not in _MODEL_CACHE:
        _MODEL_CACHE[mode] = WhisperModel(
            mode,
            device="cpu",
            compute_type="int8",
            cpu_threads=2
        )
    return _MODEL_CACHE[mode]

def transcribe(file: str, mode: str = "base") -> str:
    os.makedirs("tmp", exist_ok=True)
    tmp_wav = f"tmp/{uuid.uuid4().hex}.wav"

    try:
        run([
            "ffmpeg",
            "-y",
            "-i", file,
            "-ac", "1",
            "-ar", "16000",
            tmp_wav
        ], check=True)

        model = get_model(mode)
        lines: list[str] = []

        segments, info = model.transcribe(
            tmp_wav,
            word_timestamps=False,
            beam_size=1
        )

        for segment in segments:
            lines.append(segment.text.strip())

        return "\n".join(lines)

    finally:
        if os.path.exists(tmp_wav):
            os.remove(tmp_wav)



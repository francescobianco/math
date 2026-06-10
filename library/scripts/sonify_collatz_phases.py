#!/usr/bin/env python3
"""Sonify the Collatz phase sequence.

The phase of an integer is phi(n) = sigma(n) mod 3, where sigma(n) is the
total stopping time of n under the Collatz map (see the paper
"The Phases of Collatz"). This script maps the three phases to the three
notes of a major triad and renders the phase word phi(1) phi(2) phi(3) ...
as audio:

    phase 0 -> C4    phase 1 -> E4    phase 2 -> G4

What to listen for:

  * local rigidity — 62% of consecutive integers share a phase, so notes
    repeat far more often than chance: the line is oddly singable;
  * forbidden words — from length 6 on, certain figures never occur;
  * no refrain — the sequence provably never settles into a repeating
    motif (no translational period, by theorem).

Usage:
    python3 library/scripts/sonify_collatz_phases.py [count] [note_ms]

Defaults: count=1024 integers, note_ms=90. Output is written to
library/audio/collatz-phases.wav (sample rate 22050 Hz, mono 16-bit).
"""

from __future__ import annotations

import sys
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
AUDIO_DIR = ROOT / "library" / "audio"
OUTPUT = AUDIO_DIR / "collatz-phases.wav"

RATE = 22050
FREQS = {0: 261.63, 1: 329.63, 2: 392.00}  # C4, E4, G4


def stopping_times(count: int) -> np.ndarray:
    sigma = np.zeros(count + 1, dtype=np.int64)
    for n in range(2, count + 1):
        m, steps = n, 0
        while m >= n:
            m = m >> 1 if m % 2 == 0 else 3 * m + 1
            steps += 1
        sigma[n] = steps + sigma[m]
    return sigma


def main() -> None:
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1024
    note_ms = int(sys.argv[2]) if len(sys.argv) > 2 else 90

    sigma = stopping_times(count)
    phases = sigma[1:] % 3

    samples_per_note = int(RATE * note_ms / 1000)
    t = np.arange(samples_per_note) / RATE
    envelope = np.minimum(1.0, np.minimum(t, t[::-1]) / 0.01)  # 10 ms ramps

    notes = {
        k: (0.6 * envelope * np.sin(2 * np.pi * f * t)) for k, f in FREQS.items()
    }
    signal = np.concatenate([notes[int(p)] for p in phases])
    pcm = (signal * 32767).astype(np.int16)

    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    with wave.open(str(OUTPUT), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(RATE)
        wav.writeframes(pcm.tobytes())

    seconds = len(pcm) / RATE
    print(f"Wrote {OUTPUT} ({seconds:.0f} s, {OUTPUT.stat().st_size / 1e6:.1f} MB)")
    print(f"Phases of n = 1..{count}; notes C4/E4/G4 at {note_ms} ms each.")


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""Generate the SIx Neural Core interface assets, deterministically.

Renders the five hero frames (one per visual state) and the looping
state-cycle GIF from ``src/neural_core_interface.py``:

    assets/neural-core/idle.png        900x900 hero frame
    assets/neural-core/listening.png   900x900 hero frame
    assets/neural-core/thinking.png    900x900 hero frame
    assets/neural-core/responding.png  900x900 hero frame
    assets/neural-core/learning.png    900x900 hero frame
    assets/neural-core.gif             20 frames: 4 phases x 5 states

Every frame is a pure function of (state, phase, size, seed), so
re-running this script reproduces the shipped assets byte-for-byte.
The GIF frames share one quantised palette (from the IDLE hero frame)
to keep the loop under a sensible file size.

Usage:  python3 scripts/generate_neural_core_assets.py
"""
import logging
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from PIL import Image

from src.neural_core_interface import (
    DEFAULT_SEED,
    STATE_ORDER,
    render_frame,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

REPO_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
FRAME_DIR = os.path.join(REPO_ROOT, "assets", "neural-core")
GIF_PATH = os.path.join(REPO_ROOT, "assets", "neural-core.gif")

HERO_SIZE = 900
GIF_SIZE = 900
PHASES_PER_STATE = 4
FRAME_DURATION_MS = 450
GIF_COLORS = 192

# One photogenic phase per state for the still hero frames.
HERO_PHASES = {
    "IDLE": 0.25,
    "LISTENING": 0.30,
    "THINKING": 0.40,
    "RESPONDING": 0.45,
    "LEARNING": 0.70,
}


def generate() -> dict:
    os.makedirs(FRAME_DIR, exist_ok=True)
    written = {}

    heroes = {}
    for state in STATE_ORDER:
        frame = render_frame(state, phase=HERO_PHASES[state.value],
                             size=HERO_SIZE, seed=DEFAULT_SEED)
        path = os.path.join(FRAME_DIR, f"{state.value.lower()}.png")
        frame.save(path)
        heroes[state] = frame
        written[path] = os.path.getsize(path)
        logger.info("hero frame: %s (%d bytes)", path, written[path])

    # Shared palette from the IDLE hero so the GIF does not flicker.
    palette_source = heroes[STATE_ORDER[0]].quantize(
        colors=GIF_COLORS, method=Image.MEDIANCUT)

    gif_frames = []
    for state in STATE_ORDER:
        for step in range(PHASES_PER_STATE):
            phase = step / PHASES_PER_STATE
            frame = render_frame(state, phase=phase, size=GIF_SIZE,
                                 seed=DEFAULT_SEED)
            gif_frames.append(frame.quantize(palette=palette_source,
                                             dither=Image.FLOYDSTEINBERG))
    gif_frames[0].save(
        GIF_PATH,
        save_all=True,
        append_images=gif_frames[1:],
        duration=FRAME_DURATION_MS,
        loop=0,
        optimize=True,
    )
    written[GIF_PATH] = os.path.getsize(GIF_PATH)
    logger.info("state-cycle GIF: %s (%d frames, %d bytes)",
                GIF_PATH, len(gif_frames), written[GIF_PATH])
    return written


if __name__ == "__main__":
    results = generate()
    for path, size_bytes in results.items():
        print(f"{os.path.relpath(path, REPO_ROOT)}: {size_bytes} bytes")

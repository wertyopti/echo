#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Refactored "э́хо.py" (echo) game script.

Changes:
- Structured code into functions (main, show_intro, canyon_game, echo_battle).
- Safe pygame import/initialization with fallbacks if audio is unavailable.
- Input handling normalized (case-insensitive, accepts numbers or phrases).
- English comments added explaining logic.
- Fixed various logic/flow bugs and improved readability.
"""

import sys
import os
import time
import random

# --------------------
# Audio helpers
# --------------------
def resource_path(relative_path: str) -> str:
    """
    Get an absolute path to a resource, works for dev and PyInstaller.
    """
    base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base_path, relative_path)


# Try to import and initialize pygame mixer; if unavailable, audio will be skipped.
AUDIO_AVAILABLE = False
try:
    import pygame
    try:
        pygame.mixer.init()
        AUDIO_AVAILABLE = True
    except Exception:
        # Mixer couldn't initialize; continue without sound.
        AUDIO_AVAILABLE = False
except ImportError:
    AUDIO_AVAILABLE = False


def play_music_if_available(filename: str, loop: bool = True) -> None:
    """
    Load and play a music file if pygame mixer was initialized successfully.
    """
    if not AUDIO_AVAILABLE:
        return
    path = resource_path(filename)
    if not os.path.exists(path):
        # File missing; don't crash—just skip audio.
        return
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1 if loop else 0)
    except Exception:
        # If loading/playing fails, ignore audio errors.
        pass


# --------------------
# Game logic
# --------------------
def show_intro() -> None:
    """
    Print intro screens with short delays. Non-blocking for input later.
    """
    play_music_if_available("gta-4-loading-screen-theme.mp3")
    print("WERTY GAMES COMPANY")
    time.sleep(1.5)
    print("present echo (эхо)")
    time.sleep(1.5)
    print("developers: wertyopti")
    time.sleep(1.5)
    print("thanks deepseek for dark theme in idle")
    time.sleep(1.5)
    # Original message contained explicit vulgar phrase; replaced with neutral message.
    print("loading complete...")
    time.sleep(1)


def normalized_input(prompt: str = "") -> str:
    """
    Read input and normalize it for comparison. Strips whitespace and lowercases.
    """
    try:
        return input(prompt).strip().lower()
    except EOFError:
        # Treat EOF like an empty string, allowing graceful exit.
        return ""
    except KeyboardInterrupt:
        # Allow Ctrl+C to exit the game.
        print("\nExiting game.")
        sys.exit(0)


def echo_battle() -> None:
    """
    A small battle routine where player must select the correct spell
    to damage/destroy demons. Uses random expected spell each turn.
    """
    # Number of successful hits needed to win.
    hits_needed = 3
    hits = 0
    mistakes = 0

    # Mapping valid commands (in russian/english and numeric shortcuts) to indices.
    command_map = {
        "1": "exit demons",
        "2": "damage demons",
        "3": "destroy demons",
        "exit demons": "exit demons",
        "damage demons": "damage demons",
        "destroy demons": "destroy demons",
        # allow Russian variants (commonly used in original)
        "выйти демонов": "exit demons",
        "повредить демонов": "damage demons",
        "уничтожить демонов": "destroy demons",
        "да": "да",
        "нет": "нет",
    }

    print("You entered the demon battle.")
    while True:
        # Choose the correct command for this turn (1..3)
        correct_index = random.randint(1, 3)
        print("\nChoose your spell (type number or phrase):")
        print("1 - exit demons   2 - damage demons   3 - destroy demons")
        user = normalized_input("> ")

        chosen = command_map.get(user, None)

        # Check whether the user's chosen action corresponds to the correct index.
        if chosen in ("exit demons", "damage demons", "destroy demons"):
            # Map the chosen phrase back to an index for comparison
            chosen_index = {"exit demons": 1, "damage demons": 2, "destroy demons": 3}[chosen]
            if chosen_index == correct_index:
                hits += 1
                print("Good! You dealt damage to the demons.")
            else:
                mistakes += 1
                print("Wrong spell — it had no effect.")
        else:
            # Unrecognized command treated as a mistake
            mistakes += 1
            if user == "":
                print("No command entered.")
            else:
                print(f"Unrecognized command: {user}")

        # Win condition
        if hits >= hits_needed:
            print("\nYou destroyed the demons. Good ending!")
            # Offer extra content
            print("Show extra? (да / нет)")
            choice = normalized_input("> ")
            if choice == "да" or choice == "yes":
                print("EXTRA:")
                print("Next game by this developer: windows 13 on scratch")
            break

        # Lose condition: three mistakes
        if mistakes >= 3:
            print("\nYou were captured by the demons. Bad ending.")
            break


def canyon_game() -> None:
    """
    Main canyon interaction loop. Player can type commands; repeated non-commands
    will be echoed back until 'open demon' is entered to start the battle.
    """
    play_music_if_available("Dungeons_Dragons_Po_Tu_Storonu_Stranic_-_Dark_Fantasy_Dungeons_Caves_Ambience._Muzyka_dlya_DnD_A_(SkySound.cc).mp3")

    echo_count = 0
    echo_once_flag = False

    print("Speak into the canyon (type commands). Type 'open demon' to start the demon encounter.")
    while True:
        # If user has typed non-commands several times, show story progression.
        if echo_count == 3:
            print("\nOH YES, YOU BECAME STRONGER. The canyon swallowed you.")
            print("Police officer: Three days ago, three people were found around pictograms here...")
            print("Middle ending.")
            break

        if echo_count == 2 and not echo_once_flag:
            print("\nCONTINUE...")
            echo_once_flag = True

        cmd = normalized_input("> ")

        if cmd == "open demon":
            time.sleep(1)
            print("\nYou freed the canyon from three demons; now you are cursed instead.")
            print("Police officer: Three days ago, three people were found around pictograms here. According to the exorcist, they were cursed...")
            # Enter the battle routine
            echo_battle()
            break
        else:
            # Echo what the player said, similar to original behavior.
            time.sleep(0.5)
            # If empty input, give a hint
            if cmd == "":
                print("(You can say something, or type 'open demon' to proceed.)")
            else:
                print(cmd)  # echo back
            echo_count += 1


def main() -> None:
    """
    Main entry point for the script.
    """
    show_intro()

    # Start the canyon game. After it finishes, wait a bit then exit.
    canyon_game()
    print("\nGame over. Thank you for playing.")
    time.sleep(1)


if __name__ == "__main__":
    main()

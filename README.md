<h1 align="center">Rbxlx-2-Rojo</h1> 

<div align="center">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/TuiDevelops/shield-scan?style=for-the-badge" height="25px"> 
  <img alt="GitHub languages" src="https://img.shields.io/github/languages/count/TuiDevelops/shield-scan?style=for-the-badge" height="25px"> 
  <img alt="GitHub forks" src="https://img.shields.io/github/forks/TuiDevelops/shield-scan?style=for-the-badge" height="25px"> 
  <img alt="GitHub issues or pr" src="https://img.shields.io/github/issues/TuiDevelops/shield-scan?style=for-the-badge" height="25px"> 
  <img alt="GitHub issues or pr" src="https://img.shields.io/github/issues-pr/TuiDevelops/shield-scan?style=for-the-badge" height="25px"> 
  <img alt="GitHub stars" src="https://img.shields.io/github/stars/TuiDevelops/shield-scan?style=for-the-badge" height="25px"> 
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/TuiDevelops/shield-scan?style=for-the-badge" height="25px"> 
</div>

<img width="1280" height="720" alt="rbxlx2rojo" src="https://github.com/user-attachments/assets/c60b4d8d-59f3-4dc7-813d-c5525201dbaf" />


Rbxlx-2-Rojo is a desktop tool designed to help Roblox developers migrate existing **Roblox Studio games (.rbxlx)** into a **Rojo-compatible project structure**, enabling proper version control and a modern development workflow using editors like Visual Studio Code.

This project was created to simplify the transition from traditional Roblox Studio development to a source-controlled environment, without requiring the game to be rebuilt from scratch.

---

## Overview

Many Roblox developers start projects directly inside Roblox Studio, which makes long-term maintenance, collaboration, and versioning difficult. Rojo solves this by synchronizing files from the local filesystem into Roblox Studio — but migrating an already existing game can be complex and time-consuming.

Rbxlx-2-Rojo addresses this problem by:
- Reading a `.rbxlx` file
- Extracting scripts and relevant instances
- Rebuilding them into a folder structure compatible with Rojo

The result is a project that can be managed with Git, edited in external editors, and synced back into Roblox Studio using Rojo.

---

## Features

- Converts `.rbxlx` files into a Rojo-friendly structure
- Desktop graphical interface (GUI)
- Real-time conversion logs
- Clean, dark-themed UI
- Cross-platform support (Linux and Windows)
- Designed for simplicity and usability

---

## User Interface

The interface is intentionally minimal and focused:
- File selector for the `.rbxlx` game file
- Output directory selector
- One-click conversion
- Read-only log panel for feedback and errors

The UI was first designed in Figma and later implemented using Tkinter.

---

## Project Structure

```text
.
├── app.py          # Graphical user interface
├── converter.py    # Conversion controller and workflow
├── parser.py       # RBXLX parsing logic
├── emitter.py      # Rojo project generation
├── LICENSE         # License and usage terms
└── README.md

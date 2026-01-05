<h1 align="center">Rbxlx-Rojo-Converter</h1> 

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

---

## About

**Rbxlx-Rojo-Converter** is a desktop tool designed to help Roblox developers migrate existing  
**Roblox Studio games (`.rbxlx`)** into a **Rojo-compatible project structure**, enabling proper version control and a modern development workflow using editors like Visual Studio Code.

This project simplifies the transition from traditional Roblox Studio development to a source-controlled environment, **without rebuilding the game from scratch**.

---

## Overview

Many Roblox developers start projects directly inside Roblox Studio, which makes long-term maintenance, collaboration, and versioning difficult.

Rojo solves this by synchronizing files from the local filesystem into Roblox Studio — but migrating an already existing game can be complex and time-consuming.

**Rbxlx-Rojo-Converter** addresses this problem by:

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
- Designed for simplicity and usability

---

## User Interface

The interface is intentionally minimal and focused:

- File selector for the `.rbxlx` game file
- Output directory selector
- One-click conversion
- Read-only log panel for feedback and errors

The UI was first designed in Figma and later implemented using **Tkinter**.

---

## Installation(Linux Only)

We recommend using Gear Lever, a graphical AppImage manager available on Flathub.
It allows you to install AppImages with a simple drag-and-drop interface and automatically integrates the app into your system.

### Step 1 – Install Gear Lever

    flatpak install flathub it.mijorus.gearlever

### Step 2 – Download the AppImage

Download the latest version from the Releases page:

    RBXLX-Rojo-Converter-1.0.0-x86_64.AppImage

### Step 3 – Install
1. Open Gear Lever

2. Drag the AppImage into the window

3. Click Install

4. The application will now appear in your system menu.

---

## How to Use

### Step 1 - Launch Rojo
Open the terminal, and launch Rojo:

    aftman init
    
    aftman add rojo-rbx/rojo
    
    aftman install
    
    rojo init

### Step 2 - Launch Rbxlx-Rojo-Converter
1. Open the Rbxlx-Rojo-Converter
2. Select the .rbxlx file
3. Select the folder where the project should be located
4. Click convert, and your project is now ready!

## License
This project is licensed under the terms described in the LICENSE file.

## Project Structure
   ```bash
  ├── app.py          # Graphical user interface
  ├── converter.py    # Conversion controller and workflow
  ├── parser.py       # RBXLX parsing logic
  ├── emitter.py      # Rojo project generation
  ├── project.py      # Project's json generation
  ├── LICENSE         # License and usage terms
  └── README.md

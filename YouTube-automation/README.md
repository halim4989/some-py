# YouTube Video Downloader & Editor  
*Download, cut, and merge YouTube videos effortlessly — powered by Pytube + FFmpeg.*

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)  
![License](https://img.shields.io/badge/License-MIT-green.svg)  
![Pytube](https://img.shields.io/badge/Uses-Pytube-orange.svg)  
![FFmpeg](https://img.shields.io/badge/Backend-FFmpeg-red.svg)

---

## Overview

This project automates YouTube video editing using Python.  
It downloads a video in a **specific resolution**, separates the **audio**, **splits** the video at a given timestamp (to the nearest **keyframe**), and then **merges** it with another audio track — all without re-rendering the video.

> 💡 Because the splitting is done on keyframes, the process is **super fast and lossless**.

---

##  Key Features

 Download videos from YouTube using **Pytube**  
 Extract and replace **audio tracks**  
 Split video at the **nearest keyframe** of a given timestamp  
 Skip re-rendering for **ultra-fast editing**  
 Automatically save results in organized folders  

---

##  How It Works

1. **Download Video** → `Pytube` fetches the chosen resolution.  
2. **Split Video** → `ffmpeg` (run through `subprocess`) cuts the video at the nearest keyframe.  
3. **Extract Audio** → `ffmpeg` separates the audio track.  
4. **Merge Tracks** → The processed video and new audio are combined into a final file.  

All results are stored inside an automatically created `output/` folder.

---

##  Why Two `-ss` Flags in FFmpeg?

Using two `-ss` flags is a common **two-step seek technique**:

| Flag | Placement | Description | Speed | Accuracy |
|------|------------|-------------|--------|-----------|
| `-ss` (before `-i`) | Input-level seek | Fast but may be inaccurate | ⚡ Very Fast | ❌ Rough |
| `-ss` (after `-i`)  | Output-level seek | Accurate, decodes keyframes | 🕒 Slower | ✅ Precise |

 **Combining both** gives you **speed** + **accuracy** for precise, efficient cutting.

---

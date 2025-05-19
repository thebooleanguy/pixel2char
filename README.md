# 🎥 pixel2char

**pixel2char** is a fun little Python script that turns your webcam feed into real-time ASCII art in the terminal.

It captures frames from your webcam, downsizes them to 40x40, converts them to grayscale, and then maps the brightness levels to ASCII characters for a cool, live pixel-art effect.

This was my first time playing around with OpenCV in Python — mostly recreational and definitely not practical — but it was a fun mini weekend project!

## 🔧 Requirements
- Python 3
- `opencv-python`

Install OpenCV with:
```bash
pip install opencv-python
````

## 🚀 Run it

```bash
python pixel2char.py
```

Use `Ctrl + C` to exit the loop.

## 🤔 Notes

* The ASCII art isn’t super clear (yet) — it's more on the artistic/abstract side.
* It works best in well-lit conditions with a decent webcam feed.
* Tested on Linux (uses `clear` to wipe terminal); might need changes for Windows (`cls`).

## 💡 Future Ideas

* Tune character mapping for better clarity
* Add color?
* Output to a text file or stream

## 📸 Preview

*(Imagine a bunch of ASCII characters dancing in your terminal based on your camera feed. Yep, that’s it.)*

---

🧠 Just a fun experiment in Python + OpenCV!

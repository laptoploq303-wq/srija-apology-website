# Srija Apology Website

## Page flow

1. `/` → Homepage
2. Click **It's Okay** → `/next`
3. Click **Please Forgive Me & Seal Promise Srija 😭🤝💖** → `/last`

## Run locally

```bash
python -m pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000/

The three original HTML designs are kept as Flask templates with only the navigation behavior wired up.


## Background music

The website now embeds the supplied YouTube video (`pr3iC9Vmfe8`) as looping background music on all three pages. Autoplay starts muted where required by browser policy; the first user interaction attempts to enable the audio.

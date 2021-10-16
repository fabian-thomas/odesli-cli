# odesli-cli

CLI client for the Odesli/Songlink API.

## Installation

```bash
pip install odesli-cli
```

### From source

Install the PyPI package `build`:
```bash
pip install build
```

Then (from the root of the repo):
```bash
pip install dist/*.whl
```

## Sample usages:

### Get information on a song by it's url
```bash
odesli-cli '{URL}' all
```

### Convert current spotify track to tidal link and copy it to the X clipboard
```bash
current_spotify="$(qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Metadata | grep xesam:url |  awk '{print $2}')"
odesli-cli "$current_spotify" --provider tidal link | xclip -selection clipboard
```

### Convert link to spotify album in cliboard to tidal album link and copy it to the X clipboard
```bash
link="$(xclip -o -sel clip)"
odesli-cli "$link" --provider tidal link | xclip -selection clipboard
```

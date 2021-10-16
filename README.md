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

### Convert current Spotify track to Tidal link and copy it to the X clipboard
```bash
current_spotify="$(qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Metadata | grep xesam:url |  awk '{print $2}')"
odesli-cli "$current_spotify" --provider tidal link | xclip -selection clipboard
```

### Open Tidal, Spotify, Deezer, etc. links directly in the Spotify app (the coolest one)
For this functionality one needs to hack a bit more. I have it all set up with my Linux dofiles, so trust me, it works.
Just some key points to make it work:
- create a shell script that can handle all sorts of http(s) links and set it as the mime default
- match Tidal, etc. links, convert them with this tool and play them with `qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.OpenUri "{URI}"`
- match Spotify links and play them directly with above command (note that you need to convert the url to a uri in both cases)
If you need additional information don't hesitate to contact me via mail.

I haven't tried the dbus command for playing with the Tidal or Deezer apps, but it may work for them in the same fashion.

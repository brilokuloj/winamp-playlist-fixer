# Winamp Playlist Fixer

I recently switched from Windows to Linux full-time, but didn't want to have to go back into Windows to manually save all of my temporary playlists all-by-one, especially when I knew that data was just sitting on my hard drive unused.

## How to Use

Winamp playlists are located in `C:/Users/USER/AppData/Roaming/Winamp/Plugins/ml/playlists` on Windows. Copy the contents of this folder into `/src/` relative to `fixer.py`, make an empty `/out/` folder, then run.

The `directory` variable can be edited to your music folder, if you keep your playlists in the root of your music folder like I do. Handy for using playlists on other devices.

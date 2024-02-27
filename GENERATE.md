# Generating Screenshots

Mostly internal notes for V35 folks that are convenient to leave here.

## Preparation 

### Profile folder

1. Make a clean user folder for screenshots: `mkdir ~/screenshot_profile;cp license.dat ~/screenshot_profile`
1. Save [screenshots.py](./screenshots.py) to your `screenshot_profile/plugins` folder.
1. Launch BN with that profile: `BN_SCREENSHOT=true BN_USER_DIRECTORY=/Users/username/screenshot_profile /Applications/Binary\ Ninja.app/Contents/MacOS/binaryninja`
1. Install the Screenshot Ninja plugin
1. Add a `[CTRL] R` hotkey to the Restart action to make life easier
1. Restart BN (command-palette)

### Layouts

Make two window layouts (I used "ss1" and "ss2"). Match the existing look and feel of the two rendered views. The goal is to show as much as possible of different UI elements in each shot.

## Screenshotting

(You should auomatically start with Ninja Edit as your theme in 4.0 and beyond)

1. Open a well marked up database, pick a consistent spot (will be remembered after the first load)
1. Load layout "ss1" (command palette, ss1)
1. Select UI elements for xrefs or mini graph
1. `[CTRL+SHIFT] 1` to save the first screenshot
1. Load layout "ss2" (command palette, ss2)
1. Select UI elements for xrefs or mini graph
1. `[CTRL+SHIFT] 2` to save the second screenshot
1. `[CTRL+SHIFT] 0` to select the next theme
1. `[CTRL] R` to restart BN

Repeat until sound changes to let you know you're done and you see a log warning.

## Optional Optimizing

Currently using [ect](https://github.com/fhanau/Efficient-Compression-Tool) to compress all saved PNG files.

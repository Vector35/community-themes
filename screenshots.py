from pathlib import Path
from binaryninja import user_directory, log_error, log_alert, Settings
from binaryninjaui import UIContext, UIAction, UIActionHandler
from PySide6.QtGui import QKeySequence

from time import sleep, time
import os
import sys
sys.path.append(str(Path(user_directory()) / "repositories" / "community" / "plugins"))
import jonpalmisc_screenshot_ninja as screenshot

# Currently not working in 4.0, will fix and use to switch layouts later
def action(s: str):
    execute_on_main_thread_and_wait(lambda: UIContext.activeContext().getCurrentActionHandler().executeAction(s))
    sleep(1)

themename = Settings().get_string("ui.theme.name")
themes = Settings().query_property_string_list("ui.theme.name", "enum")
themedir = Path(user_directory()) / "community-themes" / "previews"

def theme_file(themename):
    for f in themedir.glob("*.bntheme"):
        with open(f) as fh:
            data = fh.read()
            if themename in data:
                return f
    return (themedir / Path(themename.lower().replace(" ","")).with_suffix(".bntheme"))

themeimagebase = theme_file(themename).with_suffix("") #strip the extension

def take1(_):
    qpm = screenshot.renderActiveWindow(2)
    qpm.save(str(themeimagebase) + "1.png")
    # This is a horrible, horrible hack, but QApplication.beep() wasn't working
    if "darwin" in sys.platform:
        os.system("/usr/bin/afplay /System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Resources/Sounds/ClickFast.aiff")

def take2(_):
    qpm = screenshot.renderActiveWindow(2)
    qpm.save(str(themeimagebase) + "2.png")
    # This is a horrible, horrible hack, but QApplication.beep() wasn't working
    if "darwin" in sys.platform:
        os.system("/usr/bin/afplay /System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Resources/Sounds/ClickFast.aiff")

def next_theme(_):
    idx = themes.index(themename)
    idx = (idx + 1) % len(themes)
    # Is this recent?
    newname = themes[idx]
    testimage = Path(str(theme_file(newname).with_suffix("")) + "1.png")
    currenttime = time()
    if testimage.is_file():
        modtime = testimage.stat().st_mtime
    if testimage.is_file() and modtime > currenttime - 43200:
        if "darwin" in sys.platform:
            os.system("/usr/bin/afplay /System/Library/Sounds/Glass.aiff")
        log_alert("No more themes, all themes updated") 
    else:
        Settings().set_string("ui.theme.name", themes[idx])
    log_error(f"Restart now! Theme now set to {themes[idx]}")

UIAction.registerAction("Take First Theme Screenshot", QKeySequence("Meta+Shift+1"))
UIAction.registerAction("Take Second Theme Screenshot", QKeySequence("Meta+Shift+2"))
UIAction.registerAction("Next Theme", QKeySequence("Meta+Shift+0"))
UIActionHandler.globalActions().bindAction("Take First Theme Screenshot", UIAction(take1))
UIActionHandler.globalActions().bindAction("Take Second Theme Screenshot", UIAction(take2))
UIActionHandler.globalActions().bindAction("Next Theme", UIAction(next_theme))

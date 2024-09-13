% changelog

## 1.2.0

This version is aimed at further improving the user experience and existing
content polishing. Now you can reassign keyboard shortcuts as you wish. It is
now possible to record your gameplay and play back the resulting recordings
using the built-in player for such recordings. An object map and several other
improvements and fixes are also in place.

We have opened the official [github translation
repository](https://github.com/sooslandia/translations). If you want to
translate the game and have the ability, we will be glad to accept your help.

### New features

- New translations added.
   - Turkish. Translator [fatihyuksek](https://github.com/fatihyuksek1).
   - Indonesian. Translator [MuhammadGagah](https://github.com/MuhammadGagah).
- You can now change the default keyboard shortcuts.
   - To do that, click the "Customize Keyboard Shortcuts" button located on the
"Keyboard Shortcut Configuration" tab on the Settings screen.
   - Your configuration file is located in the user data folder (userData) and is
called keyConfig.json. You can share your configuration with other people. In
order for someone else's configuration to work for you, you need to replace your
configuration file with the one you received from the other person.
   - You can find out more about configuration setting in the corresponding section
of the documentation.
- You can now record your gameplay.
   - You can check the box that determines whether your gaming session will be
recorded on the updated game mode selection screen. The recording behavior can
be configured in the Recording tab of the Settings screen.
   - You can play recordings from the recordings menu, which can be accessed by
activating the corresponding item in the main menu.
   - Recordings are saved in the recordings folder, located in the user data folder
(userData) and have a .sgr extension. The recording file can be renamed if
necessary and shared with other people. For someone else's recording to be
detected by the game, it must be placed in the game's recording folder.
   - Information about how the recording player works and its control keys can be
found in the corresponding section of the documentation.
- Added object map.
   - It can be opened with the m key during a gaming session.
   - Navigate the map using the arrow keys. You can also find out how many objects
are on the map by pressing the o key.
   - There are two navigation modes, which you can read about in the corresponding
section of the documentation.
   - All object map hotkeys can be changed in the keyboard shortcut configuration.
- Training mode is expanded as well.
   - You can now instantly  zero the cooldown of all skills by pressing f1.
   - When you press the f2 key, a screen will open where you can change the levels
of your skills and blow force recovery rate. This screen only displays the
skills you have. You can change their level only in the range from level 1 to
the maximum current level.
- In the settings, on the "Behavior" tab, a checkbox has been added that
determines whether the first-person view state will be saved between game
sessions.
- It is now possible to delete saved game progress and reset settings to default
values.
   - This can be done in the settings, on the "General" tab.
   - You will not be able to reset settings or delete your progress if you accessed
settings through the pause menu.

### Changes

- The game mode selection screen has been changed.
   - the screen is now represented by a virtual form instead of a menu. Navigation
is similar to the settings or profile screen.
   - From the new screen you can determine whether the game session will be recorded.
- Improved profile screen interface.
   - Now any item from the statistics list can be copied to the clipboard by
pressing ctrl+c.
   - The statistics tab now displays the current number of achievement points.
   - Auras now display their bonus as well.
- Slight changes to the game balance.
   - Now for every hundred points up to a thousand, one coin will be awarded. For
example, you scored 678 points, in which case you will receive 7 coins, and
not one as before.
   - After a thousand points, everything remains as before, but the 10 coins
received remain with you. For example, you scored 1234 points, in which case
you will receive 11 coins.
- The maximum number of objects on the field has been increased.
- Now the sound played by pressing the c key in first person camera mode will
play in the center of the field.
- The file name format with critical error data has been changed to (error
yyyy_MM_dd hh-mm-ss.log)

### Fixes

- Now, when critical errors are displayed, the sound will be completely muted
instead of looping.
- Improved game stability in some cases.

## 1.1.1

### Fixes

- Fixed a critical bug that occurred when the first person mode and the ball
watch mode were active at the same time.
- Fixed some other minor bugs.

## 1.1.0

This version is focused on improving the user experiance: Successful bat hit
sound, first person camera view, alternative bat swing keys, etc.

### New features

- The game now supports translations that are missing one or more strings. If a
string is not found, the game falls back to English localization strings.
- In ball watching mode, a background sound has been attached to the ceiling,
which will help make watching more spectacular.
- Added a sound to indicate when the bat succesfully hits the ball. By default,
the notification is disabled; it is enabled in the settings, on the "Behavior"
tab.
- Implemented first-person camera mode. To switch between modes, press v while
playing.
- Errors during the update are now written to a file that will be located in the
userData/errorLogs folder.
- Added temporary alternative keys for making horizontal and vertical bat swings.
   - For a horizontal swing, use the e key, for a vertical swing, use the r key.
   - This solution is temporary and remains until the key config is implemented.
- Now items with an available reward in the statistics list are at the beginning
of the list.

### Changes

- Increased points received for perfect strike streeks, ball bounces off the
ceiling and ball with object collisions streeks.
- Documentation has been updated to take new features into account.

### Fixes

- Increased the volume of the landing sound after a jump.
- Now the leader's aura does not increase the points lost due to penalties.

## 1.0.0

Initial release.

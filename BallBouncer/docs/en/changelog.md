% changelog

## 1.3.3

### New features

- Spanish translation added. Translators: [rayo-alcantar](https://github.com/rayo-alcantar), [ogomez92](https://github.com/ogomez92).

### Changes

- Czech translation updated. Translator [4sensegaming](https://github.com/4sensegaming).

### Fixes

- Fixed a critical error that occurred when many sounds were playing simultaneously.
- Fixed issues with star modules.
   - Additional module information tab now updates when you buy upgrades.
   - The description of the "ball controller" module's controlled ball speed increase no longer includes the information about the twelve percent speed increase.
   - When pressing the key to check the current amount of star energy, the number is now announced at the beginning of the message.
   - Fixed a critical bug when activating the "ball controller" star module and the ball was caught during activation.
- Fixed the completion tracking of the "Magnetism" skill usage quest in training mode.
- Recording issues fixed.
   - When closing the game using Alt+F4 during gameplay, the recording is canceled if the "Cancel recording when manually aborting the game" checkbox is checked and properly finalized if it is not checked.
   - When the game ends prematurely due to reaching -1000 points, the recording is no longer canceled even if the "Cancel recording when manually aborting the game" checkbox is checked.
- It is now possible to play with jaws active.
- Fixed an issue with launching the game on Windows for some users.

## 1.3.2

### Fixes

- Successful bat hit sound has been fixed and now plays in all intended situations.
- Information on how to activate items has been added to the descriptions of trial of will and trial of mastery modes.
- Fixed a game crash that occurred when a screen reader other than NVDA was active.
- Issues with mp3 recordings have been fixed.
   - Potentially fixed a game crash that occurred when playing with recording enabled.
   - A special VBR header is now added to recordings. Previously, its absence could cause some players to incorrectly display the recording's duration and experience issues with seeking.
   - MP3 encoding parameters have been adjusted to reduce file size without noticeable quality loss.-
- A line has been added to the documentation explaining how to unlock the quest board (in the "Other Game Modes" section).
- Fixed a critical error that occurred when many sounds were playing simultaneously.

## 1.3.1

Fixed a bug with objects sound panning.

## 1.3.0

This is the largest update, adding a lot of new content to the game.

Three new modes await you, each of which can be upgraded, along with the quest board content featuring dozens of diverse quests. By completing these quests, you can earn stars, which can then be spent on various upgrades.

New objects will help you score even more points than you could have ever imagined.

New auras will breathe new life into your skills, while the new skills will open up even more strategies for object destruction.

And of course, there are the upgrades that affect the entire gameplay, allowing you to rack up points to unprecedented levels and create even more destruction on the playing field.

To reach the true heights, you’ll have to spend dozens of hours, but don’t be scared — those hours will be filled with unrestrained chaos of destruction and the sweetness of well-deserved rewards!

### New features

- New content added.
   - Three new modes, each with its own currency.
   - A quest board.
   - New statistics items.
   - New objects, skills, and auras, unlocked with the currencies of the new modes.
   - As well as many different upgrades that affect both the new modes and the normal game.
- The ability to view the descriptions of game modes has been added.
   - To open the description, select a mode from the list on the new game start screen and press the D key, or click the "Open Mode Description" button.

### Changes

- Now auras can be active or inactive.
   - Initially, you can use only two auras at the same time, but in the future, the number of active auras can be increased, as well as new ones can be acquired.
   - You can also open the description of an aura, except for the leader and time auras, by pressing the corresponding button on the auras tab in the profile.
- The "Furious leap" ability has been improved. Now the character can dash a greater distance.
- The balance of points awarded for high streaks of collisions, object destructions, and ball bounces off the ceiling has been adjusted.
- The upgrade cost for the Leader and Time auras has been increased. If your aura level is above five, it will be reset to zero, and the achievement points spent on upgrading it will be returned.
- Now you can activate menu items by pressing the Enter key on the numpad, and also hold Enter on buttons for rapid activations.
- The calculation of the coin reward has been refined for final scores over two million.
- The behavior of the sound playback for checking the character's position has been changed.
   - Previously: The sound played at the character's position in the field center view, and played at the center of the field in the first-person view.
   - Now: The sound always plays at the character's position, except when the first-person view is active and ball watch mode is turned off. In this case, the sound plays at the center of the field.
- The learn sounds screen has been redesigned.
   - The menu has been replaced with a virtual form.
   - Sounds, both from the base game and new modes, are now organized into separate tabs of the form for easier navigation and the ability to listen to them during gameplay.
- The method of recording gameplay has been changed.
   - Now, recordings are saved in MP3 format.
   - The old recording method has been disabled, but it is still possible to play previously recorded files.
   - New recordings will be located in userData/mp3recordings.
   - The ability to play recordings in the old format will be removed in version 1.5.0.
- Minor changes and inconsistencies  fixed in English translation.
- Setting skill levels in training mode has been fixed.
   - Now, changing skill levels will have an effect on the game session.
   - Also, now you can set any skill level up to the maximum possible.
- A critical bug has been fixed when changing controls configuration during gameplay.
- The issue where the camera did not follow the character during a jump or when using the "Furious leap" skill has been fixed.
- The accuracy of the character's hit on the ball when using the "Furious leap" skill has been increased.
- Now, when the character jumps, the penalty timer for staying in one place is reset.
- The issue that allowed opening the object map and pausing the game simultaneously, leading to strange and undesirable behavior, has been fixed.
- The error in the calculation of points for object destruction has been fixed. As a result, fewer points are now awarded for this.
- Incorrect setting of the skill cooldown time after an unsuccessful attempt has been fixed.

## 1.2.4

### Fixes

- Updated and corrected translations.

## 1.2.3

### New features

- New translations added.
   - Serbian. Translator [nidza07](https://github.com/nidza07).
   - Czech. Translator [4sensegaming](https://github.com/4sensegaming).

### Fixes

- Resolved a minor issue in the Turkish translation.
- Fixed incorrect display of in-game help.
- Fixed a potential critical error when loading a recording.

## 1.2.2

Updated Turkish and Indonesian translations.

## 1.2.1

This update fixes several critical bugs for Linux users.

## 1.2.0

This version is aimed at further improving the user experience and existing content polishing. Now you can reassign keyboard shortcuts as you wish. It is now possible to record your gameplay and play back the resulting recordings using the built-in player for such recordings. An object map and several other improvements and fixes are also in place.

We have opened the official [github translation repository](https://github.com/sooslandia/translations). If you want to translate the game and have the ability, we will be glad to accept your help.

### New features

- New translations added.
   - Turkish. Translator [fatihyuksek](https://github.com/fatihyuksek1).
   - Indonesian. Translator [MuhammadGagah](https://github.com/MuhammadGagah).
- You can now change the default keyboard shortcuts.
   - To do that, click the "Customize Keyboard Shortcuts" button located on the "Keyboard Shortcut Configuration" tab on the Settings screen.
   - Your configuration file is located in the user data folder (userData) and is called keyConfig.json. You can share your configuration with other people. In order for someone else's configuration to work for you, you need to replace your configuration file with the one you received from the other person.
   - You can find out more about configuration setting in the corresponding section of the documentation.
- You can now record your gameplay.
   - You can check the box that determines whether your gaming session will be recorded on the updated game mode selection screen. The recording behavior can be configured in the Recording tab of the Settings screen.
   - You can play recordings from the recordings menu, which can be accessed by activating the corresponding item in the main menu.
   - Recordings are saved in the recordings folder, located in the user data folder (userData) and have a .sgr extension. The recording file can be renamed if necessary and shared with other people. For someone else's recording to be detected by the game, it must be placed in the game's recording folder.
   - Information about how the recording player works and its control keys can be found in the corresponding section of the documentation.
- Added object map.
   - It can be opened with the m key during a gaming session.
   - Navigate the map using the arrow keys. You can also find out how many objects are on the map by pressing the o key.
   - There are two navigation modes, which you can read about in the corresponding section of the documentation.
   - All object map hotkeys can be changed in the keyboard shortcut configuration.
- Training mode is expanded as well.
   - You can now instantly  zero the cooldown of all skills by pressing f1.
   - When you press the f2 key, a screen will open where you can change the levels of your skills and blow force recovery rate. This screen only displays the skills you have. You can change their level only in the range from level 1 to the maximum current level.
- In the settings, on the "Behavior" tab, a checkbox has been added that determines whether the first-person view state will be saved between game sessions.
- It is now possible to delete saved game progress and reset settings to default values.
   - This can be done in the settings, on the "General" tab.
   - You will not be able to reset settings or delete your progress if you accessed settings through the pause menu.

### Changes

- The game mode selection screen has been changed.
   - the screen is now represented by a virtual form instead of a menu. Navigation is similar to the settings or profile screen.
   - From the new screen you can determine whether the game session will be recorded.
- Improved profile screen interface.
   - Now any item from the statistics list can be copied to the clipboard by pressing ctrl+c.
   - The statistics tab now displays the current number of achievement points.
   - Auras now display their bonus as well.
- Slight changes to the game balance.
   - Now for every hundred points up to a thousand, one coin will be awarded. For example, you scored 678 points, in which case you will receive 7 coins, and not one as before.
   - After a thousand points, everything remains as before, but the 10 coins received remain with you. For example, you scored 1234 points, in which case you will receive 11 coins.
- The maximum number of objects on the field has been increased.
- Now the sound played by pressing the c key in first person camera mode will play in the center of the field.
- The file name format with critical error data has been changed to (error yyyy_MM_dd hh-mm-ss.log)

### Fixes

- Now, when critical errors are displayed, the sound will be completely muted instead of looping.
- Improved game stability in some cases.

## 1.1.1

### Fixes

- Fixed a critical bug that occurred when the first person mode and the ball watch mode were active at the same time.
- Fixed some other minor bugs.

## 1.1.0

This version is focused on improving the user experiance: Successful bat hit sound, first person camera view, alternative bat swing keys, etc.

### New features

- The game now supports translations that are missing one or more strings. If a string is not found, the game falls back to English localization strings.
- In ball watching mode, a background sound has been attached to the ceiling, which will help make watching more spectacular.
- Added a sound to indicate when the bat succesfully hits the ball. By default, the notification is disabled; it is enabled in the settings, on the "Behavior" tab.
- Implemented first-person camera mode. To switch between modes, press v while playing.
- Errors during the update are now written to a file that will be located in the userData/errorLogs folder.
- Added temporary alternative keys for making horizontal and vertical bat swings.
   - For a horizontal swing, use the e key, for a vertical swing, use the r key.
   - This solution is temporary and remains until the key config is implemented.
- Now items with an available reward in the statistics list are at the beginning of the list.

### Changes

- Increased points received for perfect strike streeks, ball bounces off the ceiling and ball with object collisions streeks.
- Documentation has been updated to take new features into account.

### Fixes

- Increased the volume of the landing sound after a jump.
- Now the leader's aura does not increase the points lost due to penalties.

## 1.0.0

Initial release.

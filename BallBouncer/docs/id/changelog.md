% changelog

## 1.1.1

### Fixes

- Fixed a critical bug that occurred when the first person mode and the ball watch mode were active at the same time.
- Fixed some other minor bugs.

## 1.1.0

This version is focused on improving the user experiance: Successful bat hit sound, first person camera view, alternative bat swing keys, etc.

### Added

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
# pico-keypad-dev

Scripts for the Raspberry Pi Pico and Pimoroni RGB Keypad Base accessory.

Contains examples and libraries from Adafruit and Pimoroni, can be found here:
https://learn.pimoroni.com/article/circuitpython-and-keybow-2040#pmk-on-pico-rgb-keypad


# Setup

1. Install the Adafruit CircuitPython firmware from `uf2` to the Pico.
2. Copy the keypad required libraries from `lib` to `lib` on the Pico.
3. Copy an example from `examples` as `code.py` to test all is working.


# Scripts

## `shortcuts.py` - Media and keyboard shortcuts.

| Key | Function | Color |
|-----|----------|-------|
| 0 | Volume up | Yellow |
| 1 | Previous track | Blue |
| 2 | Play/pause | Green |
| 3 | Next track | Blue |
| 4 | Volume Down | Yellow |
| 6 | Mute volume | Red |
| 12 | Ctrl+M | Red |
| 14 | Sleep | Dark blue |
| 15 | Ctrl+Shift+Esc | Purple |

## `layers.py` - Multi-layer functions.

* Layer 1 - media controls
  * Prev/play/next
  * Vol down/mute/Vol up
  * Ctrl+M
* Layer 2 - Launch apps by Start menu search
  * Spotify/Steam/Discord
* Layer 3 - Windows/System and power options
  * Task Manager/Explorer
  * Sleep/Reboot/Shutdown
* Layer 4 - Onboard/other
  * Toggle 'stay awake'
  * Sleep keypad

## `widi_test.py` - Test Pico W WiFi connection

Requires `settings.toml` with `WIFI_SSID` and `WIFI_PASSWORD`

Example:
```
WIFI_SSID = ""
WIFI_PASSWORD = ""
```

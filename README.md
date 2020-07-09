# Double clipboard
[![MIT license](https://img.shields.io/github/license/appuchias/double_clipboard?style=flat-square)](https://github.com/appuchias/double_clipboard/blob/master/LICENSE)
[![Author](https://img.shields.io/badge/Project%20by-Appu-9cf?style=flat-square)](https://github.com/appuchias)

# How it works

After you run the script, the first thing you copy will be set to your clipboard as usual and the second thing you copy will be saved but overwritten by the first one. Clipboards will be switched when you press your right alt key or the one set in 'settings.json'. To clear your clipboard just press it again if it is set to clear your cliboard or close and run again the script.
# Setup
1. Navigate to the desired folder: `cd <path>`
2. Clone the repo: `git clone https://github.com/appuchias/double_clipboard.git`
3. Navigate into the repo folder: `cd double_clipboard`
4. Modify settings.json:\
    "key" is the desired key for switching between clipboards. See special key names [here](https://github.com/boppreh/keyboard#keyboard.all_modifiers).\
    "clear" determines if you want your clipboards to be erased after you use both of them.\
    *By default, the switch key is the right alt and clear is set to true.*
5. Run the file: `python main.py`

# License
This project is licensed under the [MIT license](https://github.com/appuchias/double_clipboard/blob/master/LICENSE).

Coded with 🖤 by Appu
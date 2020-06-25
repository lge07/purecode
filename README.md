# purecode
*another terminal text editor, now extra mediocre*

Purecode is largely a practice for me in writing more advanced Python code, trying to think through the process more. The goals are the following:
- Extensibility
- Simplicity
- Efficiency

Sound like marketing speak? Sure does. Most are fairly ironic given how this is Python, which is clearly known for its legendary efficiency and simplicity. The idea is to have simple code and by extension have it run efficiently.

Extensibility is covered in the next section.

Eventually I'll move to a worthwhile language (e.g. C/C++), but for now, Python will have to do. Javascript isn't an option, since it isn't worthwhile.

I'll have to learn the following:
- Curses programming
- OS-related programming (e.g. pipes, stdin/out control, subprocesses, maybe threads.)
- Text buffering
- Unit testing (inevitably)
- Logging
- Algorithm design, data structure design.

## How it *should* work

The base is based on a series of utilities, within the ``utils`` folder:
- Buffer: Store, load, modify, and save a body of text.
- Search: Search a body of text using regex, and return match counts, beginnings and ends of each match.
- External: Run commands within the terminal, and get their output. Basically a terminal emulator tacked on.

Add-ons require further thought. Likely, it'll have to involve either a loop to influence each utility (if it's an "always on" behaviour), or some sort of external trigger (if it's an "occasional" behaviour.)

Like this: Input -> process -> add-ons -> package and output

Base features:
- Search, search and replace
- File manager built in?
- Unified command prompt that sends commands to both OS and editor.
- Auto-parenthesis completion, explicitly showing how many nested elements there are and so on.
- Current buffer statistics (lines, columns, spaces, etc.)
- Configuration via config file.
- Autocomplete???
- Support for user and included scripts that handle additional functionality
  - Linting
  - Source control
  - Syntax highlighting
  - Selection from the system clipboard, and saving to a temporary clipboard.

It'll likely be possible (although questionably logical) to run purecode without a GUI. 

The GUI Command interface will be within the folder ``gui_utils``. There will be a few simple functions that can be expanded by extensions and the like.
- Bottom bar class with ability to modify the text and a variety of parameters.
- Main text window class with ability to modify text and add appearance

TODO: File system buffer?
Unique strictly rectangular selection?  
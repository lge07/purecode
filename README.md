# purecodewar
*another terminal text editor, now with extra mediocrity*

Purecode is largely a practice for me in writing more advanced Python code, with actual thought put in, even though the results may not be so fantastic. The goals are the following:
- Extensibility
- Simplicity
- Efficiency

These are all rather vague, but code will likely be fairly simple since I don't have the skills, and at least it'll be documented well. The efficiency is hypothetically a product of the simplicity. Extensibility? Well, that'll be covered in the next part.

Eventually I'll move to something that isn't the bloated whale of Python, but that'll be soon (tm). NOT JAVASCRIPT! 

I'll have to learn the following:
- Curses programming
- Anything OS-related
- String Buffers: Why they exist and how to implement them
- UNIT TESTING \o/
- Logging
- More advanced topics
## How it *should* work

Purecode working at all is a stretch of the imagination for sure, but I'll try to explain as clearly as possible what it should do.

The base is based on a series of utilities, within the ``utils`` folder. Here's a list with a mediocre description:

- Search: Search a body of text using regex, and return match counts, beginnings and ends of each match.
- Modify: Modify specific components of a body of text, pretty self-explanatory.
- Delete: Delete specific components of a body of text, probably redundant.
- External: Run commands within the terminal, and get their output.

All of these will do what they need, run output through whatever applicable add-ons there are, and then output a series of final modifications. This is so that redundant changes or changes that can be grouped into one don't slow things down as much. 

Input -> process -> add-ons -> package and output
Combinations of the utilities will be used to do extra things. For example:
- Search and replace: Combine the search and modify/delete utilities
- In-editor terminal: Run AND get output from the terminal
- etc.

Here's a list of some features I'd like to have:
- Search, search and replace
- File manager built in?
- Unified command prompt that sends commands to both the OS and purecode, requires some thonk
- Auto-parenthesis completion, with some sort of unique way of explicitly showing which ones are impacted.
- Current buffer statistics (lines, columns, spaces, etc.)
- Support for user and included scripts that do extra stuff (tm)
  - Linter
  - Source control
  - Syntax highlighting
  - Selection from the system clipboard, and saving to a temporary clipboard.

So really, hypothetically, you could run purecode without the UI. Except that would probably be a big pain, and you wouldn't really want to do that.

The GUI Command interface will be within the folder ``gui_utils``. There will be a few simple functions that can be expanded by extensions and the like.
- Bottom bar class with ability to modify the text and a variety of parameters.
- Main text window class with ability to modify text and add appearance :D

I'll probably add more in as needed, since the feature set will likely balloon but for now that's it!

TODO: File system buffer?
Unique strictly rectangular selection?
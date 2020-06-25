- Finish unit tests for linked list
- Wrap linked lists into buffer class
- Write unit tests for buffer class
- Write search methods for buffer class.
- Write external command system
- Create primary UI elements
- Interface everything together
- Module framework
  - Keywords for use in command system, like with Vivaldi search engine select
    - ``r`` to run in terminal
    - ``c`` to command editor (or nothing at all, directly operates on editor)
    - ``s`` to search
    - etc.

ideas:
- toggle hotkey for going through whatever option is currently selected
- "tab" class that acts as a replacement for a tab within buffer, replaced with any amount of spaces as needed.
- "clips" series of buffers containing random junk to save
- options setup gui (separate program)
- Stock modules
  - Source Control
  - Printing
  - Basic syntax highlighting
  - Auto-Comment Compilation System

How modules are written:
- Keyword: letter to use in order to command that module
- Immediately Run Actions: upon any sort of module interfacing
  - buffer-applied
  - search-applied
  - ui-applied
  - etc.
- Extension methods applied in for loop during buffer


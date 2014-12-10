XYplorer-syntax-for-Sublime-Text
================================

- usage:
   + Copy to \Sublime Text\Data\Packages\XYplorer
   + Open file XYplorer.sublime-settings > edit line "xypath": "E:\\Utilities\\XYplorer"
   + To assign XYplorer icon to .xys files in sidebar:
      (1) Create an XYplorer icon in png format and save to \\Data\\Packages\\Theme - Default\\icons\\file_type_xys.png
      (2) The filename must be file_type_xys.png because it's defined in "Icon (xys).tmPreferences"
- Contextual help:
   + Place cursor on any function such as "replacelist()" > Ctrl+enter will open the corresponding reference in XYplorer help file
   + Place cursor on any CommandID such as "#101" > Ctrl+enter will display corresponding command text in statusbar
- Snippet: see tabTrigger in the *.sublime-snippet files. Typing these triggers and press Tab will insert a pre-defined script

XYplorer syntax for Sublime Text
================================

Installation:
---
- Copy to \Sublime Text\Data\Packages\XYplorer
- Edit file path in XYplorer.sublime-settings and XYplorer.sublime-build
- This package applies to .xys, .inc, .xyi files

Contextual help:
---
- Place cursor on any xy-native function such as "replacelist()" > Ctrl+enter will open the corresponding reference in XYplorer help file
- Place cursor on any user-defined function such as "gpc()" > Ctrl+enter (or Goto > Go to definition) will jump to function definition 
	+ This open included file if necessary. 
	+ Require files, which contain the function, to be indexed: 
		+ setting "index_files": true,
		+ files, which contain the function, are in a project (Project > Add folder to project => files appear in sidebar)
+ Place cursor on any CommandID such as "#101" > Ctrl+enter will display corresponding command text in statusbar

Snippet:
--- 
see tabTrigger in the *.sublime-snippet files: Typing these triggers and press Tab will insert a pre-defined script template. Example:
  
+ heredoc
+ nowdoc
+ nowdocalternative
+ feselitems: For each <selitems\>
+ foreach: For each $items\
+ function: Insert User defined function

Build:
---
+ Tool > Build (Ctrl+B) will execute current xys file in XYplorer

Assign XYplorer icon to .xys files in sidebar:
---
+ Create an XYplorer icon in png format and save to \Data\Packages\Theme - Default\icons\file_type_xys.png
+ Filename must be file_type_xys.png because it's defined in "Icon (xys).tmPreferences"

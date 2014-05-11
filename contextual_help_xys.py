import sublime, sublime_plugin, subprocess

class contextual_help_xys(sublime_plugin.TextCommand):
	def run(self, edit):
		xypath = self.view.settings().get('xypath')
		CursorLocation = self.view.sel()[0]
		ScopeName = self.view.scope_name(CursorLocation.a)
		ScopeText = self.view.substr(self.view.extract_scope(CursorLocation.a))
		if "entity.name.function" in ScopeName:
			ScopeText = ScopeText.replace("#", "_")
			arg = xypath + "\\XYplorer.chm::/idh_scripting_comref.htm#idh_sc_" + ScopeText
			subprocess.Popen(["hh.exe", arg])
		elif "variable.parameter" in ScopeName:
			subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_variables.htm"])
		elif "keyword.control" in ScopeName:
			ScopeTextLower = ScopeText.lower()
			if ScopeTextLower == "if" or ScopeTextLower == "elseif" or ScopeTextLower == "else":
				subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_scripting.htm#idh_scripting_ifthen"])
			elif ScopeTextLower == "while":
				subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_scripting.htm#idh_scripting_whileloops"])
			elif ScopeTextLower == "foreach":
				subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_scripting.htm#idh_scripting_foreachloops"])
			else:
				subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_scripting.htm"])
		else:
			window.run_command("move_to", {"to": "hardeol"})        # Add new line
			window.run_command("insert", {"characters": "\n"})      # Add new line
# ::/idh_scripting_comref.htm#idh_sc_folderreport
# mk:@MSITStore:E:\7Utilities\XYplorer\XYplorer.chm::/idh_scripting_comref.htm#idh_sc_getpathcomponent

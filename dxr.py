import sublime
import sublime_plugin
import webbrowser
from os import path

DXR_URL = "https://dxr.mozilla.org/mozilla-central/source"

class OpenInDxrCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		def find_sourcedir(file_name):
			directory = path.dirname(file_name)
			if directory == file_name:
				return None

			mach_path = path.join(directory, 'mach')
			if path.exists(mach_path):
				return directory

			return find_sourcedir(directory)

		# self.view.insert(edit, 0, "DXR!")
		file_name = self.view.file_name()
		source_dir = find_sourcedir(file_name)
		if not source_dir:
			return

		relative_name = self.view.file_name()[len(source_dir):]
		line_number = self.view.rowcol(self.view.sel()[0].begin())[0] + 1

		url = "%s%s#%d" % (DXR_URL, relative_name, line_number)
		webbrowser.open_new_tab(url)
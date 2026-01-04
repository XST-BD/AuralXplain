import os
import requests

from textual.app import App, ComposeResult, on
from textual.widgets import Button, Input, TextArea

from frontend.ui.ui import MainUI


class AuralXplain(App):
	CSS_PATH = "styles/styles.tcss"

	@staticmethod
	def compose() -> ComposeResult:
		yield MainUI()

	@on(Button.Pressed, "#submit_btn")
	def on_submit(self):
		file_path = self.query_one("#file", Input).value.strip()

		if not os.path.isfile(file_path):
			self.notify("File does not exist!", title="Error", severity="error")
			return

		self.notify(f"Audio path: {file_path}", title="Info", severity="info")

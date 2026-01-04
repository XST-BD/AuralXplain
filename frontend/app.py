import os

from textual.app import App, ComposeResult, on
from textual.widgets import Button, Input, TextArea

from frontend.ui.ui import MainUI
from backend.core import audio_to_text_summ


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
		self.query_one("#loader_container").styles.display = "block"
		self.query_one("#summary_container").styles.display = "none"

		if audio_to_text_summ(file_path):
			summary = audio_to_text_summ(file_path)
			self.query_one("#summary", TextArea).value = summary
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "block"
			self.notify("Summary generated successfully!", title="Success", severity="success")
		else:
			self.notify("Failed to generate summary.", title="Error", severity="error")
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "none"

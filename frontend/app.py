import os

from textual.app import App, ComposeResult, on
from textual.widgets import Button, Input, TextArea
from textual import work

from frontend.ui.ui import MainUI
from backend.core import audio_to_text_summ


class AuralXplain(App):
	CSS_PATH = "styles/styles.tcss"

	@staticmethod
	def compose() -> ComposeResult:
		yield MainUI()

	@work(thread=True)
	def process_audio(self, file_path: str):
		return audio_to_text_summ(file_path)

	@on(Button.Pressed, "#submit_btn")
	async def on_submit(self):
		self.query_one("#summary_container").styles.display = "none"
		self.query_one("#loader_container").styles.display = "block"

		file_path = self.query_one("#file", Input).value.strip()

		if not file_path:
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "none"
			self.notify("Please enter an audio file path.", severity="warning")
			return

		if not os.path.isfile(file_path):
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "none"
			self.notify("File does not exist!", title="Error", severity="error")
			return

		worker = self.process_audio(file_path)
		summary = await worker.wait()

		if summary:
			self.query_one("#summary", TextArea).value = summary
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "block"
			self.notify("Summary generated successfully!", title="Success")
		else:
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "none"
			self.notify("Failed to generate summary.", title="Error", severity="error")

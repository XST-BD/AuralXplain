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

	def on_mount(self) -> None:
		self.query_one("#summary_container").border_title = "Generated Summary"

	@work(thread=True)
	def process_audio(self, file_path: str):
		return audio_to_text_summ(file_path)

	@on(Button.Pressed, "#submit_btn")
	async def on_submit(self):
		self.query_one("#summary_container").styles.display = "none"
		self.query_one("#summary", TextArea).text = ""
		self.query_one("#loader_container").styles.display = "block"

		file_path = self.query_one("#file", Input).value.strip()

		if not file_path:
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "none"
			self.notify("Please enter an audio file path.", title="Empty input field", severity="warning")
			return

		if not os.path.isfile(file_path):
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "none"
			self.notify("File does not exist!", title="Error", severity="error")
			return

		self.notify("Processing audio...", severity="info")

		worker = self.process_audio(file_path)
		summary = await worker.wait()

		if len(summary.strip()) > 0:
			self.query_one("#summary", TextArea).text = summary.strip()
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "block"
			self.notify("Summary generated successfully!", title="Success")
		else:
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "none"
			self.notify("Failed to generate summary.", title="Error", severity="error")

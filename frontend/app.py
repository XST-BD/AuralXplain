import os

from textual.app import App, ComposeResult, on
from textual.containers import Container
from textual.widgets import Button, Input, TextArea
from textual import work

from frontend.ui.ui import MainUI
from backend.core import media_to_text_summ, download_summ


class MediaXplain(App):
	CSS_PATH = "styles/styles.tcss"

	@staticmethod
	def compose() -> ComposeResult:
		yield MainUI()

	def on_mount(self) -> None:
		self.query_one("#summary_box", Container).border_title = "Generated Summary"
		self.query_one("#save_file", Input).border_title = "File Path to Save Summary"

	@on(Input.Changed, "#media_file")
	def on_media_file_change(self) -> None:
		self.query_one("#summary_container").styles.display = "none"
		self.query_one("#summary", TextArea).text = ""
		self.query_one("#save_file", Input).value = ""

	@work(thread=True)
	def process_media(self, file_path: str) -> str:
		return media_to_text_summ(file_path)

	@on(Button.Pressed, "#submit_btn")
	async def on_submit(self):
		self.query_one("#summary_container").styles.display = "none"
		self.query_one("#summary", TextArea).text = ""
		self.query_one("#save_file", Input).value = ""
		self.query_one("#loader_container").styles.display = "block"

		file_path = self.query_one("#media_file", Input).value.strip()

		if not file_path:
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "none"
			self.notify("Please enter an audio or video file path.", title="Empty Audio/Video File Path!", severity="warning", timeout=1.5)
			return

		if not os.path.isfile(file_path):
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "none"
			self.notify("File does not exist.", title="Error!", severity="error", timeout=1.5)
			return

		self.notify("Processing media file...", severity="warning", timeout=1.5)

		worker = self.process_media(file_path)
		summary = await worker.wait()

		if summary.strip():
			self.query_one("#summary", TextArea).text = summary.strip()
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "block"
			self.notify("Summary generated successfully.", title="Generated!", timeout=1.5)
		else:
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "none"
			self.notify("Failed to generate summary.", title="Error!", severity="error", timeout=1.5)

	@on(Button.Pressed, "#copy_btn")
	def on_copy(self) -> None:
		summary = self.query_one("#summary", TextArea).text.strip()

		if summary:
			self.copy_to_clipboard(summary)
			self.notify("Successfully copied to clipboard.", title="Copied!", timeout=1.5)
		else:
			self.notify("Nothing to copy.", title="No Summary!", severity="warning", timeout=1.5)

	@on(Button.Pressed, "#save_btn")
	def on_save(self) -> None:
		summary = self.query_one("#summary", TextArea).text.strip()
		save_path = self.query_one("#save_file", Input).value.strip()

		if not summary:
			self.notify("No summary to save.", title="No Summary!", severity="warning", timeout=1.5)
			return

		if not save_path:
			self.notify("Please provide a file path to save the summary.", title="No File Path to Save!", severity="warning", timeout=1.5)
			return

		ext = os.path.splitext(save_path)[1].lower()
		supported_extensions = {".txt"}

		if ext not in supported_extensions:
			self.notify(f"Unsupported file type {ext}!\n\nSupported file format is .txt", title="Error!", severity="error", timeout=1.5)
			return

		try:
			download_summ(summary, save_path)
			self.notify(f"Summary saved successfully at:\n{save_path}", title="Saved!", timeout=1.5)
		except Exception as e:
			self.notify(f"Failed to save summary.\n{e}", title="Error!", severity="error", timeout=1.5)

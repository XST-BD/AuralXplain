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
			self.notify("Please enter an audio or video file path.", title="Empty Audio/Video File Path!", severity="warning")
			return

		if not os.path.isfile(file_path):
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "none"
			self.notify("File does not exist.", title="Error!", severity="error")
			return

		self.notify("Processing media file...", severity="info")

		worker = self.process_media(file_path)
		summary = await worker.wait()

		if len(summary.strip()) > 0:
			self.query_one("#summary", TextArea).text = summary.strip()
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "block"
			self.notify("Summary generated successfully.", title="Generated!")
		else:
			self.query_one("#loader_container").styles.display = "none"
			self.query_one("#summary_container").styles.display = "none"
			self.notify("Failed to generate summary.", title="Error!", severity="error")

	@on(Button.Pressed, "#copy_btn")
	def on_copy(self) -> None:
		summary = self.query_one("#summary", TextArea).text.strip()

		if summary.strip():
			self.copy_to_clipboard(summary)
			self.notify("Successfully copied to clipboard.", title="Copied!")
		else:
			self.notify("Nothing to copy.", title="No Summary!", severity="warning")

	@on(Button.Pressed, "#save_btn")
	def on_save(self) -> None:
		summary = self.query_one("#summary", TextArea).text.strip()
		save_path = self.query_one("#save_file", Input).value.strip()

		if not summary:
			self.notify("No summary to save.", title="No Summary!", severity="warning")
			return

		if not save_path:
			self.notify("Please provide a file path to save the summary.", title="No File Path to Save!", severity="warning")
			return

		ext = os.path.splitext(save_path)[1].lower()
		supported_extensions = {".txt"}

		if ext not in supported_extensions:
			self.notify(f"Unsupported file type {ext}!\n\nSupported file formate is .txt", title="Error!", severity="error")
			return

		try:
			download_summ(summary, save_path)
			self.notify(f"Summary saved successfully at:\n{save_path}", title="Saved!")
		except Exception as e:
			self.notify(f"Failed to save summary.\n{e}", title="Error!", severity="error")

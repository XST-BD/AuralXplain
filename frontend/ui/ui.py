from textual.containers import VerticalScroll, Horizontal, Container
from textual.widgets import Header, Footer, Label, Input, TextArea, Button
from textual.app import App, ComposeResult

from frontend.ui.components.loader import SpinnerWidget


class MainUI(VerticalScroll):
	@staticmethod
	def compose():
		yield Header(show_clock=True)
		yield Footer()

		with Container(id="main_container"):
			with Container():
				yield Label("Audio/Video File Path:", id="file_label", shrink=True)
				yield Input(id="media_file", placeholder="Enter the absolute path of an audio or video file...")

			with Container(id="button_container"):
				yield Button("Generate", id="submit_btn")

			with Container(id="loader_container"):
				yield SpinnerWidget("#7F00FF")

			with Container(id="summary_container"):
				with Container(id="summary_box"):
					yield TextArea(id="summary", placeholder="No summary...", read_only=True, disabled=True)

				with Container():
					yield Button("Copy to Clipboard", id="copy_btn")

				with Horizontal():
					yield Input(id="save_file", placeholder="Enter the absolute path to save summary (e.g., \"C:/Downloads/summary.txt\")...")
					yield Button("Save Summary", id="save_btn")

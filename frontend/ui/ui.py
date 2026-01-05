from textual.containers import VerticalScroll, Container
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
				yield Label("Audio File Path:", id="file_label", shrink=True)
				yield Input(id="file", placeholder="Enter the absolute file path of the audio here...")

			with Container(id="button_container"):
				yield Button("Generate", id="submit_btn", variant="primary")

			with Container(id="loader_container"):
				yield SpinnerWidget("#7F00FF")

			with Container(id="summary_container"):
				yield TextArea(id="summary", placeholder="No summary...", disabled=True)

from textual.containers import VerticalScroll, Container
from textual.widgets import Header, Footer, Label, Input, TextArea, Button


class MainUI(VerticalScroll):
	@staticmethod
	def compose():
		yield Header(show_clock=True)
		yield Footer()

		with Container():
			yield Label("Audio File Path:", shrink=True)
			yield Input(id="file", placeholder="Enter the absolute file of the audio here...")

		with Container(id="button_container"):
			yield Button("Generate", id="submit_btn", variant="primary")

		with Container():
			yield Label("Generated Summary:", shrink=True)
			yield TextArea(id="summary", placeholder="The generated summary will appear here...", disabled=True)

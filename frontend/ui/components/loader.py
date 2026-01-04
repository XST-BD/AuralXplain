from textual.widgets import Static
from rich.spinner import Spinner


class SpinnerWidget(Static):
	DEFAULT_CSS = """
    SpinnerWidget {
        content-align: center middle;
    }
    """

	def __init__(self, color_hex: str = "#7F00FF"):
		super().__init__()
		self.spinner = Spinner("aesthetic", style=f"bold {color_hex}")
		self.interval_update = None

	def on_mount(self) -> None:
		self.interval_update = self.set_interval(1 / 60, self.update_spinner)

	def update_spinner(self) -> None:
		self.update(self.spinner)

	def pause(self) -> None:
		if self.interval_update:
			self.interval_update.pause()

	def resume(self) -> None:
		if self.interval_update:
			self.interval_update.resume()

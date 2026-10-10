from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import QPointF, QProcess, QMargins
from PySide6.QtWidgets import QGraphicsSimpleTextItem
from .timings import load_timings
import sys

class ChartWindow(QWidget):
    def __init__(self, timings):
        super().__init__()
        self.setWindowTitle("Build Timings Diagram")
        self.setMinimumSize(600, 400)

        layout = QVBoxLayout(self)

        self.timings = timings
        self.chart = QChart()
        self.series = QLineSeries()

        for index, entry in enumerate(timings):
            self.series.append(index, entry["duration"])

        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Build Step Timings")

        self.chart_view = QChartView(self.chart)
        layout.addWidget(self.chart_view)

        self.chart_view.setRubberBand(QChartView.RectangleRubberBand)

        self.chart_view.setInteractive(True)

        self.tooltip_item = QGraphicsSimpleTextItem()
        self.chart_view.scene().addItem(self.tooltip_item)
        self.tooltip_item.hide()

        self.series.hovered.connect(self.on_hover)

    def on_hover(self, point: QPointF, state: bool):
        if not state:
            self.tooltip_item.hide()
            return

        idx = int(point.x())
        title = self.timings[idx]["title"]
        self.tooltip_item.setText(title)

        pixel_pos = self.chart.mapToPosition(point, self.series)

        offset_x = 12
        offset_y = -24

        self.tooltip_item.setPos(pixel_pos.x() + offset_x, pixel_pos.y() + offset_y)
        self.tooltip_item.show()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Qt6 Builder Frontend")
        self.setMinimumSize(300, 120)

        layout = QVBoxLayout(self)

        self.button = QPushButton("Run")
        self.button.clicked.connect(self.on_run_clicked)
        layout.addWidget(self.button)

        self.process = QProcess(self)

    def on_run_clicked(self):
        self.button.setEnabled(False)
        self.button.setText("Running…")

        self.process.finished.connect(self.on_finished)
        self.process.start("python3", ["build.py", "--quiet", "--output-job-time-as-json"])

    def on_finished(self):
        self.button.setEnabled(True)
        self.button.setText("Run")

        timings = load_timings()
        if timings:
            chart_window = ChartWindow(timings)
            chart_window.show()

            # Keep reference alive
            self.chart_window = chart_window

def gui_main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()

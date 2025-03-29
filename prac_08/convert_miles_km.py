from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934
DEFAULT_VALUE = 0


class MilesConverterApp(App):
    """Kivy App for converting miles to kilometres"""
    message = StringProperty()

    def build(self):
        """Build the Kivy app from kivy file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.message = "67.592"
        return self.root

    def handle_calculate(self):
        """Handler for pressing convert button"""
        value = self.validate_miles_input()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Handler for pressing up or down button"""
        value = self.validate_miles_input() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def validate_miles_input(self):
        """Validate miles input and convert it to float"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return DEFAULT_VALUE


MilesConverterApp().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """App to display a list of names as labels dynamically."""

    def __init__(self, **kwargs):
        """Initialize a list of names"""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "David", "Eve"]

    def build(self):
        """Load the UI and create labels dynamically."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Dynamically add labels for each name in the list."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)

DynamicLabelsApp().run()

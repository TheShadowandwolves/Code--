from datetime import datetime
class Debug:
    def __init__(self):
        self.date = datetime.now()
        self.file = open(f"DEBUG/debug.txt-{self.date.strftime('%Y%H%M%S')}", "a")

    def now(self):
        self.file.write(f"DEBUG STARTED AT {self.date.strftime('%Y:%H:%M:%S')}\n")

    def end(self):
        self.file.write(f"DEBUG ENDED AT {datetime.now().strftime('%Y:%H:%M:%S')}\n")
        self.file.close()

    def df(self, reason, text):
        self.file.write(f"DEBUG {reason} AT {datetime.now().strftime('%Y:%H:%M:%S')}: {text}\n")
        return text


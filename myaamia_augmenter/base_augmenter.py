class BaseAugmenter:
    def __init__(self, text):
        self.text = text

    def getOriginalText(self):
        return self.text

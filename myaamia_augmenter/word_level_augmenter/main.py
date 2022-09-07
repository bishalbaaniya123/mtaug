from myaamia_augmenter.base_augmenter import BaseAugmenter


class WordAugmenter(BaseAugmenter):
    def __init__(self, text):
        super().__init__(text)

    def augment_word(self):
        return f'Word-Augmented text - {self.getOriginalText()}'

from myaamia_augmenter.base_augmenter import BaseAugmenter


class SentenceAugmenter(BaseAugmenter):
    def __init__(self, text):
        super().__init__(text)

    def augment_word(self):
        return f'Sentence-Augmented text - {self.getOriginalText()}'

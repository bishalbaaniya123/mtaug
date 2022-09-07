from myaamia_augmenter.word_level_augmenter.main import WordAugmenter


class WordAugmentPlayground(WordAugmenter):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def get_augmentation(self):
        return self.augment_word()


dummy_text = 'The lazy brown fox jumped over a bridge'
wordAugmenter = WordAugmentPlayground(dummy_text)
print(wordAugmenter.get_augmentation())

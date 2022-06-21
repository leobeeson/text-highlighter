from gensim.models.phrases import Phrases
from gensim.models.phrases import FrozenPhrases
from gensim.models.phrases import ENGLISH_CONNECTOR_WORDS

class PhraseExtractor:
    corpus: list[list[str]]
    updatable_model: Phrases
    frozen_model: FrozenPhrases

    def __init__(self, corpus) -> None:
        self.corpus = corpus
        self.updatable_model = self.run_model_iteration()
        self.frozen_model = self.freeze_model()


    def run_model_iteration(self) -> Phrases:
        phrases_model = Phrases(
            sentences = self.corpus,
            min_count = 10,
            threshold = 0,
            scoring = "npmi",
            connector_words = ENGLISH_CONNECTOR_WORDS)
        return phrases_model
    

    def freeze_model(self) -> FrozenPhrases:
        frozen_model = self.updatable_model.freeze()
        return frozen_model

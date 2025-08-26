import pytest


class LexerTest:
    @pytest.fixture(autouse=True)
    def set_context(self, context):
        self.context = context

    def test_check_tokenize(self):
        content = self.content
        tokenized = self.context.library.tokenize(content)
        self.tokenized = [token.type for token in tokenized]
        correct = self.correct.strip().split()
        assert self.tokenized == correct
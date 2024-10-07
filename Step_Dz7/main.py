class ExampleIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
    # Повертаємо генератор
        return self._generator()

    def _generator(self):
        for item in self.data:
            yield item
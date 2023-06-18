class Person:
    def __init__(self, name, identifier) -> None:
        self.name = name
        self.identifier = identifier

    def __str__(self):
        return f'nome: {self.name}'

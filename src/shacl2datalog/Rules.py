class Rules:
    """Container to hold a series of rules"""

    class Rule:
        """Representation of a Datalog rule."""
        def __init__(self, head: str, body: [str]):
            self.head = head
            self.body = body

        def __str__(self) -> str:
            return "(<- " + self.head + "\n".join(self.body) + ")"

        def __repr__(self) -> str:
            return "Rule(" + self.head + str(self.body) + ")"

    def __init__(self, rules: [Rule] = None):
        self._rules: [Rule] = rules

    def write(self, path: str) -> None:
        with open(path, 'w') as file:
            for rule in self._rules:
                file.write(str(rule))

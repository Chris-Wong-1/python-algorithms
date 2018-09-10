class Stack:
    """
    Illustrate class-level docstring.

    Classes use a special whitespace convention: the opening and closing quotes
    are preceded and followed by a blank line, respectively. No other
    docstrings should be preceded or followed by anything but code.
    A blank line at the end of a multi-line docstring before the closing
    quotation marks simply makes it easier for tooling to auto-format
    paragraphs (wrapping them at 79 characters, per PEP8), without the closing
    quotation marks interfering. While it's not required, the
    presence of a blank line is quite common and much appreciated. Regardless,
    the closing quotation marks should certainly be on a line by themselves.

    """

    def __init__(self):
        """Illustrate method-level docstring.

        All public callables should have docstrings, including magic methods
        like ``__init__()``.

        You'll notice that all these docstrings are wrapped in triple double
        quotes, as opposed to just "double quotes", 'single quotes', or
        '''triple single quotes.''' This is a convention for consistency and
        readability. However, there are two edge cases worth knowing about
        which I'll illustrate in just a moment.

        """
        self.items = []

    def isEmpty(self):
        """Illustrate one line docstring, including the quotation marks."""
        return len(self.items) == 0

    def push(self, item):
        """Illustrate one line docstring, including the quotation marks."""
        self.items.append(item)

    def pop(self):
        """Illustrate one line docstring, including the quotation marks."""
        return self.items.pop()

    def peek(self):
        """Illustrate one line docstring, including the quotation marks."""
        return self.items[len(self.items) - 1]

    def size(self):
        """Illustrate one line docstring, including the quotation marks."""
        return len(self.items)


s = Stack()

print(s.isEmpty())
s.push("A")
s.push("B")
print(s.peek())
s.push("C")
print(s.size())
print(s.pop())
print(s.size())

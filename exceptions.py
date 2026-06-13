class NoValidOffsetError(Exception):
    """Raised when no rafter offset satisfies mounting constraints."""
    pass


class InvalidInputError(Exception):
    """Raised when input data has invalid structure or types."""
    pass
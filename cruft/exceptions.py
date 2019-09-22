"""Contains all custom exceptions raised by cruft"""


class CruftError(Exception):
    """The base exception for any error originating from the cruft project"""


class UnableToFindCookiecutterTemplate(CruftError):
    """Raised when Cruft is unable to find a cookiecutter template"""

    def __init__(self, directory):
        super().__init__(self, f"Was unable to locate a Cookiecutter template in `{directory}` !")
        self.directory = directory

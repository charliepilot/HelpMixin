import inspect
from typing import Dict, Tuple, List


class HelpMixin:
    """
    A MixIn that returns class comments as help text.

    To return the comments, call get_help_class_text.  This is a class method:
        MyClass.get_help_class_text() is valid.

    The comments can contain string formatting curly brackets {}.
        For example:  Hello, {class_name}
        To add additional variables, override get_help_test_custom_format method
        NOTE: If an IndexError or KeyError occurs while formatting the string,
            the Comments are returned as is.  So if the format is not working,
            validate all positional values and keys are specified.  As the error
            is trapped and not raised.  Don't want "help" to cause an
            application to fail.
    """

    # If class has no comments, this message is used.
    # Override for custom default message.
    HELP_DEFAULT_MESSAGE = "Help is not available for {class_name}."

    @classmethod
    def get_help_text_custom_format(cls) -> Tuple[List[str], Dict[str, str]]:
        """
        Used to create a custom list and dict to be used as arguments to
            str.format(*args, **kwargs) of the comments.
        This list and dict will be merged with the build in mappings.
            So no need to add "class_name".

        :return: Returns a tuple of a custom list and dict.
        """
        return [], {}

    @classmethod
    def _get_help_text_format(cls) -> Tuple[List[str], Dict[str, str]]:
        """
        Combines custom formats from cls.get_help_text_custom_format and the
            default formats to be used as arguments to
            str.format(*args, **kwargs) of the comments.

        For custom mappings, it is best practice to override
            get_help_text_custom_format instead of this method.

        :return: Returns a tuple (list, dict) for str.format(*args, **kwargs)
        """
        format_positional = []
        format_mappings = {
            "class_name": cls.__name__,
        }
        custom_positional, custom_mappings = cls.get_help_text_custom_format()
        format_mappings.update(custom_mappings)

        return format_positional + custom_positional, format_mappings

    @classmethod
    def _help_format_text(cls, comments: str) -> str:
        # TODO: Add comments
        try:
            positional, mappings = cls._get_help_text_format()
            formatted_comments = comments.format(*positional, **mappings)
        except (IndexError, KeyError):
            formatted_comments = comments

        return formatted_comments

    @classmethod
    def get_help_class_text(cls) -> str:
        # TODO: Add comments
        comments = inspect.cleandoc(cls.__doc__ or cls.HELP_DEFAULT_MESSAGE)

        return cls._help_format_text(comments)

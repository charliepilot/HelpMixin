import inspect
import os
from typing import Optional


class HelpMixin:
    """
    A MixIn that provides help text by returning an object's comments.

    By default, the class object itself is used for providing help.

    To retrieve the comments as help text, call .help() or .short_help().
    These are class methods, so you can use MyClass.help() to access them.

    Comments containing {class_name} will be replaced with the current
        class name.
    Comments containing {object_name} will be replaced with the name of the
        object, provided the help_obj argument is passed to
        .help() or .short_help(), otherwise, it will be replaced with the
        class name.
    """

    # If the object has no comments, this message is used.
    # Override for custom default message.
    HELP_DEFAULT_MESSAGE: str = "Help is not available for {object_name}."

    @classmethod
    def _help_format(cls,
                     text: str,
                     help_obj: Optional[object] = None) -> str:
        """
        Replaces {class_name} with the current class name, and
        replaces {object_name} with the help_obj's name, if it
        is specified, otherwise, it will be replaced with the class name.

        :param text: The input text that may contain
                     {class_name} and {object_name}.
        :param help_obj: Optional object whose name is used to replace
                        {object_name}.
        :return: The text with {class_name} and {object_name} replaced.
        """

        # Note:  .format() is not used, because super class may have additional
        #        fields which would cause IndexError or KeyError.
        text = text.replace("{class_name}", cls.__name__)
        obj = help_obj or cls
        text = text.replace("{object_name}", obj.__name__)

        return text

    @classmethod
    def help(cls, help_obj: Optional[object] = None) -> str:
        """
        Retrieve the comments from the help_obj, update the {class_name} and
        {object_names}, and return them as help message.

        :param help_obj: Optional object to pull comments from; the default is
                         the current class.
        :return: str: Comments from help_obj with {class_name} and
                 {object_name} replaced.  If the help_obj has no comments, then
                 HELP_DEFAULT_MESSAGE is used.
        """
        obj = help_obj or cls
        comments = inspect.cleandoc(
            obj.__doc__ or cls.HELP_DEFAULT_MESSAGE
        )
        f_comments = cls._help_format(comments, help_obj=help_obj)

        return f_comments

    @classmethod
    def short_help(cls,
                   help_obj: Optional[object] = None,
                   help_lines: Optional[int] = None) -> str:
        """
        Return the first lines of .help() as specified by help_lines.

        :param help_obj: See .help().
        :param help_lines: The number of lines to return from .help();
                           the default is 1 line.
        :return: The first lines of .help() as specified by help_lines.
        """
        lines = help_lines or 1
        message = cls.help(help_obj=help_obj)
        return os.linesep.join(message.splitlines()[:lines])

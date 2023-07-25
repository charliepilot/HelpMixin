import unittest
from typing import Dict, Tuple, List

from pyhelpmixin.help_mixin import HelpMixin


class HelpMixinTestCustomDefaultMsg(HelpMixin):
    HELP_DEFAULT_MESSAGE = "Hello {class_name}"


class HelpMixinTestCustomFormat(HelpMixin):
    """
    Hello, {name}.  My name is {class_name}. {}
    """

    @classmethod
    def get_help_text_custom_format(cls) -> Tuple[List[str], Dict[str, str]]:
        return ["Best regards"], {"name": "world", "test": "this"}


class TestHelpMixin(unittest.TestCase):

    # ----- HELP_DEFAULT_MESSAGE
    def test_help_default_message(self):
        self.assertEqual(
            HelpMixin.HELP_DEFAULT_MESSAGE,
            "Help is not available for {class_name}."
        )

    def test_help_default_message_custom(self):
        self.assertEqual(
            HelpMixinTestCustomDefaultMsg.HELP_DEFAULT_MESSAGE,
            "Hello {class_name}"
        )

    # ----- get_help_text_custom_format
    def test_get_help_text_custom_format(self):
        self.assertEqual(
            HelpMixin.get_help_text_custom_format(),
            ([], {})
        )

    def test_get_help_test_custom_format_override(self):
        self.assertEqual(
            HelpMixinTestCustomFormat.get_help_text_custom_format(),
            (["Best regards"], {"name": "world", "test": "this"})
        )

    # ----- _get_help_text_format
    def test_get_help_text_format(self):
        self.assertEqual(
            HelpMixin._get_help_text_format(),
            ([], {"class_name": "HelpMixin"})
        )

    def test_get_help_text_format_custom_format(self):
        self.assertEqual(
            HelpMixinTestCustomFormat._get_help_text_format(),
            (
                ["Best regards"],
                {
                    "class_name": "HelpMixinTestCustomFormat",
                    "name": "world",
                    "test": "this"
                }
            )
        )

    # ----- _help_format_text
    def test_help_format_text(self):
        self.assertEqual(
            HelpMixin._help_format_text("Hello, {class_name}"),
            "Hello, HelpMixin"
        )

    def test_help_format_index_error(self):
        self.assertEqual(
            HelpMixin._help_format_text("Hello {}"),
            "Hello {}"
        )

    def test_help_format_key_error(self):
        self.assertEqual(
            HelpMixin._help_format_text("Hello {world}"),
            "Hello {world}"
        )

    # ----- get_help_class_text
    def test_get_help_class_text_custom_format(self):
        self.assertEqual(
            HelpMixinTestCustomFormat.get_help_class_text(),
            "Hello, world.  My name is HelpMixinTestCustomFormat. Best regards"
        )

    def test_get_help_class_text_custom_default_msg(self):
        self.assertEqual(
            HelpMixinTestCustomDefaultMsg.get_help_class_text(),
            "Hello HelpMixinTestCustomDefaultMsg"
        )

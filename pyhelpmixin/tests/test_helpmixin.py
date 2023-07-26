import os
import unittest

from pyhelpmixin.help_mixin import HelpMixin


class HelpMixinTestCustomDefaultMsg(HelpMixin):
    HELP_DEFAULT_MESSAGE = "Hello {class_name}"


class HelpMixinTestMethod(HelpMixin):
    """
    Hello {}, My name is {class_name}
    """

    def my_test(self):
        """
        Method help message, {} {class_name}.{object_name}
        """


class HelpMixinTestMultiLine(HelpMixin):
    """
    This is line 1
    This is line 2
    This is line 3
    """

    def my_test(self):
        """
        Method line 1
        Method line 2
        Method line 3
        """
        pass


class TestHelpMixin(unittest.TestCase):

    # ----- HELP_DEFAULT_MESSAGE
    def test_help_default_message(self):
        self.assertEqual(
            HelpMixin.HELP_DEFAULT_MESSAGE,
            "Help is not available for {object_name}."
        )

    def test_help_default_message_custom(self):
        self.assertEqual(
            HelpMixinTestCustomDefaultMsg.HELP_DEFAULT_MESSAGE,
            "Hello {class_name}"
        )

    # ----- _help_format
    def test_help_format_class_name(self):
        self.assertEqual(
            HelpMixinTestMethod._help_format(
                "{h}{}{class_name}.{object_name}"
            ),
            "{h}{}HelpMixinTestMethod.HelpMixinTestMethod"
        )

    def test_help_format_object_name(self):
        self.assertEqual(
            HelpMixinTestMethod._help_format(
                "{h}{}{class_name}.{object_name}",
                help_obj=HelpMixinTestMethod.my_test
            ),
            "{h}{}HelpMixinTestMethod.my_test"
        )

    def test_help_format_lambda(self):
        self.assertEqual(
            HelpMixinTestMethod._help_format(
                "{h}{}{class_name}.{object_name}",
                help_obj=lambda: None
            ),
            "{h}{}HelpMixinTestMethod.<lambda>"
        )

    # ----- get_help
    def test_get_help(self):
        self.assertEqual(
            HelpMixinTestMethod.help(),
            "Hello {}, My name is HelpMixinTestMethod"
        )

    def test_get_help_default_message(self):
        self.assertEqual(
            HelpMixinTestCustomDefaultMsg.help(),
            "Hello HelpMixinTestCustomDefaultMsg"
        )

    def test_get_help_method_message(self):
        self.assertEqual(
            HelpMixinTestMethod.help(
                HelpMixinTestMethod.my_test
            ),
            "Method help message, {} HelpMixinTestMethod.my_test"
        )

    # ----- short_help
    def test_short_help(self):
        self.assertEqual(
            HelpMixinTestMultiLine.short_help(),
            "This is line 1"
        )

    def test_short_help_2_lines(self):
        self.assertEqual(
            HelpMixinTestMultiLine.short_help(help_lines=2),
            f"This is line 1{os.linesep}This is line 2"
        )

    def test_short_help_method(self):
        self.assertEqual(
            HelpMixinTestMultiLine.short_help(
                help_obj=HelpMixinTestMultiLine.my_test
            ),
            "Method line 1"
        )

    def test_short_help_method_2_lines(self):
        self.assertEqual(
            HelpMixinTestMultiLine.short_help(
                help_obj=HelpMixinTestMultiLine.my_test,
                help_lines=2
            ),
            f"Method line 1{os.linesep}Method line 2"
        )

    def test_short_help_help_lines_longer(self):
        self.assertEqual(
            HelpMixinTestMultiLine.short_help(
                help_obj=HelpMixinTestMultiLine.my_test,
                help_lines=100
            ),
            f"Method line 1{os.linesep}Method line 2{os.linesep}Method line 3"
        )

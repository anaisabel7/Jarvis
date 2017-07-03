import unittest
from mock import patch
from Jarvis import Jarvis
from CmdInterpreter import CmdInterpreter
from packages import un


class UnTest(unittest.TestCase):

    def setUp(self):
        self.CI_instance = CmdInterpreter('', '')

    @patch.object(Jarvis, 'default')
    def test_un_is_dict_cmd(self, mock_default):
        # Error message is printed if the cmd is only 'un' (without further words)
        J_instance = Jarvis()
        J_instance.precmd('un children')
        self.assertFalse(mock_default.called)
        J_instance.precmd('un')
        mock_default.assert_called()

    @patch.object(un, 'main')
    def test_main_un_runs(self, mock_un):
        self.CI_instance.do_un('children')
        mock_un.assert_called_with(self.CI_instance, 'children')

    @patch.object(un, 'request_information')
    def test_keyword_obtained_from_cmd(self, mock_request_info):
        un.main(self.CI_instance, 'children information')
        mock_request_info.assert_called_with('children')

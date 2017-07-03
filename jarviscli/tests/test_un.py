import unittest
from mock import patch
from Jarvis import Jarvis


class UnTest(unittest.TestCase):

    @patch.object(Jarvis, 'default')
    def test_un_is_dict_cmd(self, mock_default):
        # Error message is printed if the cmd is only 'un' (without further words)
        J_instance = Jarvis()
        J_instance.precmd('un children')
        self.assertFalse(mock_default.called)
        J_instance.precmd('un')
        mock_default.assert_called()

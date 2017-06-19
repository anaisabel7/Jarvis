import unittest
import os
<<<<<<< HEAD
import re
from mock import call, patch, mock_open
from packages import music

class MusicTest(unittest.TestCase):

    def setUp(self):
        self.song_name = 'alex kara stand by you'
        self.filename = "Alex & Kara | Stand By You.mp3"
        self.first_system_call = call("instantmusic -s " + self.song_name)
        self.final_system_call = call("XDG_CURRENT_DESKTOP= DESKTOP_SESSION= xdg-open " + re.escape(self.filename))
        self.first_popen_call = call("ls | grep -i " +'"'+ self.song_name +'"')

    def test_song_is_searched_with_the_given_song_name(self):
        with patch.object(os, 'system', return_value=None) as mock_system:
            with patch.object(os, 'popen', return_value=os.popen("")) as mock_popen:
                music.play(self.song_name)
                mock_popen.assert_has_calls([self.first_popen_call])
                mock_system.assert_has_calls([self.first_system_call])

    def test_song_is_not_searched_without_a_song_name(self):
        with patch.object(os, 'system', return_value=None) as mock_system:
            with patch.object(os, 'popen', return_value=os.popen("")) as mock_popen:
                music.play('')
                self.assertFalse(mock_popen.called)
                self.assertFalse(mock_system.called)

    def test_characters_escaped_from_local_song_filename_in_terminal_cmd(self):
        m = mock_open()
        def myreadline():
            return self.filename

        m.readline = myreadline

        with patch.object(os, 'system', return_value=None) as mock_system:
            with patch.object(os, 'popen', return_value=m) as mock_popen:
                music.play(self.song_name)
                mock_system.assert_has_calls([self.final_system_call])
                self.assertEqual(mock_system.call_count, 1)

    def test_characters_escaped_from_downloaded_song_filename_in_terminal_cmd(self):
        m = mock_open()
        global count
        count = 0
        def myreadline():
            global count
            if count == 1:
                return self.filename
            count = count + 1
            return ''

        m.readline = myreadline

        with patch.object(os, 'system', return_value=None) as mock_system:
            with patch.object(os, 'popen', return_value=m) as mock_popen:
                music.play(self.song_name)
                mock_system.assert_has_calls([self.final_system_call])
                self.assertEqual(mock_system.call_count, 2)
                self.assertEqual(mock_popen.call_count, 2)

import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Leon Bridges - River")
        self.song_2 = Song("Vance Joy - Riptide")

    def test_has_song(self):
        self.assertEqual("Leon Bridges - River", self.song_1.name)
        self.assertEqual("Vance Joy - Riptide", self.song_2.name)
import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Vance Joy - Riptide")
        self.song_2 = Song("Leon Bridges - River")
        self.guest_1 = Guest("Jan", 35)
        self.guest_2 = Guest("Jessica", 31)
        self.guest_3 = Guest("Timmy", 69)
        songs_1 = [self.song_1, self.song_2]
        songs_2 = []
        self.room_1 = Room("Indie", songs_1)
        self.room_2 = Room("Soul", songs_2)

    def test_guest_has_name(self):
        self.assertEqual("Indie", self.room_1.name)
        self.assertEqual("Soul", self.room_2.name)

    def test_no_guests_in_room(self):
        self.assertEqual(0, self.room_1.get_guests_in_room())

    def test_room_has_songs(self):
        self.assertEqual(2, self.room_1.check_songs())

    def test_room_can_add_song(self):
        self.song_3 = Song("Ben Howard - Promise")
        self.room_1.add_song_to_room(self.song_3)
        self.assertEqual(3, self.room_1.check_songs())

    def test_room_can_add_guests(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEqual(["Jan"], self.room_1.guests_in_room)

    def test_room_can_remove_guests(self):
        self.room_1.add_guest_to_room(self.guest_3)
        self.room_1.remove_guest_from_room()
        self.assertEqual([], self.room_1.guests_in_room)

    # def test_guest_check_in(self):
    #     self.room_1.guest_check_in(self.guest_1)
    #     self.assertEqual(45, self.guest_1.money)

    # def test_guest_cant_check_in(self):
    #     self.room_1.guest_check_in(self.guest_3)
    #     self.assertEqual(3, self.guest_3.money)
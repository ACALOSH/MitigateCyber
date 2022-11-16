import unittest
import sqlite3

from main import Tasks

class Tests(unittest.TestCase):

    def test_create(self):
        con = sqlite3.connect("database.db")
        Tasks.create(con, "extra task")
        self.assertEqual(Tasks.create(con,"txt msg"), "Your task: txt msg has been added!", 'msg is wrong.')

    def test_update(self):
        con = sqlite3.connect("database.db")
        self.assertEqual(Tasks.update(con, 1, "update txt msg"), "Task 1 has been updated to: update txt msg", 'msg is wrong.')


    def test_stop(self):
        con = sqlite3.connect("database.db")
        self.assertEqual(Tasks.stop(con, 2), "Task 2 has been stopped", 'msg is wrong.')

    def test_delete(self):
        con = sqlite3.connect("database.db")
        self.assertEqual(Tasks.delete(con, 1), "Task 1 has been deleted", 'msg is wrong.')

    def test_wrongdelete(self):
        con = sqlite3.connect("database.db")
        self.assertEqual(Tasks.delete(con, 100), "Task 100 is not in table", 'msg is wrong.')

if __name__ == '__main__':
    unittest.main()
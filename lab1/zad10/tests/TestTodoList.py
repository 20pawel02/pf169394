import unittest
from zad10.src.TodoList import TodoList


class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = TodoList()

    def test_add_task(self):
        self.todo_list.add_task("zad1")
        self.assertIn("zad1", self.todo_list.get_active_tasks())

    def test_complete_task(self):
        self.todo_list.add_task("zad1")
        self.todo_list.complete_task("zad1")
        self.assertIn("zad1", self.todo_list.get_completed_tasks())

    def test_get_active_tasks(self):
        self.todo_list.add_task("zad")
        self.todo_list.add_task("zad1")
        self.todo_list.complete_task("zad")
        self.assertEqual(self.todo_list.get_active_tasks(), ["zad1"])

    def test_get_completed_tasks(self):
        self.todo_list.add_task("zad")
        self.todo_list.add_task("zad1")
        self.todo_list.add_task("zad2")
        self.todo_list.add_task("zad3")
        self.todo_list.complete_task("zad")
        self.todo_list.complete_task("zad1")
        self.todo_list.complete_task("zad2")
        self.todo_list.complete_task("zad3")
        self.assertEqual(self.todo_list.get_completed_tasks(), ["zad", "zad1", "zad2", "zad3"])


if __name__ == '__main__':
    unittest.main()

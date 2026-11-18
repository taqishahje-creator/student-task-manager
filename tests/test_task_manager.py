import unittest

import main


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        main.tasks.clear()

    def test_adds_valid_task(self):
        self.assertTrue(main.add_task("Read chapter one"))
        self.assertEqual(main.tasks, [{"id": 1, "title": "Read chapter one", "completed": False}])

    def test_rejects_empty_task_title(self):
        self.assertFalse(main.add_task("   "))
        self.assertEqual(main.tasks, [])

    def test_completes_existing_task(self):
        main.add_task("Submit assignment")
        self.assertTrue(main.complete_task(1))
        self.assertTrue(main.tasks[0]["completed"])

    def test_deletes_valid_task_after_confirmation(self):
        main.add_task("Temporary task")
        self.assertTrue(main.delete_task(1, "yes"))
        self.assertEqual(main.tasks, [])

    def test_handles_invalid_task_id(self):
        main.add_task("Existing task")
        self.assertFalse(main.complete_task("not-a-number"))
        self.assertFalse(main.delete_task(99, "yes"))
        self.assertEqual(len(main.tasks), 1)

    def test_prevents_duplicate_task_titles_case_insensitively(self):
        self.assertTrue(main.add_task("Plan presentation"))
        self.assertFalse(main.add_task(" plan PRESENTATION "))
        self.assertEqual(len(main.tasks), 1)


if __name__ == "__main__":
    unittest.main()

import io
import unittest
from contextlib import redirect_stdout

import _paths  # noqa: F401
import check_skill


class CheckSkillTest(unittest.TestCase):
    def test_repository_is_consistent(self):
        check_skill.errors.clear()
        with redirect_stdout(io.StringIO()) as out:
            code = check_skill.main()
        self.assertEqual(code, 0, out.getvalue())


if __name__ == "__main__":
    unittest.main()

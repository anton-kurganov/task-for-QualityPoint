import io
import unittest
from unittest.mock import patch


class TestProgram(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_basic_input(self, mock_stdout):
        with patch('builtins.input', side_effect=['123', '456', '789', '0']):
            prog = open('task_numbers.py')
            exec(prog.read())
            self.assertEqual(mock_stdout.getvalue(), '789\n')
            prog.close()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boundary_input(self, mock_stdout):
        with patch('builtins.input', side_effect=['999999', '1000000', '0']):
            prog = open('task_numbers.py')
            exec(prog.read())
            self.assertEqual(mock_stdout.getvalue(), '999999\n')
            prog.close()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_error_input(self, mock_stdout):
        with patch('builtins.input', side_effect=['abc', '0']):
            prog = open('task_numbers.py')
            exec(prog.read())
            prog.close()
            self.assertEqual(mock_stdout.getvalue(), '0\n')


if __name__ == '__main__':
    unittest.main()

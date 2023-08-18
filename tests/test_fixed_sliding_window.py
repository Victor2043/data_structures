import unittest
from sliding_window.fixed_sliding_window import fixed_sliding_window

class TestFixedSlidingWindow(unittest.TestCase):
    def test_should_return_all_possible_combinations(self):
        nums = [1, 2, 3, 4, 5, 6]
        window_size = 3
        expected_result = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
        result = fixed_sliding_window(nums, window_size)
        self.assertEqual(result, expected_result)

    def test_should_return_empty_list(self):
        nums = [1, 2, 3]
        window_size = 4
        expected_result = []
        result = fixed_sliding_window(nums, window_size)
        self.assertEqual(result, expected_result)
    
    def test_should_return_every_value_with_window_size_one(self):
        nums = [1, 2, 3]
        window_size = 1
        expected_result = [[1], [2], [3]]
        result = fixed_sliding_window(nums, window_size)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()


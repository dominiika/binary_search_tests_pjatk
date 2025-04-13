import time

from binary_search import binary_search
from unittest import TestCase

from k_steps_leaps import k_steps_leaps


class TestBinarySearch(TestCase):
    def setUp(self):
        self.data = [-1, 2, 4, 10, 20, 23, 40, 90, 100]

    def test_binary_search__target_found(self):
        target = 20

        result = binary_search(self.data, target)

        expected_result = 4
        self.assertEqual(result, expected_result)


    def test_binary_search__target_as_first(self):
        target = -1

        result = binary_search(self.data, target)

        expected_result = 0
        self.assertEqual(result, expected_result)


    def test_binary_search__target_as_last(self):
        target = 100

        result = binary_search(self.data, target)

        expected_result = len(self.data) - 1
        self.assertEqual(result, expected_result)

    def test_binary_search__target_not_found(self):
        target = 200

        result = binary_search(self.data, target)

        expected_result = -1
        self.assertEqual(result, expected_result)

    def test_binary_search__target_duplicated(self):
        data = [1, 5, 5,7, 4, 6]
        target = 5

        result = binary_search(data, target)

        expected_result = 2
        self.assertEqual(result, expected_result)

    def test_binary_search__one_element_found(self):
        data = [5]
        target = 5

        result = binary_search(data, target)

        expected_result = 0
        self.assertEqual(result, expected_result)


    def test_binary_search__one_element_not_found(self):
        data = [5]
        target = 1

        result = binary_search(data, target)

        expected_result = -1
        self.assertEqual(result, expected_result)

    def test_binary_search_execution_time_less_than_k_step_leaps(self):
        execution_time_binary =self._measure_execution_time(binary_search)

        execution_k_steps =self._measure_execution_time(k_steps_leaps)


        self.assertLess(execution_time_binary, execution_k_steps)

    def _measure_execution_time(self, algo):
        start = time.time()
        algo(self.data, 10)
        end = time.time()
        return end - start
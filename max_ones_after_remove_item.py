import unittest

def max_ones_after_remove_item(array):
    max_ones = 0
    first_max_ones = 0
    second_max_ones = 0
    first_zero = False
    second_zero = False
    prev_digit = None

    for digit in array:
        if digit == 1:
            first_max_ones += 1
            if first_zero:
                second_max_ones += 1

            if first_max_ones > max_ones:
                max_ones = first_max_ones
            if second_max_ones >= max_ones:
                max_ones = second_max_ones
        else:
            if prev_digit == 0:
                first_zero = False
                second_zero = False
                first_max_ones = 0
                second_max_ones = 0
            else:
                if not first_zero and not second_zero:
                    first_zero = True
                    continue
                if first_zero and not second_zero:
                    second_zero = True
                    first_max_ones = 0
                    continue
                if first_zero and second_zero:
                    first_zero = False
                    second_zero = False
                    second_max_ones = 0
        prev_digit = digit

    if len(array) == max_ones:
        max_ones -= 1

    return max_ones


class TestMaxOnesAfterRemoveItem(unittest.TestCase):
    def test_max_ones_after_remove_item(self):
        self.assertEqual(max_ones_after_remove_item([0, 0]), 0)
        self.assertEqual(max_ones_after_remove_item([0, 1]), 1)
        self.assertEqual(max_ones_after_remove_item([1, 0]), 1)
        self.assertEqual(max_ones_after_remove_item([1, 1]), 1)
        self.assertEqual(max_ones_after_remove_item([1, 1, 0, 1, 1]), 4)
        self.assertEqual(max_ones_after_remove_item([1, 1, 0, 1, 1, 0, 1, 1, 1]), 5)
        self.assertEqual(max_ones_after_remove_item([1, 1, 0, 1, 1, 0, 1, 1, 1, 0]), 5)

        self.assertEqual(max_ones_after_remove_item([0, 1, 1, 1]), 3)
        self.assertEqual(max_ones_after_remove_item([1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1]), 5)


if __name__ == '__main__':
    unittest.main()

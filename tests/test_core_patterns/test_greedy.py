"""
Comprehensive tests for Greedy Algorithms.
"""

import pytest
from dsa.core_patterns.greedy import GreedySolutions


class TestJumpGame:
    """Tests for Jump Game problem."""

    def test_can_reach_end(self):
        assert GreedySolutions.jump_game([2, 3, 1, 1, 4]) == True

    def test_cannot_reach_end(self):
        assert GreedySolutions.jump_game([3, 2, 1, 0, 4]) == False

    def test_single_element(self):
        assert GreedySolutions.jump_game([0]) == True

    def test_all_zeros_except_first(self):
        assert GreedySolutions.jump_game([2, 0, 0]) == True

    def test_zero_in_middle(self):
        assert GreedySolutions.jump_game([2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3]) == True


class TestJumpGameII:
    """Tests for Jump Game II problem."""

    def test_basic_example(self):
        assert GreedySolutions.jump_game_ii([2, 3, 1, 1, 4]) == 2

    def test_single_element(self):
        assert GreedySolutions.jump_game_ii([0]) == 0

    def test_two_elements(self):
        assert GreedySolutions.jump_game_ii([1, 1]) == 1

    def test_large_jumps(self):
        assert GreedySolutions.jump_game_ii([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]) == 2


class TestGasStation:
    """Tests for Gas Station problem."""

    def test_basic_example(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        assert GreedySolutions.gas_station(gas, cost) == 3

    def test_impossible(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        assert GreedySolutions.gas_station(gas, cost) == -1

    def test_start_at_zero(self):
        gas = [5, 1, 2, 3, 4]
        cost = [4, 4, 1, 5, 1]
        assert GreedySolutions.gas_station(gas, cost) == 4

    def test_single_station(self):
        assert GreedySolutions.gas_station([1], [1]) == 0
        assert GreedySolutions.gas_station([1], [2]) == -1


class TestPartitionLabels:
    """Tests for Partition Labels problem."""

    def test_basic_example(self):
        result = GreedySolutions.partition_labels("ababcbacadefegdehijhklij")
        assert result == [9, 7, 8]

    def test_all_same_char(self):
        assert GreedySolutions.partition_labels("aaaaa") == [5]

    def test_all_unique(self):
        assert GreedySolutions.partition_labels("abcdef") == [1, 1, 1, 1, 1, 1]

    def test_two_partitions(self):
        assert GreedySolutions.partition_labels("aba") == [3]


class TestTaskScheduler:
    """Tests for Task Scheduler problem."""

    def test_basic_example(self):
        assert GreedySolutions.task_scheduler(['A', 'A', 'A', 'B', 'B', 'B'], 2) == 8

    def test_no_cooling(self):
        assert GreedySolutions.task_scheduler(['A', 'A', 'A', 'B', 'B', 'B'], 0) == 6

    def test_enough_variety(self):
        assert GreedySolutions.task_scheduler(['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'E'], 2) == 12

    def test_single_task(self):
        assert GreedySolutions.task_scheduler(['A'], 2) == 1


class TestNonOverlappingIntervals:
    """Tests for Non-overlapping Intervals problem."""

    def test_basic_example(self):
        assert GreedySolutions.non_overlapping_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1

    def test_all_overlapping(self):
        assert GreedySolutions.non_overlapping_intervals([[1, 2], [1, 2], [1, 2]]) == 2

    def test_no_overlapping(self):
        assert GreedySolutions.non_overlapping_intervals([[1, 2], [2, 3], [3, 4]]) == 0

    def test_empty(self):
        assert GreedySolutions.non_overlapping_intervals([]) == 0

    def test_single_interval(self):
        assert GreedySolutions.non_overlapping_intervals([[1, 2]]) == 0


class TestMinimumArrows:
    """Tests for Minimum Number of Arrows problem."""

    def test_basic_example(self):
        assert GreedySolutions.minimum_arrows([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2

    def test_all_separate(self):
        assert GreedySolutions.minimum_arrows([[1, 2], [3, 4], [5, 6]]) == 3

    def test_all_overlapping(self):
        assert GreedySolutions.minimum_arrows([[1, 10], [2, 9], [3, 8], [4, 7]]) == 1

    def test_empty(self):
        assert GreedySolutions.minimum_arrows([]) == 0

    def test_touching_boundaries(self):
        assert GreedySolutions.minimum_arrows([[1, 2], [2, 3], [3, 4]]) == 2


class TestQueueReconstruction:
    """Tests for Queue Reconstruction by Height problem."""

    def test_basic_example(self):
        people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        expected = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        assert GreedySolutions.queue_reconstruction(people) == expected

    def test_all_same_height(self):
        people = [[5, 0], [5, 1], [5, 2]]
        expected = [[5, 0], [5, 1], [5, 2]]
        assert GreedySolutions.queue_reconstruction(people) == expected

    def test_single_person(self):
        assert GreedySolutions.queue_reconstruction([[7, 0]]) == [[7, 0]]


class TestReorganizeString:
    """Tests for Reorganize String problem."""

    def test_possible_reorganization(self):
        result = GreedySolutions.reorganize_string("aab")
        assert result in ["aba", "baa"]
        # Verify no adjacent same chars
        for i in range(len(result) - 1):
            assert result[i] != result[i+1]

    def test_impossible(self):
        assert GreedySolutions.reorganize_string("aaab") == ""

    def test_already_valid(self):
        result = GreedySolutions.reorganize_string("abc")
        assert len(result) == 3

    def test_all_same(self):
        assert GreedySolutions.reorganize_string("aaa") == ""

    def test_two_chars(self):
        result = GreedySolutions.reorganize_string("aabb")
        assert result in ["abab", "baba"]


class TestCandy:
    """Tests for Candy Distribution problem."""

    def test_basic_example(self):
        assert GreedySolutions.candy([1, 0, 2]) == 5

    def test_equal_ratings(self):
        assert GreedySolutions.candy([1, 2, 2]) == 4

    def test_decreasing(self):
        assert GreedySolutions.candy([3, 2, 1]) == 6

    def test_increasing(self):
        assert GreedySolutions.candy([1, 2, 3]) == 6

    def test_single_child(self):
        assert GreedySolutions.candy([1]) == 1

    def test_valley(self):
        assert GreedySolutions.candy([1, 3, 2, 2, 1]) == 7


class TestGreedyEdgeCases:
    """Test edge cases across greedy problems."""

    def test_empty_inputs(self):
        assert GreedySolutions.partition_labels("") == []
        assert GreedySolutions.candy([]) == 0

    def test_single_elements(self):
        assert GreedySolutions.jump_game([1]) == True
        assert GreedySolutions.candy([5]) == 1

    def test_large_inputs(self):
        # Jump game with large array
        large_array = [1] * 10000
        assert GreedySolutions.jump_game(large_array) == True

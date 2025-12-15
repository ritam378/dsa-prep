"""
Greedy Algorithms Pattern

Pattern: Make the locally optimal choice at each step with the hope of finding a global optimum.

When to use:
- Optimization problems where local optimum leads to global optimum
- Problems with optimal substructure and greedy-choice property
- Activity selection, scheduling problems
- Huffman coding, Dijkstra's algorithm
- Minimum spanning trees

Key Characteristics:
1. Greedy Choice Property: A global optimum can be arrived at by selecting a local optimum
2. Optimal Substructure: An optimal solution contains optimal solutions to subproblems

Time Complexity: Usually O(n log n) due to sorting
Space Complexity: Usually O(1) to O(n)

INTERVIEW TIPS:
- Not all problems have greedy solutions - need to prove greedy works
- Usually involves sorting first
- Greedy doesn't always work - sometimes need DP instead
- Common mistake: assuming greedy works without proof
- Ask: "Will local optimum lead to global optimum?"
- Test with counterexamples

Difficulty: Medium
Interview Frequency: HIGH
Companies: Google, Facebook, Amazon, Microsoft, Apple, Netflix
"""

from typing import List, Tuple


class GreedySolutions:
    """Solutions using greedy algorithm pattern."""

    @staticmethod
    def jump_game(nums: List[int]) -> bool:
        """
        Determine if you can reach the last index.

        Each element represents max jump length from that position.

        Greedy approach: Track the farthest position reachable.

        Args:
            nums: Array where nums[i] is max jump length at position i

        Returns:
            True if can reach last index, False otherwise

        Time Complexity: O(n)
        Space Complexity: O(1)

        Difficulty: Medium
        Interview Frequency: HIGH
        Companies: Google, Amazon, Microsoft, Apple
        Estimated Time: 15-20 minutes

        Example:
            >>> GreedySolutions.jump_game([2,3,1,1,4])
            True
            >>> GreedySolutions.jump_game([3,2,1,0,4])
            False

        Interview Tips:
        - Greedy is simpler than DP for this problem
        - Track max reachable position, update as you go
        - If current position > max reachable, return False
        - Can also solve with BFS but greedy is optimal
        """
        max_reach = 0

        for i in range(len(nums)):
            # If current position is beyond max reachable, can't proceed
            if i > max_reach:
                return False

            # Update max reachable position
            max_reach = max(max_reach, i + nums[i])

            # Early termination if we can reach the end
            if max_reach >= len(nums) - 1:
                return True

        return True

    @staticmethod
    def jump_game_ii(nums: List[int]) -> int:
        """
        Return minimum number of jumps to reach last index.

        Greedy approach: Make jumps greedily, choosing position that
        allows furthest reach on next jump.

        Args:
            nums: Array where nums[i] is max jump length at position i

        Returns:
            Minimum number of jumps to reach last index

        Time Complexity: O(n)
        Space Complexity: O(1)

        Difficulty: Medium
        Interview Frequency: HIGH
        Companies: Google, Facebook, Amazon, Microsoft
        Estimated Time: 20-25 minutes

        Example:
            >>> GreedySolutions.jump_game_ii([2,3,1,1,4])
            2

        Interview Tips:
        - Think of it as BFS levels (each jump is a level)
        - Track current jump's max reach and next jump's max reach
        - Increment jumps when reaching end of current jump range
        - Can also solve with DP but greedy is O(n) vs O(n²)
        """
        if len(nums) <= 1:
            return 0

        jumps = 0
        current_end = 0  # End of current jump range
        farthest = 0     # Farthest we can reach from current range

        for i in range(len(nums) - 1):
            # Update farthest position reachable from current range
            farthest = max(farthest, i + nums[i])

            # When we reach end of current jump range, make another jump
            if i == current_end:
                jumps += 1
                current_end = farthest

                # Early termination
                if current_end >= len(nums) - 1:
                    break

        return jumps

    @staticmethod
    def gas_station(gas: List[int], cost: List[int]) -> int:
        """
        Find starting gas station to complete circular route.

        gas[i] = gas at station i
        cost[i] = gas needed to go from station i to i+1

        Greedy insight: If total gas >= total cost, solution exists.
        Start from station where tank doesn't go negative.

        Args:
            gas: Gas available at each station
            cost: Gas cost to travel to next station

        Returns:
            Starting station index, or -1 if impossible

        Time Complexity: O(n)
        Space Complexity: O(1)

        Difficulty: Medium
        Interview Frequency: Medium-High
        Companies: Amazon, Facebook, Google
        Estimated Time: 20-25 minutes

        Example:
            >>> GreedySolutions.gas_station([1,2,3,4,5], [3,4,5,1,2])
            3

        Interview Tips:
        - Key insight: if sum(gas) >= sum(cost), solution exists
        - If tank becomes negative, start can't be before this point
        - Reset start position when tank goes negative
        - One pass solution using greedy observation
        """
        total_tank = 0
        current_tank = 0
        start_station = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            # If tank becomes negative, can't start from current start
            if current_tank < 0:
                start_station = i + 1
                current_tank = 0

        return start_station if total_tank >= 0 else -1

    @staticmethod
    def partition_labels(s: str) -> List[int]:
        """
        Partition string into as many parts as possible where each letter
        appears in at most one part.

        Greedy approach: Track last occurrence of each character.
        Extend current partition until we've seen all chars.

        Args:
            s: Input string

        Returns:
            List of partition sizes

        Time Complexity: O(n)
        Space Complexity: O(1) - at most 26 letters

        Difficulty: Medium
        Interview Frequency: Medium
        Companies: Amazon, Facebook
        Estimated Time: 20-25 minutes

        Example:
            >>> GreedySolutions.partition_labels("ababcbacadefegdehijhklij")
            [9, 7, 8]

        Interview Tips:
        - First pass: record last occurrence of each character
        - Second pass: extend partition end to include all occurrences
        - When reach partition end, create new partition
        - Similar to merge intervals conceptually
        """
        # Record last occurrence of each character
        last_occurrence = {char: i for i, char in enumerate(s)}

        partitions = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            # Extend partition to include last occurrence of current char
            end = max(end, last_occurrence[char])

            # If we've reached the end of partition
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1

        return partitions

    @staticmethod
    def task_scheduler(tasks: List[str], n: int) -> int:
        """
        Schedule tasks with cooling interval.

        Same task must be n intervals apart.
        Return minimum intervals needed.

        Greedy approach: Schedule most frequent tasks first,
        fill gaps with other tasks or idle time.

        Args:
            tasks: List of tasks (represented by letters)
            n: Cooling interval between same tasks

        Returns:
            Minimum intervals needed

        Time Complexity: O(n) where n is number of tasks
        Space Complexity: O(1) - at most 26 task types

        Difficulty: Medium
        Interview Frequency: Medium-High
        Companies: Google, Facebook, Amazon
        Estimated Time: 25-30 minutes

        Example:
            >>> GreedySolutions.task_scheduler(['A','A','A','B','B','B'], 2)
            8

        Interview Tips:
        - Key insight: most frequent task determines minimum time
        - Formula: max(len(tasks), (max_freq - 1) * (n + 1) + num_max_tasks)
        - Can use heap for actual scheduling (more complex)
        - Math formula is elegant greedy solution
        """
        from collections import Counter

        if n == 0:
            return len(tasks)

        # Count frequency of each task
        freq_map = Counter(tasks)
        max_freq = max(freq_map.values())

        # Count how many tasks have max frequency
        num_max_freq = sum(1 for freq in freq_map.values() if freq == max_freq)

        # Calculate minimum intervals
        # (max_freq - 1): number of "chunks" between first and last max task
        # (n + 1): size of each chunk (task + cooling period)
        # + num_max_freq: tasks with max frequency at end
        intervals = (max_freq - 1) * (n + 1) + num_max_freq

        # Can't be less than total tasks
        return max(intervals, len(tasks))

    @staticmethod
    def non_overlapping_intervals(intervals: List[List[int]]) -> int:
        """
        Find minimum number of intervals to remove to make rest non-overlapping.

        Greedy approach: Sort by end time, keep intervals that end earliest.

        Args:
            intervals: List of [start, end] intervals

        Returns:
            Minimum number of intervals to remove

        Time Complexity: O(n log n) for sorting
        Space Complexity: O(1)

        Difficulty: Medium
        Interview Frequency: Medium-High
        Companies: Amazon, Microsoft, Google
        Estimated Time: 20-25 minutes

        Example:
            >>> GreedySolutions.non_overlapping_intervals([[1,2],[2,3],[3,4],[1,3]])
            1

        Interview Tips:
        - Classic interval scheduling problem
        - Sort by end time (greedy choice: earliest ending)
        - Skip intervals that overlap with last kept interval
        - Similar to activity selection problem
        - Can also think as: max non-overlapping intervals, then subtract
        """
        if not intervals:
            return 0

        # Sort by end time
        intervals.sort(key=lambda x: x[1])

        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            # If current interval overlaps with previous
            if intervals[i][0] < prev_end:
                count += 1  # Remove current interval
            else:
                prev_end = intervals[i][1]  # Update end time

        return count

    @staticmethod
    def minimum_arrows(points: List[List[int]]) -> int:
        """
        Find minimum arrows needed to burst all balloons.

        Each balloon is [start, end]. Arrow at x bursts all balloons where
        start <= x <= end.

        Greedy approach: Sort by end, shoot arrow at earliest end.

        Args:
            points: List of [start, end] representing balloons

        Returns:
            Minimum number of arrows needed

        Time Complexity: O(n log n) for sorting
        Space Complexity: O(1)

        Difficulty: Medium
        Interview Frequency: Medium
        Companies: Amazon, Microsoft
        Estimated Time: 20-25 minutes

        Example:
            >>> GreedySolutions.minimum_arrows([[10,16],[2,8],[1,6],[7,12]])
            2

        Interview Tips:
        - Similar to non-overlapping intervals
        - Greedy: shoot arrow at end of first balloon
        - This arrow bursts all overlapping balloons
        - Find next non-burst balloon and repeat
        """
        if not points:
            return 0

        # Sort by end position
        points.sort(key=lambda x: x[1])

        arrows = 1
        current_end = points[0][1]

        for i in range(1, len(points)):
            # If balloon starts after current arrow position
            if points[i][0] > current_end:
                arrows += 1
                current_end = points[i][1]

        return arrows

    @staticmethod
    def queue_reconstruction(people: List[List[int]]) -> List[List[int]]:
        """
        Reconstruct queue based on height and number of taller people in front.

        people[i] = [h, k] where h = height, k = number of people >= h in front

        Greedy approach: Sort by height desc, then insert by k position.

        Args:
            people: List of [height, k] pairs

        Returns:
            Reconstructed queue

        Time Complexity: O(n²) due to insertions
        Space Complexity: O(n)

        Difficulty: Medium
        Interview Frequency: Medium
        Companies: Google, Amazon
        Estimated Time: 25-30 minutes

        Example:
            >>> GreedySolutions.queue_reconstruction([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
            [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

        Interview Tips:
        - Non-obvious greedy solution
        - Key insight: process tallest people first
        - For same height, process smaller k first
        - Insert at position k (shorter people don't affect taller)
        - Draw example to understand the pattern
        """
        # Sort by height descending, then by k ascending
        people.sort(key=lambda x: (-x[0], x[1]))

        result = []
        for person in people:
            # Insert at position k
            result.insert(person[1], person)

        return result

    @staticmethod
    def reorganize_string(s: str) -> str:
        """
        Reorganize string so no two adjacent characters are the same.

        Greedy approach: Always place most frequent remaining character,
        ensuring it's different from previous.

        Args:
            s: Input string

        Returns:
            Reorganized string, or "" if impossible

        Time Complexity: O(n log k) where k is unique characters
        Space Complexity: O(k)

        Difficulty: Medium
        Interview Frequency: Medium
        Companies: Amazon, Google, Facebook
        Estimated Time: 25-30 minutes

        Example:
            >>> GreedySolutions.reorganize_string("aab")
            'aba'
            >>> GreedySolutions.reorganize_string("aaab")
            ''

        Interview Tips:
        - Use max heap to always get most frequent character
        - If most frequent char count > (n+1)//2, impossible
        - Keep track of previous character to avoid adjacency
        - Use heap to efficiently get next most frequent
        """
        from collections import Counter
        import heapq

        # Count frequencies
        freq_map = Counter(s)

        # Check if reorganization is possible
        max_freq = max(freq_map.values())
        if max_freq > (len(s) + 1) // 2:
            return ""

        # Max heap (use negative for max heap in Python)
        heap = [(-freq, char) for char, freq in freq_map.items()]
        heapq.heapify(heap)

        result = []
        prev_freq, prev_char = 0, ''

        while heap:
            # Get most frequent character
            freq, char = heapq.heappop(heap)
            result.append(char)

            # Put back previous character if it still has count
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))

            # Update previous (current becomes previous)
            prev_freq = freq + 1  # Increment (less negative)
            prev_char = char

        return ''.join(result) if len(result) == len(s) else ""

    @staticmethod
    def candy(ratings: List[int]) -> int:
        """
        Distribute candies to children such that:
        1. Each child gets at least 1 candy
        2. Children with higher rating get more candy than neighbors

        Return minimum candies needed.

        Greedy approach: Two passes - left to right, then right to left.

        Args:
            ratings: Array of children's ratings

        Returns:
            Minimum total candies needed

        Time Complexity: O(n)
        Space Complexity: O(n)

        Difficulty: Hard
        Interview Frequency: Medium
        Companies: Google, Amazon
        Estimated Time: 30-35 minutes

        Example:
            >>> GreedySolutions.candy([1,0,2])
            5
            >>> GreedySolutions.candy([1,2,2])
            4

        Interview Tips:
        - Two pass solution is key
        - First pass: left to right (satisfy left neighbor)
        - Second pass: right to left (satisfy right neighbor)
        - Take max of both passes for each position
        - One pass doesn't work - need to consider both directions
        """
        n = len(ratings)
        if n == 0:
            return 0

        candies = [1] * n

        # Left to right: if rating > left neighbor, give more candy
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # Right to left: if rating > right neighbor, ensure more candy
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)


# Greedy Algorithm Recognition Guide
GREEDY_RECOGNITION = """
HOW TO RECOGNIZE GREEDY PROBLEMS:

1. OPTIMIZATION KEYWORDS:
   - "Minimum/Maximum"
   - "Least/Most"
   - "Shortest/Longest"
   - "Optimal"

2. PROBLEM CHARACTERISTICS:
   - Making a sequence of choices
   - Each choice looks best at the moment
   - Can't undo previous choices
   - Local optimum leads to global optimum

3. COMMON PROBLEM TYPES:
   - Activity/Interval selection
   - Scheduling problems
   - Huffman encoding
   - Fractional knapsack (not 0/1)
   - Minimum spanning tree
   - Shortest path (Dijkstra)

4. GREEDY VS DYNAMIC PROGRAMMING:

   Use GREEDY when:
   ✓ Greedy choice property holds
   ✓ Optimal substructure exists
   ✓ Local optimum → global optimum
   ✓ Can prove correctness

   Use DP when:
   ✓ Overlapping subproblems
   ✓ Need to consider all possibilities
   ✓ Greedy doesn't give optimal solution
   ✓ 0/1 Knapsack, LCS, Edit Distance

5. VERIFICATION CHECKLIST:
   □ Can you make choice that looks best now?
   □ Does this choice reduce problem to smaller subproblem?
   □ Will local optimum lead to global optimum?
   □ Can you prove it with exchange argument?
   □ Try counterexamples - if greedy fails, use DP

6. COMMON GREEDY STRATEGIES:
   - Sort first, then make greedy choices
   - Use heap/priority queue for next best choice
   - Keep track of running maximum/minimum
   - Process elements in specific order

INTERVIEW APPROACH:
1. Identify if problem has greedy solution
2. Propose greedy strategy
3. Prove correctness (or give strong intuition)
4. Implement
5. Test with edge cases
6. Analyze complexity

RED FLAGS (Greedy won't work):
- Problem asks for "number of ways"
- Need exact count of solutions
- 0/1 choices (can't take fraction)
- Overlapping subproblems matter
- Order of previous choices affects future
"""

# 🚀 Complete Data Structures & Algorithms Guide

A comprehensive guide for learning DSA from fundamentals to advanced topics with practical problem-solving.

## 📚 Table of Contents
1. [Fundamental DSA Theory](#fundamental-dsa-theory)
2. [Array & String](#array--string)
3. [Two Pointers](#two-pointers)
4. [Sliding Window](#sliding-window)
5. [Binary Search](#binary-search)
6. [Stack](#stack)
7. [Linked List](#linked-list)
8. [Tree](#tree)
9. [Heap](#heap)
10. [Recursive Backtracking](#recursive-backtracking)
11. [Graph](#graph)
12. [Dynamic Programming](#dynamic-programming)

---

## 🎯 Fundamental DSA Theory

### Core Concepts
**Time Complexity (Big O Notation)**
- O(1) - Constant time
- O(log n) - Logarithmic (Binary Search)
- O(n) - Linear (Single loop)
- O(n log n) - Linearithmic (Efficient sorting)
- O(n²) - Quadratic (Nested loops)
- O(2ⁿ) - Exponential (Recursive branching)

**Space Complexity**
Understanding auxiliary space vs total space usage in algorithms.

**Key Problem-Solving Strategies**
- Brute Force → Optimize
- Pattern Recognition
- Break down into subproblems
- Use appropriate data structure

### Essential Math & Techniques
- Modular arithmetic
- Prime numbers & GCD
- Bit manipulation basics
- Prefix sums
- Two's complement

---

## 📦 Array & String

### Theory & Patterns
Arrays are contiguous memory blocks with O(1) access. Strings are immutable in many languages (Java, Python).

**Key Techniques:**
- In-place modification to save space
- Hash maps for frequency counting
- Sorting for easier processing
- Prefix/suffix arrays

### Practice Problems

**Easy:**
- Two Sum (LeetCode 1)
- Best Time to Buy and Sell Stock (121)
- Contains Duplicate (217)
- Valid Anagram (242)
- Majority Element (169)
- Move Zeroes (283)
- Plus One (66)
- Merge Sorted Array (88)

**Medium:**
- 3Sum (15)
- Product of Array Except Self (238)
- Container With Most Water (11)
- Rotate Array (189)
- Group Anagrams (49)
- Longest Substring Without Repeating Characters (3)
- String to Integer (atoi) (8)
- Spiral Matrix (54)
- Set Matrix Zeroes (73)

**Hard:**
- Trapping Rain Water (42)
- First Missing Positive (41)
- Median of Two Sorted Arrays (4)

---

## 👉👈 Two Pointers

### Theory & Patterns
Using two pointers to traverse array/string from different positions to optimize from O(n²) to O(n).

**Common Patterns:**
- Opposite direction (start & end)
- Same direction (slow & fast)
- Used in sorted arrays often

### Practice Problems

**Easy:**
- Valid Palindrome (125)
- Remove Duplicates from Sorted Array (26)
- Merge Sorted Array (88)
- Remove Element (27)
- Intersection of Two Arrays II (350)

**Medium:**
- 3Sum (15)
- Container With Most Water (11)
- Sort Colors (75)
- Remove Nth Node From End of List (19)
- 4Sum (18)
- Partition Labels (763)

**Hard:**
- Trapping Rain Water (42)
- Minimum Window Substring (76)

---

## 🪟 Sliding Window

### Theory & Patterns
Maintain a window that slides through array/string. Used for contiguous subarrays/substrings.

**Types:**
- Fixed size window
- Variable size window
- Two pointer + hash map

**Time Complexity:** Usually O(n)

### Practice Problems

**Easy:**
- Maximum Average Subarray I (643)
- Contains Duplicate II (219)

**Medium:**
- Longest Substring Without Repeating Characters (3)
- Longest Repeating Character Replacement (424)
- Permutation in String (567)
- Maximum Length of Repeated Subarray (718)
- Fruit Into Baskets (904)
- Max Consecutive Ones III (1004)
- Subarray Product Less Than K (713)

**Hard:**
- Minimum Window Substring (76)
- Sliding Window Maximum (239)
- Substring with Concatenation of All Words (30)

---

## 🔍 Binary Search

### Theory & Patterns
Divide and conquer on sorted data. Reduces search space by half each iteration.

**Template:**
```python
left, right = 0, len(arr) - 1
while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

**Key Concepts:**
- Search in sorted array: O(log n)
- Finding boundaries (first/last occurrence)
- Binary search on answer space

### Practice Problems

**Easy:**
- Binary Search (704)
- Search Insert Position (35)
- First Bad Version (278)
- Valid Perfect Square (367)
- Sqrt(x) (69)

**Medium:**
- Search in Rotated Sorted Array (33)
- Find First and Last Position of Element (34)
- Search a 2D Matrix (74)
- Find Peak Element (162)
- Find Minimum in Rotated Sorted Array (153)
- Koko Eating Bananas (875)
- Capacity To Ship Packages Within D Days (1011)

**Hard:**
- Median of Two Sorted Arrays (4)
- Find Minimum in Rotated Sorted Array II (154)
- Split Array Largest Sum (410)

---

## 📚 Stack

### Theory & Patterns
LIFO (Last In First Out) data structure. O(1) push, pop, peek.

**Common Uses:**
- Expression evaluation
- Parentheses matching
- Monotonic stack (next greater/smaller element)
- DFS traversal
- Undo operations

### Practice Problems

**Easy:**
- Valid Parentheses (20)
- Implement Stack using Queues (225)
- Min Stack (155)
- Baseball Game (682)

**Medium:**
- Evaluate Reverse Polish Notation (150)
- Daily Temperatures (739)
- Next Greater Element II (503)
- Asteroid Collision (735)
- Decode String (394)
- Remove K Digits (402)
- Online Stock Span (901)

**Hard:**
- Largest Rectangle in Histogram (84)
- Maximal Rectangle (85)
- Trapping Rain Water (42)
- Basic Calculator (224)

---

## 🔗 Linked List

### Theory & Patterns
Linear data structure with nodes containing data and pointer to next node.

**Key Techniques:**
- Dummy head node to simplify edge cases
- Fast & slow pointer (cycle detection)
- Reverse linked list (iterative & recursive)
- Two pointer for intersection

**Time:** Access O(n), Insert/Delete O(1) at known position
**Space:** O(1) for in-place operations

### Practice Problems

**Easy:**
- Reverse Linked List (206)
- Merge Two Sorted Lists (21)
- Linked List Cycle (141)
- Remove Duplicates from Sorted List (83)
- Middle of the Linked List (876)
- Palindrome Linked List (234)

**Medium:**
- Add Two Numbers (2)
- Remove Nth Node From End (19)
- Reorder List (143)
- Linked List Cycle II (142)
- Intersection of Two Linked Lists (160)
- Odd Even Linked List (328)
- Rotate List (61)
- Copy List with Random Pointer (138)

**Hard:**
- Reverse Nodes in k-Group (25)
- Merge k Sorted Lists (23)
- LRU Cache (146)

---

## 🌳 Tree

### Theory & Patterns
Hierarchical data structure with root and children nodes.

**Types:**
- Binary Tree
- Binary Search Tree (BST)
- AVL Tree (balanced)
- Trie (prefix tree)

**Traversals:**
- Inorder (Left, Root, Right) - gives sorted for BST
- Preorder (Root, Left, Right)
- Postorder (Left, Right, Root)
- Level Order (BFS)

**Key Properties:**
- BST: left < root < right
- Complete tree: all levels filled except possibly last
- Balanced tree: height difference ≤ 1

### Practice Problems

**Easy:**
- Maximum Depth of Binary Tree (104)
- Same Tree (100)
- Invert Binary Tree (226)
- Symmetric Tree (101)
- Path Sum (112)
- Merge Two Binary Trees (617)
- Diameter of Binary Tree (543)

**Medium:**
- Binary Tree Level Order Traversal (102)
- Validate Binary Search Tree (98)
- Lowest Common Ancestor of BST (235)
- Binary Tree Right Side View (199)
- Kth Smallest Element in BST (230)
- Construct Binary Tree from Preorder and Inorder (105)
- Path Sum II (113)
- Flatten Binary Tree to Linked List (114)
- Populating Next Right Pointers (116)

**Hard:**
- Binary Tree Maximum Path Sum (124)
- Serialize and Deserialize Binary Tree (297)
- Lowest Common Ancestor of Binary Tree (236)
- Vertical Order Traversal (987)

---

## 🔺 Heap (Priority Queue)

### Theory & Patterns
Complete binary tree maintaining heap property. Min-heap or max-heap.

**Operations:**
- Insert: O(log n)
- Delete min/max: O(log n)
- Get min/max: O(1)
- Heapify: O(n)

**Common Uses:**
- K largest/smallest elements
- Median finding
- Merge K sorted lists
- Top K frequent elements
- Task scheduling

### Practice Problems

**Easy:**
- Kth Largest Element in a Stream (703)
- Last Stone Weight (1046)
- Relative Ranks (506)

**Medium:**
- Kth Largest Element in Array (215)
- Top K Frequent Elements (347)
- K Closest Points to Origin (973)
- Find K Pairs with Smallest Sums (373)
- Reorganize String (767)
- Task Scheduler (621)
- Ugly Number II (264)

**Hard:**
- Merge k Sorted Lists (23)
- Find Median from Data Stream (295)
- Sliding Window Median (480)
- IPO (502)

---

## 🔄 Recursive Backtracking

### Theory & Patterns
Exhaustively search through all possible solutions by making choices and undoing them.

**Template:**
```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path.copy())
        return
    
    for choice in choices:
        # Make choice
        path.append(choice)
        # Recurse
        backtrack(path, new_choices)
        # Undo choice
        path.pop()
```

**Common Patterns:**
- Permutations
- Combinations
- Subsets
- N-Queens
- Sudoku solving

### Practice Problems

**Easy:**
- Subsets (78)
- Permutations (46)

**Medium:**
- Combination Sum (39)
- Permutations II (47)
- Subsets II (90)
- Letter Combinations of Phone Number (17)
- Generate Parentheses (22)
- Palindrome Partitioning (131)
- Word Search (79)
- Combinations (77)
- Combination Sum II (40)

**Hard:**
- N-Queens (51)
- Sudoku Solver (37)
- Word Search II (212)
- Regular Expression Matching (10)

---

## 🕸️ Graph

### Theory & Patterns
Set of vertices connected by edges. Can be directed or undirected, weighted or unweighted.

**Representations:**
- Adjacency Matrix: O(V²) space
- Adjacency List: O(V + E) space (preferred)

**Key Algorithms:**
- **BFS:** Shortest path in unweighted graph, O(V + E)
- **DFS:** Explore all paths, cycle detection, O(V + E)
- **Dijkstra:** Shortest path in weighted graph, O((V + E) log V)
- **Union Find:** Detect cycles, connected components, O(α(n)) ≈ O(1)
- **Topological Sort:** Order tasks with dependencies
- **Kruskal/Prim:** Minimum spanning tree

### Practice Problems

**Easy:**
- Find the Town Judge (997)
- Find Center of Star Graph (1791)

**Medium:**
- Number of Islands (200)
- Clone Graph (133)
- Course Schedule (207)
- Pacific Atlantic Water Flow (417)
- Number of Connected Components (323)
- Graph Valid Tree (261)
- Rotting Oranges (994)
- Surrounded Regions (130)
- Word Ladder (127)
- Network Delay Time (743)

**Hard:**
- Course Schedule II (210)
- Alien Dictionary (269)
- Minimum Height Trees (310)
- Critical Connections in Network (1192)
- Swim in Rising Water (778)

---

## 💎 Dynamic Programming

### Theory & Patterns
Breaking problem into overlapping subproblems and storing results to avoid recomputation.

**Approach:**
1. Define state (what does dp[i] represent?)
2. Find recurrence relation
3. Identify base cases
4. Determine iteration order
5. Optimize space if possible

**Common Patterns:**
- **1D DP:** Fibonacci, House Robber
- **2D DP:** Edit Distance, Longest Common Subsequence
- **DP on Strings:** Palindrome, Pattern Matching
- **DP on Trees:** Path sums
- **Knapsack:** 0/1, Unbounded, Bounded
- **DP + State Machine:** Buy/Sell Stock

### Practice Problems

**Easy:**
- Climbing Stairs (70)
- Min Cost Climbing Stairs (746)
- House Robber (198)
- Best Time to Buy and Sell Stock (121)
- Maximum Subarray (53)

**Medium:**
- Longest Increasing Subsequence (300)
- Coin Change (322)
- Longest Common Subsequence (1143)
- Unique Paths (62)
- Word Break (139)
- House Robber II (213)
- Decode Ways (91)
- Partition Equal Subset Sum (416)
- Target Sum (494)
- Maximum Product Subarray (152)
- Longest Palindromic Substring (5)

**Hard:**
- Edit Distance (72)
- Regular Expression Matching (10)
- Wildcard Matching (44)
- Distinct Subsequences (115)
- Interleaving String (97)
- Best Time to Buy and Sell Stock III (123)
- Burst Balloons (312)
- Palindrome Partitioning II (132)

---

## 📖 Study Plan

### Week 1-2: Foundations
- Fundamental theory + Big O
- Arrays & Strings (Easy problems)
- Two Pointers (Easy → Medium)

### Week 3-4: Core Techniques
- Sliding Window
- Binary Search
- Stack problems

### Week 5-6: Linear Structures
- Linked Lists (all difficulties)
- More Stack & Queue problems

### Week 7-9: Trees & Heaps
- Binary Trees & BST
- Tree traversals
- Heap/Priority Queue

### Week 10-12: Advanced Topics
- Graphs (BFS, DFS, Union Find)
- Recursive Backtracking
- Introduction to DP

### Week 13-16: Dynamic Programming
- 1D DP patterns
- 2D DP patterns
- Hard DP problems

---

## 💡 Tips for Success

**Problem-Solving Approach:**
1. Understand the problem (read 2-3 times)
2. Identify patterns & data structures
3. Start with brute force
4. Optimize step by step
5. Code carefully with edge cases
6. Test with examples
7. Analyze complexity

**Practice Strategy:**
- Solve 2-3 problems daily consistently
- Revisit unsolved problems after 2 days
- Time yourself (45 min per medium problem)
- Review multiple solutions
- Focus on understanding, not memorizing

**Resources:**
- LeetCode / HackerRank for practice
- "Cracking the Coding Interview" book
- NeetCode YouTube channel
- Visualgo for algorithm visualization

---

## 🎯 Progress Tracker

Create a spreadsheet to track:
- [ ] Problems solved per topic
- [ ] Difficulty distribution
- [ ] Time taken per problem
- [ ] Review dates
- [ ] Weak areas to revisit

**Goal:** Aim for 200+ problems across all topics before interviews.

---

Happy Coding! 🚀 Remember: Consistency > Intensity

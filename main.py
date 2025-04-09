from test import seating_students

# Test suite: list of (input, expected_output)
test_cases = [
    ([12, 2, 6, 7, 11], 6),      # Original test case
    ([6, 4], 4),                 # Original test case
    ([8, 1, 8], 6),              # Original test case
    ([4], 4),                    # New: No desks are occupied
    ([10, 1, 2, 3, 4, 5], 4),    # New: First 5 desks are blocked
    ([2, 1], 0),                 # New: Only one available desk
    ([6, 1, 3, 5], 0),           # New: All odd desks occupied
]

# Run test suite
all_passed = True
for i, (input_data, expected) in enumerate(test_cases):
    result = seating_students(input_data)
    if result != expected:
        print(f"Test case {i+1} FAILED: input={input_data}, expected={expected}, got={result}")
        all_passed = False

if all_passed:
    print("✅ All test cases PASSED!")

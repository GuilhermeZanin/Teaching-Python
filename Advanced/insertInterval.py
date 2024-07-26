def insert_interval(intervals, newInterval):
    result = []
    i = 0
    
    # Add all intervals ending before the new interval starts
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)
    
    # Add all intervals starting after the new interval ends
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result

# Example test case
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert_interval(intervals, newInterval))  # Output: [[1, 5], [6, 9]]

# Example test cases
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert_interval(intervals, newInterval))  # Output: [[1, 5], [6, 9]]

# Additional test cases
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert_interval(intervals, newInterval))  # Output: [[1, 2], [3, 10], [12, 16]]

intervals = []
newInterval = [5,7]
print(insert_interval(intervals, newInterval))  # Output: [[5, 7]]

intervals = [[1,5]]
newInterval = [2,3]
print(insert_interval(intervals, newInterval))  # Output: [[1, 5]]

intervals = [[1,5]]
newInterval = [2,7]
print(insert_interval(intervals, newInterval))  # Output: [[1, 7]]

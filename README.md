# Python Week 1 Assignment

This repository contains 7 Python programming tasks.

# Tasks

1. Age CLI
2. Bug Fix
3. Bill Splitter
4. Password Checker
5. Text Extractor
6. Search and Sort
7. Result Manager

## Requirements

- Python 3.12 or newer
- Standard Python libraries only

## T2 – Fix the Legacy Receipt Script

### BUG-1: Missing Pen
**Cause:** The loop started from index 1, skipping the first item.

**Fix:** Changed `range(1, len(items))` to `range(0, len(items))`.

### BUG-2: Wrong Multiplication
**Cause:** The input quantities were strings instead of integers.

**Fix:** Used `list(map(int, ...))` to convert quantities into integers.

### BUG-3: Incorrect Total
**Cause:** `total = line` replaced the previous total.

**Fix:** Changed it to `total += line` to add all item prices.

### BUG-4: Wrong Discount
**Cause:** The 10% discount condition was checked before the 20% condition.

**Fix:** Checked `total > 1000` before `total > 500`.

### BUG-5: TypeError
**Cause:** The program tried to combine a string and a float using `+`.

**Fix:** Used `print("Pay: Rs", final)`.

### BUG-6: Invalid Input
**Cause:** Entering text instead of numbers caused a ValueError.

**Fix:** Added `try` and `except` to handle invalid input.

### Testing
- Input `2,1,1` → Final Payment: Rs 1112.0
- Input `two,1,1` → Invalid input message displayed.

All 6 bugs have been fixed successfully.
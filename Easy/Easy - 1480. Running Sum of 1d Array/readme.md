# Problem Description

Given an array `nums`, we define a **running sum** of an array as:  
`runningSum[i] = sum(nums[0]…nums[i])`.

Return the **running sum** of `nums`.

---

## Examples:

### Example 1:

**Input:**  
`nums = [1, 2, 3, 4]`

**Output:**  
`[1, 3, 6, 10]`

**Explanation:**  
The running sum is obtained as follows:  
`[1, 1+2, 1+2+3, 1+2+3+4]`.

---

### Example 2:

**Input:**  
`nums = [1, 1, 1, 1, 1]`

**Output:**  
`[1, 2, 3, 4, 5]`

**Explanation:**  
The running sum is obtained as follows:  
`[1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1]`.

---

### Example 3:

**Input:**  
`nums = [3, 1, 2, 10, 1]`

**Output:**  
`[3, 4, 6, 16, 17]`

**Explanation:**  
The running sum is obtained as follows:  
`[3, 3+1, 3+1+2, 3+1+2+10, 3+1+2+10+1]`.

---

## Constraints:

- `1 <= nums.length <= 1000`
- `-10^6 <= nums[i] <= 10^6`

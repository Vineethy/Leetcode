class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            # Need at least 3 bars to trap any water
            return 0

        left, right = 0, len(height) - 1  # Pointers at both ends
        left_max, right_max = 0, 0        # Track max height to the left and right
        total_water = 0                   # Accumulator for total trapped water

        while left < right:
            if height[left] < height[right]:
                # We process from the left side
                if height[left] >= left_max:
                    left_max = height[left]  # Update left max
                else:
                    # Water trapped is difference between left_max and current height
                    total_water += left_max - height[left]
                left += 1
            else:
                # We process from the right side
                if height[right] >= right_max:
                    right_max = height[right]  # Update right max
                else:
                    # Water trapped is difference between right_max and current height
                    total_water += right_max - height[right]
                right -= 1

        return total_water
        

package main

import "fmt"

func runningSum(nums []int) []int {
	for i := 0; i < len(nums); i++ {
		if i > 0 {
			nums[i] += nums[i-1]
		}
	}
	return nums
}

func main() {
	fmt.Println(runningSum([]int{1, 2, 3, 4}))
}

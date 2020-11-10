package leetcode

func flipAndInvertImage(A [][]int) [][]int {
    for i, s := range A {
        var tmp = make([]int, len(s))
        for j := len(s) -1; j >= 0; j-- {
            tmp[len(s) - j - 1] = s[j] ^ 1
        }
        A[i] = tmp
    }
    return A
}
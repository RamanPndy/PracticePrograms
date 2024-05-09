package main

import (
	"fmt"
	"math"
	"sync"
)

func coinChange(amount int, coins []int, ways chan int, minCoins chan int, wg *sync.WaitGroup) {
	defer wg.Done()

	waysToMake := make([]int, amount+1)
	minCoinsRequired := make([]int, amount+1)

	waysToMake[0] = 1
	minCoinsRequired[0] = 0

	for i := 1; i <= amount; i++ {
		minCoinsRequired[i] = math.MaxInt32
	}

	for _, coin := range coins {
		for i := coin; i <= amount; i++ {
			waysToMake[i] += waysToMake[i-coin]
			if minCoinsRequired[i-coin]+1 < minCoinsRequired[i] {
				minCoinsRequired[i] = minCoinsRequired[i-coin] + 1
			}
		}
	}

	ways <- waysToMake[amount]
	minCoins <- minCoinsRequired[amount]
}

func main() {
	amount := 10
	coins := []int{1, 2, 5}
	ways := make(chan int)
	minCoins := make(chan int)
	var wg sync.WaitGroup

	for _, coin := range coins {
		wg.Add(1)
		go coinChange(amount, []int{coin}, ways, minCoins, &wg)
	}

	go func() {
		wg.Wait()
		close(ways)
		close(minCoins)
	}()

	totalWays := 0
	minimumCoins := math.MaxInt32

	for w := range ways {
		totalWays += w
	}

	for mc := range minCoins {
		if mc < minimumCoins {
			minimumCoins = mc
		}
	}

	fmt.Printf("Total ways to make %d using coins %v: %d\n", amount, coins, totalWays)
	fmt.Printf("Minimum coins required to make %d: %d\n", amount, minimumCoins)
}

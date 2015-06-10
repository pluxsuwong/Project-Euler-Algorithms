// Problem 10 - Summation of Primes

#include <stdio.h>

int primeNums[500000]; 

int isPrime(int num) {
    int i = 0;
    while (primeNums[i] != 0) {
	if (num % primeNums[i] == 0) {
	    return 0;
	}
	else {
	    i++;
	}
    }
    primeNums[i] = num;
    return 1;
}

int main(int argc, char *argv[]) {
    printf("Problem 10 - Summation of Primes\n");

    int i = 0;
    long sum = 2;

    // Initialize DP tools
    for (i = 0; i < 500000; i++) {
	primeNums[i] = 0;
    }
    primeNums[0] = 2;

    for (i = 2; i < 2000000; i++) {
	if (isPrime(i) == 1) {
	    sum += i;
	}
	printf("%d\n", i);
    }
    printf("%ld\n", sum);
    return 0;
}

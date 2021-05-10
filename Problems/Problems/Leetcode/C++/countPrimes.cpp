// https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
class Solution {
public:
    int countPrimes(int n) {
        if (n < 2) return 0;
        bool isPrime[n];
        for (int i = 2; i < n; i++) {
            isPrime[i] = true;
        }
        for (int i = 2; i*i < n; i++) {
            for (int j = i*i; j < n; j += i) {
                isPrime[j] = false;
            }
        }
        int total = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime[i]) total++;
        }
        return total;
    }
};
# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.
#
# Note:
# (1) 1 is a super ugly number for any given primes.
# (2) The given numbers in primes are in ascending order.
# (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import heapq
        uglies = [1]

        def gen(prime):
            for ugly in uglies:
                yield ugly * prime

        merged = heapq.merge(*map(gen, primes))

        while len(uglies) < n:
            ugly = next(merged)
            if ugly != uglies[-1]:
                uglies.append(ugly)

        return uglies[-1]


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1] * n
        i_list = [-1] * len(primes)
        v_list = [1] * len(primes)
        k = 0
        while k < n:
            x = min(v_list)
            ugly[k] = x
            for v in xrange(len(v_list)):
                if x == v_list[v]:
                    i_list[v] += 1
                    v_list[v] = ugly[i_list[v]] * primes[v]
            k += 1
        return ugly[k - 1]

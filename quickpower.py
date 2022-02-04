### this is a code which gives a more efficient way of finding the power of an integer by dyadic expansion
### the efficiency of this algorithm is O(log_2(power)) I think

def quickpower(base: int, power: int) -> int:
    answer = base
    if power>1:
        answer = quickpower(base, power >> 1)*quickpower(base, power >> 1)*((base)**(power%2))
    return answer

### not getting the right answer, e.g. when I run for 2^4 I get 128

if __name__ == '__main__':
    base, power = int(input()), int(input())
    result = quickpower(base, power)
    print(result)

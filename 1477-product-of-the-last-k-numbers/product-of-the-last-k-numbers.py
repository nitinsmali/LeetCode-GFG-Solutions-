class ProductOfNumbers:

    def __init__(self):
        # Initialize with 1 to act as a neutral base for multiplication
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # A 0 makes any future product including it equal to 0, so reset
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is >= the length of valid non-zero products, a 0 was encountered within the last k elements
        if k >= len(self.prefix):
            return 0
        # Divide the total product by the product right before the last k elements
        return self.prefix[-1] // self.prefix[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
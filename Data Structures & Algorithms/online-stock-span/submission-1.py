class StockSpanner:

    def __init__(self):
        self.stock_spanner = []
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        if len(self.stack) == 1:
            self.stock_spanner.append(1)
            return 1
        i = len(self.stack) - 1
        count = 0
        while i >= 0:
            if self.stack[i] > price:
                self.stock_spanner.append(count)
                return count
            else:
                i -= 1
                count += 1
        self.stock_spanner.append(count)
        return count



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
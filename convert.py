class Roman(str):

    def to_int(self):
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = ""
        for i in range(len(ints)):
            count = int(self / ints[i])
            result += nums[i] * count
            self -= ints[i] * count
        return result


    def from_int(self):
        input = self.upper()
        nums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        ints = [1000, 500, 100, 50, 10, 5, 1]
        places = []
        for i in range(len(input)):
            c = input[i]
            value = ints[nums.index(c)]
            # If the next place holds a larger number, this value is negative.
            try:
                nextvalue = ints[nums.index(input[i + 1])]
                if nextvalue > value:
                    value *= -1
            except IndexError:
                # there is no next place.
                pass
            places.append(value)
        sum = 0
        for n in places:
            sum += n
        # Easiest test for validity...
        return sum


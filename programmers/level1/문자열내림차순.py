def solution(s):
    sorted_word = sorted(s, key=lambda x: (str.upper, reversor))
    sorted_word.reverse()
    return ''.join(sorted_word)


class reversor:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return other.obj == self.obj

    def __lt__(self, other):
           return other.obj < self.obj

print(solution('Zbcdefg'))

# Useful doc on Python magic methods:
# https://rszalski.github.io/magicmethods/


class Vector:
    def __init__(self, arr=None, size=None):
        self.d = arr if arr is not None else (([0] * size) if size else [])

    @classmethod
    def from_arr(cls, arr):
        return Vector(arr=arr)

    @classmethod
    def from_size(cls, size):
        return Vector(size=size)

    def set(self, arr):
        self.d = arr
        return self

    def get(self):
        return self.d

    def __len__(self):
        return len(self.d)

    def __repr__(self):
        return str(self.d)

    def __getitem__(self, item):
        return self.d[item]

    def __hash__(self):
        return sum(self.d)

    def __setitem__(self, key, value):
        if key >= len(self.d):
            self.d.extend(key+1)
        self[key] = value;
        return None


    def __cmp__(self, other):
        if (sorted(self.d) > sorted(get(other))):
            return 1
        elif (sorted(self.d) == sorted(get(other))):
            return 0
        return -1

    def __neg__(self):
        return Vector([-x for x in self.d])

    def __reversed__(self):
        return Vector(list(reversed(self.d)))

    def __add__(self, other):
        if isinstance(other, int):
            return Vector([x + other for x in self.d])
        elif isinstance(other, Vector):
            return Vector([self.d[i] + other[i] for i in range(len(self))])

    def __sub__(self, other):
        return [item for item in self.d if item not in get(other)]

    def __mul__(self, other):
        return [(item*other) for item in self.d]

    def __xor__(self, other):
        return [item^other for item in self.d]

    def length(self):
        return math.sqrt(sum(x*x for x in self.d))

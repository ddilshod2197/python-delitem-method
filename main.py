class Dictionary:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data.get(key)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __str__(self):
        return str(self.data)


d = Dictionary()
d['a'] = 1
d['b'] = 2
print(d)  # {'a': 1, 'b': 2}

del d['a']
print(d)  # {'b': 2}

try:
    del d['c']
except KeyError:
    print("Key not found")
```

Kodda `__delitem__` metodining ishlashini ko'rish mumkin. U `del` operatori orqali ma'lumotni o'chirish uchun ishlatiladi.

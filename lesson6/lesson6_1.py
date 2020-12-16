class MyDict(dict):
	def get(self, key, default=0):
		return dict.get(self, key, default)

a = dict(a=1, b=2)
b = MyDict(a=3, b=4)

b["c"] = 5
print(b)

print()
print(a.get("v"))
print(b.get("v"))
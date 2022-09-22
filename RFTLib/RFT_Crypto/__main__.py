import Rypto





key=Rypto.Key()

key.setSalt(69)
key.setSeed(69)

print(key.salt)
print(key.seed)

print(key.random.randint(0,10))





"""
@END
"""

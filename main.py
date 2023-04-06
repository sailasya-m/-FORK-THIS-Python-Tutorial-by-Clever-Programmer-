def bigger_guy(a, b):
  if a >= b:
    print(f"{a} is bigger than or equal to {b}")
    return a
  else:
    print(f"{b} is bigger than {a}")
    return b

result = bigger_guy(4, 3)
print(f"The bigger guy is: {result}")

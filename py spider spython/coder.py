def code(Mind, Tired):
    while True:
        if Mind == 0 or Tired == 100:
            print("Take A Rest")
            break
        else:
            Mind -= 1
            Tired += 1

code(100, 0)
print("Code Again")

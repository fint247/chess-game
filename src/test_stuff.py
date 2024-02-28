class Doggy():
    def __init__(self, legs) -> None:
        self.leg = legs



lyst = [Doggy(1),Doggy(5),Doggy(9)]

lyst2 = []

for thing in lyst:
    print(thing.leg)
    lyst2.append(thing)

lyst[1].leg = 2

print(lyst[1].leg)
print(lyst2[1].leg)

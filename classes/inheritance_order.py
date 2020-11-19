class GrandparentA:
    eye_color = 'grey'

class GrandparentB:
    eye_color = 'brown'

class ParentA(GrandparentA):
    pass

class ParentB(GrandparentB):
    eye_color = 'blue'

class ChildA(ParentA, ParentB):
    pass

class ChildB(ParentB, ParentA):
    pass

child_a = ChildA()
child_b = ChildB()

print(f'ChildA eye color: {child_a.eye_color}')
print(f'ChildB eye color: {child_b.eye_color}')
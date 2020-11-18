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
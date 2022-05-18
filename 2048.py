import operator
not_ = operator.not_
import unittest


def shift(A, B, C, D):
    """
    shift all to A direction
    """
    A, B, C, D = [
        A + not_(A)*B + not_(A or B)*C + not_(A or B or C)*D,
        bool(A or 0)*B + (bool(A) ^ bool(B))*C + bool(A and not B and not C  or  not A and B and not C  or  not A and not B and C)*D,
        bool(A and B)*C + bool(A*B*not_(C) or A*not_(B)*C or not_(A)*B*C)*D,
        bool(A and B and C)*D]
    return [A, B, C, D]
# test cases!
class TestShift(unittest.TestCase):
    # test function to test equality of two value
    def test_shift(self):
        self.assertEqual(shift(*[0, 0, 0, 1]), [1, 0, 0, 0])
        self.assertEqual(shift(*[0, 0, 1, 0]), [1, 0, 0, 0])
        self.assertEqual(shift(*[0, 1, 0, 0]), [1, 0, 0, 0])
        self.assertEqual(shift(*[1, 0, 0, 0]), [1, 0, 0, 0])

        self.assertEqual(shift(*[0, 0, 1, 1]), [1, 1, 0, 0])
        self.assertEqual(shift(*[0, 0, 2, 1]), [2, 1, 0, 0])
        self.assertEqual(shift(*[0, 1, 0, 1]), [1, 1, 0, 0])
        self.assertEqual(shift(*[1, 0, 0, 1]), [1, 1, 0, 0])
        self.assertEqual(shift(*[1, 0, 1, 0]), [1, 1, 0, 0])
        self.assertEqual(shift(*[1, 1, 0, 0]), [1, 1, 0, 0])

        self.assertEqual(shift(*[0, 1, 2, 1]), [1, 2, 1, 0])
        self.assertEqual(shift(*[2, 0, 2, 1]), [2, 2, 1, 0])
        self.assertEqual(shift(*[2, 2, 0, 1]), [2, 2, 1, 0])
        self.assertEqual(shift(*[2, 2, 1, 0]), [2, 2, 1, 0])

        self.assertEqual(shift(*[1, 2, 1, 2]), [1, 2, 1, 2])
        self.assertEqual(shift(*[4, 3, 2, 1]), [4, 3, 2, 1])



def merge(A, B, C, D, incr=1):
    # merge and consolidate to A direction
    "perform merge and then left shift"
    """
    []..        M1 iff (A = B) and nonzero
    .[].        M2 iff (A != B) and (B = C) and nonzero
    ..[]        M3 iff ((A = B) or (B != C)) and (C = D) and nonzero. if (A = B) and B is zero then we know that all else is 0. B != C is true only if one is nonzero
    .<-.
    ..<-
    """
    # incr = 0.01
    # !M1 ===> not_((A == B) and B)*B ===> !(A == B)*B + !(B)*B (de Moivre's thm.) ===> (A != B)*B
    A, B, C, D = [
        A + bool((A == B) and A)*incr,
                # if A matches B, we increment
        (A != B) * (B + bool((B == C) and B)*incr)
                # either: a) A and B are different, so nothing had happened.
                # thus we keep B. but if B and C are the same, they further merge
            + (A == B) * (C + bool(((C == D) and D))*incr),
                # if A and B are the same:
                # if they're both 0, then we know that C and D are all zero, so we don't need to check for nonzero
                # anyways we know that C will slide across into the B position
                # if C and D are both the same and nonzero, they will merge and increment
        (A == B)*(C != D) * D + (A != B)*((B == C)*D + (B != C) * (C + bool((C == D) and D)*incr)),
                # if A = B
                #   if C = D: 0
                #   else D
                # else (A != B)
                #   C + (C = D) and D
                #
        bool((A != B) and (B != C) and (C != D))*D
                # D only remains in place if all A, B, C are unique and there are no merging

    ]
    return [A, B, C, D]

class TestMerge(unittest.TestCase):
    # test function to test equality of two value
    # given: everything is left shifted to the max.
    # therefore, if a=0, then b=c=d=0
    # if b=0, then c=d=0
    # if c=0, then d=0
    def test_merge(self):
        self.assertEqual(merge(*[1, 1, 0, 0]), [2, 0, 0, 0])
        self.assertEqual(merge(*[3, 3, 0, 0]), [4, 0, 0, 0])
        self.assertEqual(merge(*[1, 1, 3, 0]), [2, 3, 0, 0])
        self.assertEqual(merge(*[1, 1, 2, 0]), [2, 2, 0, 0])
        self.assertEqual(merge(*[1, 1, 3, 4]), [2, 3, 4, 0])
        self.assertEqual(merge(*[1, 1, 2, 4]), [2, 2, 4, 0])

        self.assertEqual(merge(*[3, 1, 1, 4]), [3, 2, 4, 0])
        self.assertEqual(merge(*[3, 1, 1, 2]), [3, 2, 2, 0])
        self.assertEqual(merge(*[3, 1, 1, 2]), [3, 2, 2, 0])
        self.assertEqual(merge(*[2, 1, 1, 2]), [2, 2, 2, 0])

        self.assertEqual(merge(*[1, 1, 2, 1]), [2, 2, 1, 0])
        self.assertEqual(merge(*[1, 2, 1, 1]), [1, 2, 2, 0])
        self.assertEqual(merge(*[3, 2, 2, 2]), [3, 3, 2, 0])
        self.assertEqual(merge(*[3, 3, 3, 1]), [4, 3, 1, 0])
        self.assertEqual(merge(*[3, 3, 3, 0]), [4, 3, 0, 0])
        self.assertEqual(merge(*[5, 1, 5, 5]), [5, 1, 6, 0])

        self.assertEqual(merge(*[4, 4, 1, 1]), [5, 2, 0, 0])

        self.assertEqual(merge(*[4, 0, 0, 0]), [4, 0, 0, 0])
        self.assertEqual(merge(*[4, 3, 0, 0]), [4, 3, 0, 0])
        self.assertEqual(merge(*[4, 3, 2, 0]), [4, 3, 2, 0])
        self.assertEqual(merge(*[4, 3, 2, 1]), [4, 3, 2, 1])





def step(A, B, C, D):
    A, B, C, D = shift(A, B, C, D)
    return merge(A, B, C, D)
class TestAll(unittest.TestCase):
    def test_all(self):
        self.assertEqual(step(*[0, 0, 2, 2]), [3, 0, 0, 0])


def formatShiftTI(A, B, C, D):
    return f"""
{A}+not({A}){B}+not({A} or {B}){C}+not({A} or {B} or {C}){D},
({A} or 0){B}+({A} xor {B}){C}+((({A} or 0)+({B} or 0)+({C} or 0))=1){D},
({A} and {B}){C}+({A}*{B}*not({C}) or {A}*not({B})*{C} or not({A})*{B}*{C}){D},
({A} and {B} and {C}){D}
""".replace('\n', '')

def formatMergeTI(A, B, C, D):
    return f"""
{A}+(({A}={B}) and {A})I,
({A}!={B})*({B}+(({B}={C}) and {B})I)+({A}={B})*({C}+(({C}={D}) and {D})I),
({A}={B})({C}!={D}){D}+({A}!={B})(({B}={C}){D}+({B}!={C})({C}+(({C}={D}) and {D})I)),
(({A}!={B}) and ({B}!={C}) and ({C}!={D})){D}
""".replace('\n', '')

if __name__ == '__main__':
    print('{'+formatShiftTI('Ans(1)', 'Ans(2)', 'Ans(3)', 'Ans(4)') + ',' +
          formatShiftTI('Ans(5)', 'Ans(6)', 'Ans(7)', 'Ans(8)') + ',' +
          formatShiftTI('Ans(9)', 'Ans(10)', 'Ans(11)', 'Ans(12)') + ',' +
          formatShiftTI('Ans(13)', 'Ans(14)', 'Ans(15)', 'Ans(16)')+'}')
    print('{'+formatMergeTI('Ans(1)', 'Ans(2)', 'Ans(3)', 'Ans(4)') + ',' +
          formatMergeTI('Ans(5)', 'Ans(6)', 'Ans(7)', 'Ans(8)') + ',' +
          formatMergeTI('Ans(9)', 'Ans(10)', 'Ans(11)', 'Ans(12)') + ',' +
          formatMergeTI('Ans(13)', 'Ans(14)', 'Ans(15)', 'Ans(16)')+'}')

import math
import numpy as np
import sympy as sp
x, y, z, r, theta, phi, X, Y, x0, y0 = sp.symbols("x y z r theta phi X Y x0 y0")
# expr = sp.Eq(x + 1,0)

# Write the class Point as outlined in the instructions
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**(1/2)

    def reflect(self, axis):
        if axis == "x":
            return (self.x, -self.y)

        elif axis == "y":
            return (-self.x, self.y)
        else:
            print("error")






class ConicSection:
    """A conic is a plane curve given by a quadratic equation.
   A real (affine) conic is a curve C ⊂ R^2 given by a quadratic equation of the
       form  """
    def __init__(self, A, B, C, D, E, F):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.F = F

    def cartesian(self):
        return self.A * x ** 2 + self.B * x * y + self.C * y ** 2 + self.D * x + self.E * y + self.F


    def algebraic_form(self):
        return sp.Eq(self.cartesian(), 0)

    def homogeneous_form(self):
        expr = self.A * x ** 2 + self.B * x * y + self.C * y ** 2 + self.D * x*z + self.E * y*z + self.F*z**2
        return sp.Eq(expr, 0)

    def small_matrix(self):
        M = sp.Matrix([[self.A, (self.B)/2],
                  [(self.B)/2, self.C]])
        return M

    def delta(self):
        return sp.det(self.small_matrix())

    def classify(self):
        """Returns the classification type of a non-degenerate conic. Must incl
        """
        z = -4* self.delta()
        if z < 0:
            if self.A == self.C and self.B == 0:
                return "Circle"
            else:
                return "Ellipse"

        elif z==0:
            return "Parabola"
        else:
            return "Hyperbola"

    def big_matrix(self):
        M = sp.Matrix([[self.A, (self.B)/2, (self.D)/2],
                       [(self.B)/2, self.C, (self.E)/2],
                       [(self.D)/2, (self.E)/2, self.F]])
        return M

    def is_degenerate(self):
        """Checks if the conic section provided is degenerate or not. Returns Boolean"""
        determinant = sp.det(self.big_matrix())
        if determinant == 0:
            return True
        else:
            return False

    def classify_degen(self):
        """
        Determines the type of degenereate conic
        """
        determinant = self.delta()
        if determinant < 0 :
            return "Two intersecting lines"
        elif determinant == 0 :
            return "Two pararrel lines"
        else:
            return "A single point (degenerate ellipse)"

    @property
    def eccentricity(self):
        h = -sp.sign(np.linalg.det(self.big_matrix()))
        return math.sqrt((2*math.sqrt( (self.A - self.C)**2 + (self.B)**2)) / \
                         ( h*(self.A + self.C) +  (self.A -self.C)**2+ (self.B)**2))
            
    def affine_trans(self, A, q):
        """
        

        Parameters
        ----------
        A : sp.Matrix 2x2
        q : sp.Matrix - vector 2x1

        Returns
        -------
        algebraic form

        """
        p = sp.Matrix([x, y])
        result = A * p + sp.Matrix(q)
        expr = self.cartesian()
        return sp.Eq(expr.subs({x: result[0], y: result[1]}), 0)    
    
    def rotation_expansion(self,radian,s):
        """
        

        Parameters
        ----------
        radian : angle of rotation given in radians
        s : scalar

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        p = sp.Matrix([x, y]) 
        A = [[sp.cos(radian), sp.sin(radian)], 
             [-sp.sin(radian),sp.cos(radian)]]
        M = sp.Matrix(A)
        result = s*M * p
        expr =self.cartesian()
        return expr.subs({x:result[0], y: result[1]})
        




     # def canonical_ellipse(self):
     #    """
     #    Works only for ellipse. Takes an equation in general form and returns the canonical form.
     #    :return:
     #    """
     #    pass




o = ConicSection(1, -1, -1, -1, 1, -1)
print(o.algebraic_form())
print(o.is_degenerate())
print(o.classify())




# y = ConicSection(9,12,4,-54,-36,72)
#
# print(y.is_degenerate())
# # print(y.degen_type())
#
# q = ConicSection(1,0,1,-4,-6,8)
# print(q.algebraic_form())
# print(q.is_degenerate())
# print(q.classify())
# print(q.eccentricity)
#
#
#
#
#
#
# o = ConicSection(5, 6, 7, 1, 1, 1)
# print(o.algebraic_form())
# print(o.is_degenerate())
# print(o.classify())
# print(o.eccentricity)

#
#
# print(o.cartesian_form())
#
# print(sp.factor(3*x**2 -2 *x*y - y**2 -6*x +10*y -9))







### canonical form of conic sections


class Circle:
    """ Circle class. r is for rarius. Default center is the origin of axis.
    """
    def __init__(self, r):
        self.r = r

    def cartesian(self):
        return x**2 + y**2

    def complex_form(self):
        pass

    def algebraic_form(self):
        return sp.Eq(self.cartesian(), (self.r)**2)

    @property
    def circumference(self):
        return 2*math.pi* self.r
    @property
    def area(self):
        return math.pi* (self.r)**2

    def affine_trans(self, A, q):
        """
        Affine transformation of circle. A has to be a sympy matrix.
        Return is not necessarily is a circle, that is it is not an instance of the class Circle
        """
        p = sp.Matrix([x, y])
        result = A * p + sp.Matrix(q)
        expr = self.cartesian()
        return sp.Eq(expr.subs({x: result[0], y: result[1]}), 1)
    


c = Circle(1)
print(c.cartesian())
print(c.algebraic_form())

A = sp.Matrix([[1,1], [-1,1]])
print(c.affine_trans(A,[1,5]))






# expr.subs(x,y)
# print(expr.subs(x,y))
##implicit plot
## ellipsis
### hyperbola
#### parabola
#
# unitcircle = Circle(1)
#
# xcircle = Circle(2, 1, 1)
#
# print(xcircle.algebraic_form())
#
# print(sp.expand(xcircle.algebraic_form()))
#
# print(sp.simplify(sp.sin(x)**2 + sp.cos(x)**2))

class Ellipse:
    """
    the equation of a standard ellipse centered at the origin with width 2a and height 2b is """
    def __init__(self, a, b):
        self.a = a  # a cannot be zero
        self.b = b  # b cannot be zero


    def cartesian(self):
        return x**2 / self.a + y**2 / self.b

    def algebraic_form(self):
        """
        Algebraic form of standard ellipse in cartesian coordinates

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return sp.Eq(self.cartesian(), 1)

    @property
    def linear_eccentricity(self):
        """
          This is the distance from the center to a focus
        """
        if self.a >= self.b :
            return math.sqrt(self.a**2 - self.b**2 )
        else:
            return math.sqrt(self.b**2 - self.a**2 )

    @property
    def eccentricity(self):

        if self.a > self.b:
            return self.linear_eccentricity/self.a

        else:
            return "check again"

    # def rotate(self, radian):
    #     expr = self.cartesian()
    #     substitute = expr.subs({x: x * sp.cos(radian) + y*sp.sin(radian), y: x*sp.cos(radian) - y*sp.sin(radian)})

    def move_center(self, vector):
        '''
        Move the center of the ellipse. argument vector has to be a tuple or a list.
        '''
        expr = self.cartesian()
        expr.subs({x: x + vector[0], y: y+vector[1]})
        return expr.subs({x: x - vector[0], y: y - vector[1]})








# c = Ellipse(2,3)
# print(c.algebraic_form())
# print(c.cartesian())
# print(c.move_center([1,1]))



# expr = c.cartesian()
#
# print(expr.subs({x: X-5,  y: y-5 }))
#
# expr = r * sp.sin(theta)
#
# expr = x**2 +y**2
# polar = expr.subs({ x:r * sp.sin(theta),   y: r*sp.cos(theta)})
# print(polar.trigsimp())






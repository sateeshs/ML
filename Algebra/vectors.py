import math

class VectorOperations(Object):
    "Vector opreration in class"
    
    #Constructor to initialize
    def __init__(self):
        print("vector operations")
    
    def addition(v,w):
        """Add two vectors"""
        return [v_i+w_i for v_i,w_i in zip(v,w)]
        
    def subtraction(v,w):
        return [v_i-w_i for v_i,w_i in zip(v,w)]

    def vector_sum(vectors):
        """Sum of all elements"""
        result=vectors[0]
        for vector in vectors[1:]:
            result = addition(result,vector)
        return result

    def scalar_multiply(c,v):
        """c is number v is vector"""
        return [c* v_i for v_i in v]
    
    def vector_mean(vectors):
        n=len(vectors)
        return scalar_multiply(1/n, vector_sum(vectors))

    def dot(v,w):
        """dot product of two vectos dot product measures how far the vector v extends in the w direction"""
        return sum(v_i * w_i for v_i, w_i in zip(v,w))

    def sum_of_squares(v):
        """v_1*V_1 + ... v_n*v_n"""
        return dot(v,v)
        
    def magnitude(v):
        return math.sqrt(sum_of_squares(v)) #sqrt: Square root 
    
    def squared_distance(v,w):
        """ditance between two vectos"""
        return mat.sqrt(subtraction(v,w))
    
    def distance(v, w):
        return math.sqrt(squared_distance(v,w))

class VectorOperations:
    "Vector opreration in class"
    
    #Constructor to initialize
    def __init__(self):
        print("vector operations")

    def addition(v,w):
        """Add two vectors"""
        return [v_i+w_i for v_i,w_i in zip(v,w)]
import numpy as np

# A renderable represents an object that can be rendered on the screen
#
# it has a transformation matrix that can be processed by a graphics processor,
# and a position, angle, and scale that can be used to calculate the 
# transformation matrix
class Renderable():
    def __init__(self):
        self.transformation_matrix = np.array([[1,0,0],[0,1,0],[0,0,1]]) # access this to get the transformation matrix
        
        # explicit position, angle, scale is required to save on computational time while simulating
        self.__position = np.array([0,0])
        self.__angle = 0
        self.__size = np.array([1,1])
        
    # scale
    def scale(self, scale=1): # scale the object in both axes with respect to origin
        self.scale(self, scale, scale)
        
    def scale(self, scale_x=1, scale_y=1):
        self.transformation_matrix = np.matmul(self.transformation_matrix, np.array([[scale_x,0,0],[0,scale_y,0],[0,0,1]]))
        self.__size[0] *= scale_x
        self.__size[1] *= scale_y

    # rotate
    def rotate(self, angle=0): # rotate the object with respect to origin
        self.transformation_matrix = np.matmul(self.transformation_matrix, np.array([[np.cos(angle), -np.sin(angle), 0],[np.sin(angle), np.cos(angle), 0],[0,0,1]]))
        self.__angle += angle
        
    # translate
    def translate(self, x=0, y=0): # scale the object with respect to origin
        self.transformation_matrix = np.matmul(self.transformation_matrix, np.array([[1,0,x],[0,1,y],[0,0,1]]))
        self.__position += np.array([x,y])
        
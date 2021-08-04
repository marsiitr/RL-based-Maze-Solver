# Import required libraries
from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt

class preprocess:
    # Preprocessing the input image maze to generate 2D matrix
    # Use the following links to generate high-resolution mazes:
    # https://keesiemeijer.github.io/maze-generator/#generate
    # http://www.mazegenerator.net/      

    def __init__(self, s):

        # Open the maze image at location 's' and make grayscale
        # 'convert()' internally uses the NTSC formula:
        # b = 0.299 * r + 0.587 * g + 0.114 * b
        # Get its dimensions
        self.im = Image.open(s).convert('L') 
        self.w, self.h = self.im.size
     
    def generate(self, margin = 0.01, way = None, pix = 1, div = 128):

        # Ensure all pixels with value less than 'div' (default: 128) 
        # are 1 (black) and others are 0 (white)
        binary = self.im.point(lambda p: p < div)

        # Convert to Numpy array
        self.nim = np.array(binary)

        self.reduceMatrix(margin)
        self.invert()
        if way != None:
            self.sharpen(way, margin)
        self.trim(pix)
        self.loc = self.detectOpenings() # Mark the openings
        self.nim[self.loc[2], self.loc[3]] = 1

    def __str__(self):
        # Returns the maze as string of 0s and 1s

        s = ""
        for r in range(self.h):
            for c in range(self.w):
                s += str(self.nim[r, c])
            s += '\n'

        return s

    def reduceMatrix(self, margin = 0.01): 
        # Reduces the size of the matrix by deleting identical and
        # consecutive rows and columns
        # Rows and columns are marked identical using 'rowIdent()' & 'colIdent()' 
        # operations within a margin specified by 'margin' in percent
        # The paramter 'margin' can be a tuple or a list with two float values, 
        # the first one specifying the margin for rows and the second one for columns
        # It can also be a sigle float value specifying the margin for both 
        # rows and columns  
	    # In normal cases the function returns proper plots of input mazes for 
	    # 0.5 to 1 % margin

        t = type(margin) # checking the datatype of 'margin'
        if (t is tuple or t is list): # if 'margin' is list or tuple
            p = self.w * margin[0]
            q = self.h * margin[1]
        else: # if 'margin' is float
            p = self.w * margin
            q = self.h * margin

        def rowIdent(i):
            # Checks if (i)th and (i + 1)th rows of 'nim' are identical 
            # within a margin of p errors
        
            I = self.nim[i]
            I1 = self.nim[i + 1]
            
            c = count = 0
            while(c < self.w):
                if I[c] != I1[c]: count += 1
                c += 1
            
            return True if count <= p else False

        def colIdent(j):
            # Checks if (j)th and (j + 1)th columns of 'nim' are identical
            # within a margin of q errors
            
            r = count = 0
            while(r < self.h):
                if self.nim[r, j] != self.nim[r, j + 1]: count += 1
                r += 1

            return True if count <= q else False

        # Reduce rows
        r = []
        i = x = 0
        while (i < self.h - 1):
            if rowIdent(i): 
                r.append(i)
                x += 1
            i += 1
        self.h -= x
        self.nim = np.delete(self.nim, r, 0) # delete the rows with indices in r

        # Reduce columns
        c = []
        j = x = 0
        while (j < self.w - 1):
            if colIdent(j): 
                c.append(j)
                x += 1
            j += 1
        self.w -= x
        self.nim = np.delete(self.nim, c, 1) # delete the columns with indices in c
        
    def invert(self):
        # Converts the walls to -1 if they are 1
        # Reduce the matrix using 'reduceMatrix()' operation before using this
        # for faster results

        n = np.zeros((self.h, self.w))

        for r in range(self.h):
            for c in range(self.w):
                if self.nim[r, c] == 1: n[r, c] = -1
        self.nim = n

    def show(self, aspect = 1):
        # Shows a pictorial representation of the maze using Matplotlib
        # Aspect defines the height to width ratio of the pixels

        plt.imshow(self.nim, aspect = aspect)
        plt.clim(-1, 1)
        plt.colorbar()
        plt.show()

    def trim(self, pix = 1):
        # Trims the maze by 'pix' pixels (default: 1 px) from all sides

        r = []
        c = []
        for i in range(pix):
            r.append(i)
            c.append(i)
        for i in range(pix, 0, -1):
            r.append(self.h - i)
            c.append(self.w - i)

        self.nim = np.delete(np.delete(self.nim, r, 0), c, 1)
        self.h -= 2 * pix
        self.w -= 2 * pix

    def detectOpenings(self):
        # Detects the openings (start and the end points) in the maze
        # Ought to trim outer whitespaces and reduce the matrix using 'trim()'
        # and 'reduceMatrix()' operation respectively before using this

        count = 0
        l = []

        # Detect opening in first in last row
        for i in range(self.w):
            if self.nim[0, i] == 0: 
                l.append(0)
                l.append(i)
                count += 1
                break

        for i in range(self.w):
            if self.nim[self.h - 1, i] == 0: 
                l.append(self.h - 1)
                l.append(i)
                count += 1
                if count == 2 : return l   
                else: break     

        # Detect opening in the first and last column
        for i in range(self.h):
            if self.nim[i, 0] == 0: 
                l.append(i)
                l.append(0)
                count += 1
                if count == 2 : return l
                else: break

        for i in range(self.h):
            if self.nim[i, self.w -1] == 0: 
                l.append(i)
                l.append(self.w -1)
                count += 1
                if count == 2 : return l

    def sharpen(self, way = 0, margin = 0.01):
        # Reduce the matrix using 'reduceMatrix()' operation before using this
        # for faster results 
        # Ought to invert the matrix using 'invert()' operation before this

        # Calculating the number of black pixels surrounding each pixel
        n = np.zeros((self.h - 2, self.w - 2), int)

        for r in range(1, self.h - 1):
            for c in range(1, self.w - 1):
                n[r - 1, c - 1] = self.nim[r - 1, c - 1] + self.nim[r - 1, c] + self.nim[r - 1, c + 1] + self.nim[r, c - 1] + self.nim[r, c + 1] + self.nim[r + 1, c - 1] + self.nim[r + 1, c] + self.nim[r + 1, c + 1]
        
        def sharpen_round_edge():
            # Removes protuding stray black pixels that exist due to rounded 
            # maze wall endings

            for r in range(1, self.h - 1):
                for c in range(1, self.w - 1):
                    # check if a black pixel is around other 3 black pixels
                    if (n[r - 1, c - 1] == -3 and self.nim[r, c] != 0):
                        # convert to white if the black pixel is surrounded by 3 
                        # black pixels forming a straight line
                        if self.nim[r - 1, c] + self.nim[r - 1, c - 1] + self.nim[r - 1, c + 1] == -3 or self.nim[r + 1, c] + self.nim[r + 1, c + 1] + self.nim[r + 1, c - 1] == -3 or self.nim[r + 1, c + 1] + self.nim[r, c + 1] + self.nim[r - 1, c + 1] == -3 or self.nim[r - 1, c - 1] + self.nim[r, c - 1] + self.nim[r + 1, c - 1] == -3: self.nim[r, c] = 0
        
        def sharpen_corners():
            # Removes protuding stray black pixels at inner corners and
            # white pixels at the outer corners of the walls

            for r in range(1, self.h - 1):
                for c in range(1, self.w - 1):
                    # Check if a black pixel is surrounded by 5 black pixels
                    if (n[r - 1, c - 1] == -5 and self.nim[r, c] != 0):
                        # Convert to white if the black pixel is surrounded by 3 
                        # 'L' forming white pixels
                        if self.nim[r - 1, c] + self.nim[r, c - 1] + self.nim[r - 1, c - 1] == 0 or self.nim[r + 1, c] + self.nim[r, c - 1] + self.nim[r + 1, c - 1] == 0 or self.nim[r + 1, c] + self.nim[r, c + 1] + self.nim[r + 1, c + 1] == 0 or self.nim[r - 1, c] + self.nim[r, c + 1] + self.nim[r - 1, c + 1] == 0: self.nim[r, c] = 0

                    # Check if a white pixel is surrounded by 3 black pixels
                    elif (n[r - 1, c - 1] == -3 and self.nim[r, c] == 0):
                        # Convert to black if the white pixel is surrounded by 3 
                        # 'L' forming black pixels
                        if self.nim[r - 1, c] + self.nim[r, c - 1] + self.nim[r - 1, c - 1] == -3 or self.nim[r + 1, c] + self.nim[r, c - 1] + self.nim[r + 1, c - 1] == -3 or self.nim[r + 1, c] + self.nim[r, c + 1] + self.nim[r + 1, c + 1] == -3 or self.nim[r - 1, c] + self.nim[r, c + 1] + self.nim[r - 1, c + 1] == -3: self.nim[r, c] = -1

                    # Check if a black pixel is surrounded by 6 black pixels
                    elif (n[r - 1, c - 1] == -6 and self.nim[r, c] != 0):
                        # Convert to white if the black pixel is surrounded by 2 
                        # white pixels; one in the same column and other in the same row
                        # as the black pixel
                        if self.nim[r - 1, c] + self.nim[r, c - 1] == 0 or self.nim[r + 1, c] + self.nim[r, c - 1] == 0 or self.nim[r + 1, c] + self.nim[r, c + 1] == 0 or self.nim[r - 1, c] + self.nim[r, c + 1] == 0: self.nim[r, c] = 0
                    
                    # Check if a white pixel is surrounded by 2 black pixels
                    elif (n[r - 1, c - 1] == -2 and self.nim[r, c] == 0):
                        # Convert to black if the white pixel is surrounded by 2 
                        # black pixels; one in the same column and other in the same row
                        # as the white pixel
                        if self.nim[r - 1, c] + self.nim[r, c - 1] == -2 or self.nim[r + 1, c] + self.nim[r, c - 1] == -2 or self.nim[r + 1, c] + self.nim[r, c + 1] == -2 or self.nim[r - 1, c] + self.nim[r, c + 1] == -2: self.nim[r, c] = -1

        if way == 0: 
            sharpen_round_edge()
            sharpen_corners()
        elif way == 1:
            sharpen_round_edge()
        elif way == 2:
            sharpen_corners()
        self.reduceMatrix(margin)

if __name__ == "__main__":
    p = preprocess("F:/New folder/9.png")
    p.generate(margin = 0.004, pix = 0)
    p.show()
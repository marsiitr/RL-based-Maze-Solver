# Image Processing Workflow
#### 1. The program takes the directory location of the maze image as input .

## Input
```
if __name__ == "__main__":
    p = preprocess("F:/New folder/9.png")
    p.generate(margin = 0.004, pix = 0)
    p.show()
```

#### 2. The size of the image is calculated.

#### 3. The image is converted to grayscale and then to a binary matrix with walls as 1 and travel-path as 0.

## [`generate()`](https://github.com/tushdon2/RL-based-Maze-Solver/blob/fbd11ce17a93b9e0d79abbe9c3acc61b46c69b3a/src/ImgPreprocess.py#L21)
_Ensures all pixels with value less than 'div' (default: 128) are 1 (black) and others are 0 (white).It has to be called for processing of the image._
```
def generate(self, margin = 0.01, way = None, pix = 1, div = 128):
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
```

#### 4. The width of maze walls and travel-path can be of several pixels which has to be reduced to 1 pixel. The need for the above operation is to restrict the movement of Agent in forward and backward direction only (if we would have had multiple pixels then the agent would have moved left and right too).

## [`reduceMatrix()`](https://github.com/tushdon2/RL-based-Maze-Solver/blob/fbd11ce17a93b9e0d79abbe9c3acc61b46c69b3a/src/ImgPreprocess.py#L49)
<p align = "center">
<img src = "https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/Images%20and%20Videos/Images/reduceMatrix.png" alt = "reduceMatrix()"><br>fig1 <i>reduceMatrix()</i></p>

_Reduces the size of the matrix by deleting identical and consecutive rows and columns. Rows and columns are marked identical using `rowIdent()` & `colIdent()` operations within a margin specified by **margin** in percent. The paramter **margin** can be a tuple or a list with two float values, the first one specifying the margin for rows and the second one for columns. It can also be a sigle float value specifying the margin for both rows and columns. In normal cases the function returns proper plots of input mazes for  0.5 to 1 % margin._
```
def reduceMatrix(self, margin = 0.01): 
    t = type(margin) 
    if (t is tuple or t is list): 
        p = self.w * margin[0]
        q = self.h * margin[1]
    else: 
        p = self.w * margin
        q = self.h * margin

    def rowIdent(i):
        # Checks if (i)th and (i + 1)th rows of 'nim' are identical within a margin of p errors

        I = self.nim[i]
        I1 = self.nim[i + 1]
        
        c = count = 0
        while(c < self.w):
            if I[c] != I1[c]: count += 1
            c += 1
        
        return True if count <= p else False

    def colIdent(j):
        # Checks if (j)th and (j + 1)th columns of 'nim' are identical within a margin of q errors
        
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
```
#### 5. Convert the 1s in the matrix to -1. This is necessary as in the maze solver code, we have considered the wall pixels to be -1.
   
## [`invert()`](https://github.com/tushdon2/RL-based-Maze-Solver/blob/fbd11ce17a93b9e0d79abbe9c3acc61b46c69b3a/src/ImgPreprocess.py#L116)
_It converts the walls to -1 if they are 1. Reduce the matrix using `reduceMatrix()` operation before using this for faster results._   
```
def invert(self):
    n = np.zeros((self.h, self.w))

    for r in range(self.h):
        for c in range(self.w):
            if self.nim[r, c] == 1: n[r, c] = -1
    self.nim = n
```
#### 6. The sharpen function requires way as a parameter. Depending on the value of the way, the program will decide whether to Sharpen the corners or sharpen the round edges or both.

## [`sharpen()`](https://github.com/tushdon2/RL-based-Maze-Solver/blob/fbd11ce17a93b9e0d79abbe9c3acc61b46c69b3a/src/ImgPreprocess.py#L193)
_Reduce the matrix using `reduceMatrix()` operation before using this for faster results. Ought to invert the matrix using `invert()` operation before this._

* [`sharpen_round_edge()`](https://github.com/tushdon2/RL-based-Maze-Solver/blob/fbd11ce17a93b9e0d79abbe9c3acc61b46c69b3a/src/ImgPreprocess.py#L205) - Removes protuding stray black pixels that exist due to rounded maze wall endings

<p align = "center">
<img src = "https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/Images%20and%20Videos/Images/sharpen_round_edge.png" alt = "sharpen_round_edge()"><br>fig2 <i>sharpen_round_edge()</i></p>

* [`sharpen_corners()`](https://github.com/tushdon2/RL-based-Maze-Solver/blob/fbd11ce17a93b9e0d79abbe9c3acc61b46c69b3a/src/ImgPreprocess.py#L217) - Removes protuding stray black pixels at inner corners and white pixels at the outer corners of the walls

<p align = "center">
<img src = "https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/Images%20and%20Videos/Images/sharpen_corners%20erroneous%20corner%20pixels.png" alt = "sharpen_corners(): Erroneous Corner pixels">
<br>fig3 <i>sharpen_corners(): Erroneous Corner pixels</i> <br></br>
<img src = "https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/Images%20and%20Videos/Images/sharpen_corners%20path-blocking%20pixels.png" alt = "sharpen_corners(): Path-Blocking pixels">
<br>fig4 <i>sharpen_corners(): Path-Blocking pixels</i> <br></br></p>

```
def sharpen(self, way = 0, margin = 0.01):
    # Calculating the number of black pixels surrounding each pixel
    n = np.zeros((self.h - 2, self.w - 2), int)

    for r in range(1, self.h - 1):
        for c in range(1, self.w - 1):
            n[r - 1, c - 1] = self.nim[r - 1, c - 1] + self.nim[r - 1, c] + self.nim[r - 1, c + 1] + self.nim[r, c - 1] + self.nim[r, c + 1] + self.nim[r + 1, c - 1] + self.nim[r + 1, c] + self.nim[r + 1, c + 1]
    
    def sharpen_round_edge():
        for r in range(1, self.h - 1):
            for c in range(1, self.w - 1):
                # check if a black pixel is around other 3 black pixels
                if (n[r - 1, c - 1] == -3 and self.nim[r, c] != 0):
                    # convert to white if the black pixel is surrounded by 3 
                    # black pixels forming a straight line
                    if self.nim[r - 1, c] + self.nim[r - 1, c - 1] + self.nim[r - 1, c + 1] == -3 or self.nim[r + 1, c] + self.nim[r + 1, c + 1] + self.nim[r + 1, c - 1] == -3 or self.nim[r + 1, c + 1] + self.nim[r, c + 1] + self.nim[r - 1, c + 1] == -3 or self.nim[r - 1, c - 1] + self.nim[r, c - 1] + self.nim[r + 1, c - 1] == -3: self.nim[r, c] = 0
    
    def sharpen_corners():
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
```

#### 7. The extra space present on the borders of the image matrix are trimmed by passing the no. of pixels to be deleted.

## [`trim()`](https://github.com/tushdon2/RL-based-Maze-Solver/blob/fbd11ce17a93b9e0d79abbe9c3acc61b46c69b3a/src/ImgPreprocess.py#L137)
_Trims the maze by **pix** pixels (default: 1 px) from all sides._
```
def trim(self, pix = 1):
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
```

#### 8. The openings in the border of the maze are detected, and one of them is defined as starting and other as the ending.
## [`detectOpenings()`](https://github.com/tushdon2/RL-based-Maze-Solver/blob/fbd11ce17a93b9e0d79abbe9c3acc61b46c69b3a/src/ImgPreprocess.py#L153)
_Detects the openings (start and the end points) in the maze. Ought to trim outer whitespaces and reduce the matrix using `trim()` and `reduceMatrix()` operation respectively before using this._
```
def detectOpenings(self):
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

    # Detect opening in the first and last column
    for i in range(self.h):
        if self.nim[i, 0] == 0: 
            l.append(i)
            l.append(0)
            count += 1
            if count == 2 : return l
    
    for i in range(self.h):
        if self.nim[i, self.w -1] == 0: 
            l.append(i)
            l.append(self.w -1)
            count += 1
            if count == 2 : return l
```

#### 9. This [ImgPreprocess.py](https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/src/ImgPreprocess.py) file is then imported by [Maze_Solving_Code.ipynb](https://github.com/tushdon2/RL-based-Maze-Solver/blob/main/src/Maze_Solving_Code.ipynb).
```from ImgPreprocess import preprocess```

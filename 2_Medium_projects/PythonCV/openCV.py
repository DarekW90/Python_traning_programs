import cv2 as cv
import numpy as np
import os
import time

img = np.zeros((600, 900, 3), dtype=np.uint8)
# skies
# open CV przyjmuje B,G,R kolejność

cv.rectangle(img, (0, 0), (900, 500), (255, 255, 85), -1)
# dla prostokąta (img(od X1 do X2), (od Y1 do Y2), (B,G,R),((-1) - wypełnienie))
cv.rectangle(img, (0, 500), (900, 600), (75, 180, 70), -1)

# sun
cv.circle(img, (200, 150), 60, (0, 255, 255), -1)
# dla okręgu (img(pozycja), średnica, (B,G,R))
cv.circle(img, (200, 150), 75, (220, 255, 255), 10)

# *** TREE 1 ***
# tree stem
cv.line(img, (600, 500), (600, 420), (30, 65, 155), 25)
# dla lini ((img,(pozycja X),(Pozycja Y),(B,G,R),(grubość)))

# tree leafs
triangle = np.array([[500, 440], [700, 440], [600, 75]], dtype=np.int32)
cv.fillPoly(img, [triangle], (75, 180, 70))

# *** TREE 2 ***
# tree stem
cv.line(img, (710, 500), (710, 420), (30, 65, 155), 15)
# dla lini ((img,(pozycja X),(Pozycja Y),(B,G,R),(grubość)))

# tree leafs
triangle2 = np.array([[640, 460], [780, 460], [710, 200]], dtype=np.int32)
cv.fillPoly(img, [triangle2], (75, 200, 70))

# text
font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
cv.putText(img, "Python", (120, 490), font, 1.5, (255, 255, 255), 2)


# save
currentTime = time.localtime()
formattedTime = time.strftime("%Y-%m-%d_%H-%M-%S", currentTime)
print(formattedTime)

current_dir = os.path.dirname(os.path.realpath(__file__))
filePath = os.path.join(current_dir, f'tree_{formattedTime}.png')
print(filePath)
cv.imwrite(filePath, img)

cv.imshow('tree', img)

cv.waitKey(0)
cv.destroyAllWindows()

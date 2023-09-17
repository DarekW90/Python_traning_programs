import cv2 as cv
import numpy as np

img = np.zeros((600,900,3), dtype=np.uint8)
#




cv.imshow('tree',img)

cv.waitKey(0)
cv.destroyAllWindows()
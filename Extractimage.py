import cv2
import numpy as np

# load the images
empty = cv2.imread("whiteback.png")
empty=cv2.resize(empty,(224,224))
full = cv2.imread("tempr.jpg")
full=cv2.resize(full,(224,224))
# save color copy for visualization
full_c = full.copy()

# convert to grayscale
empty_g = cv2.cvtColor(empty, cv2.COLOR_BGR2GRAY)
full_g = cv2.cvtColor(full, cv2.COLOR_BGR2GRAY)

# blur to account for small camera movement
# you could try if maybe different values will maybe
# more reliable for broader cases
empty_g = cv2.GaussianBlur(empty_g, (41, 41), 0)
full_g = cv2.GaussianBlur(full_g, (41, 41), 0)

# get the difference between full and empty box
diff = full_g - empty_g
cv2.imwrite("diff.jpg", diff)

# # inverse thresholding to change every pixel above 190
# # to black (that means without the bag)
# _, diff_th = cv2.threshold(diff, 190, 255, 1)
# cv2.imwrite("diff_th.jpg", diff_th)

# # combine the difference image and the inverse threshold
# # will give us just the bag
# bag = cv2.bitwise_and(diff, diff_th, None)
# cv2.imwrite("Just_the_Apple.jpg", bag)

# # threshold to get the mask instead of gray pixels
# _, bag = cv2.threshold(bag, 100, 255, 0)

# # dilate to account for the blurring in the beginning
# kernel = np.ones((15, 15), np.uint8)
# bag = cv2.dilate(bag, kernel, iterations=1)

# # find contours, sort and draw the biggest one
# _, contours, _ = cv2.findContours(bag, cv2.RETR_TREE,
#                                   cv2.CHAIN_APPROX_SIMPLE)
# contours = sorted(contours, key=cv2.contourArea, reverse=True)[:3]
# cv2.drawContours(full_c, [contours[0]], -1, (0, 255, 0), 3)

# # show and save the result
# cv2.imshow("Apple", full_c)
# cv2.imwrite("results.jpg", full_c)
# cv2.waitKey(0)
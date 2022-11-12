import cv2

# print(cv2.__version__)

# img = cv2.imread("image/cat.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("image/cat.jpg")
print(img.shape)

resize_img = cv2.resize(img, dsize=(768 // 2, 432 // 2))
cv2.imwrite("image/resize_cat.jpg", resize_img)
# cv2.putText(
#     img,
#     text="cat !!!",
#     org=(100, 250),
#     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
#     fontScale=5,
#     color=(255, 255, 255),
#     thickness=3,
# )
# cv2.imshow("Image", img)

# cv2.waitKey(1000)

# cv2.imwrite("image/new_cat.jpg", img)

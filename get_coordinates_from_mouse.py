import cv2

image = cv2.imread("image.jpeg")
points_of_interest = []

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'({x}, {y}')
        cv2.circle(image, (x,y), 3, (0,255,255), -1)
        points_of_interest.append([x,y])

cv2.namedWindow("Point Coordinates")

cv2.setMouseCallback("Point Coordinates", click_event)

while True:
    cv2.imshow("Point Coordinates", image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

print(points_of_interest)
cv2.destroyAllWindows()
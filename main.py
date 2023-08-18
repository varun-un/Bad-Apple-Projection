import cv2
import numpy as np

scale_percent = 70 # percent of original size
offset = (549, 279) # offset of the video from top left corner (horizontal, vertical)
number_frames = 6571
image_path='us_county_b_w.png'

def flood_fill(image, x, y, new_color):
    h, w = image.shape[:2]
    mask = np.zeros((h+2, w+2), dtype=np.uint8)
    old_color = image[y, x]
    cv2.floodFill(image, mask, (x, y), new_color, loDiff=(0, 0, 0, 0), upDiff=(0, 0, 0, 0), flags=4)


base_image = cv2.imread(image_path)
image=cv2.imread(image_path)

gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
th1,img_bin = cv2.threshold(gray_scale,150,225,cv2.THRESH_BINARY)

_, labels, stats, centroids = cv2.connectedComponentsWithStats(img_bin, connectivity=4, ltype=cv2.CV_32S)

# add missed counties
centroids = centroids.tolist()
missing_counties = [[923, 477], [951, 566], [944, 580], [1017, 627], [1041, 778], [1094, 594], [1245, 670], [1195, 500], [1226, 527], [1218, 505], [1235, 508], [1298, 517], [1244, 528], [1239, 418], [1289, 441]]
centroids = centroids + missing_counties

print(len(centroids))


# loop over all frames
for i in range(number_frames + 1):

    # insert overlay image
    overlay_path='./init_frames/frame' + str(i) + '.jpg'

    overlay_image = cv2.imread(overlay_path)
    base_image = cv2.imread(image_path)

    # resize overlay to be 70%
    width = int(overlay_image.shape[1] * scale_percent / 100)
    height = int(overlay_image.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(overlay_image, dim, interpolation = cv2.INTER_AREA)

    for x in centroids:
        if x[0] > 0 and x[1] > 0 and base_image[int(x[1]), int(x[0])][0] >= 30:

            if int(x[0]) - offset[0] < width and int(x[1]) - offset[1] < height and int(x[0]) - offset[0] >= 0 and int(x[1]) - offset[1] >= 0:

                r, g, b = resized[int(x[1] - offset[1]), int(x[0] - offset[0])]
                flood_fill(base_image, int(x[0]), int(x[1]), (int(r), int(g), int(b)))
        
    cv2.imwrite('output_frames/frame%d.jpg' % i, base_image)

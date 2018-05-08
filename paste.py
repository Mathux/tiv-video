import cv2
import argparse


CHOICE = ["play", "pause", "fast", "left", "right", "rewind"]
DIC = {}
for x in CHOICE:
    DIC[x] = "icons/" + x + ".png"


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(
        description='Paste an icon in ')
    parser.add_argument("image", help="path of the image")
    parser.add_argument("icon", help="path of the icon",
                        choices=CHOICE)
    parser.add_argument("output", help="path of the output file")
    parser.add_argument('-x', dest='x',
                        help='x offset, default: 25: ',
                        type=int, default=25)
    parser.add_argument('-y', dest='y',
                        help='y offset, default: 25: ',
                        type=int, default=25)

    args = parser.parse_args()
    return args


def paste_icon(image, icon, out, x=50, y=50):
    if icon == -1:
        return
    lim = image
    sim = DIC[icon]
    s_img = cv2.imread(sim, -1)
    l_img = cv2.imread(lim)
    x_offset, y_offset = x, y
    y1, y2 = y_offset, y_offset + s_img.shape[0]
    x1, x2 = x_offset, x_offset + s_img.shape[1]
    alpha_s = s_img[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        l_img[y1:y2, x1:x2, c] = (alpha_s * s_img[:, :, c] +
                                  alpha_l * l_img[y1:y2, x1:x2, c])

    cv2.imwrite(out, l_img)


if __name__ == '__main__':
    args = parse_args()
    paste_icon(args.image, args.icon, args.output, args.x, args.y)

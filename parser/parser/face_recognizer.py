import cv2


face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades
    + "haarcascade_frontalface_default.xml"
)


def found_faces(image_path):
    """
    Found faces on image

    Args:
        * image_path (str): temporary image's path

    Returns:
        * faces (list): coordinates of faces on image
    """
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30),
    )
    return faces

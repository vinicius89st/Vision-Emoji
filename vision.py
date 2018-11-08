import emoji

def detect_faces(path):
    """Detects faces in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = (0, 1, 2, 3, 4, 5)

    my_dict = {}
    person = 1

    for face in faces:
        my_dict[':angry:'] = (likelihood_name[face.anger_likelihood])
        my_dict[':smiley:'] = (likelihood_name[face.joy_likelihood])
        my_dict[':weary:'] = (likelihood_name[face.sorrow_likelihood])
        my_dict[':open_mouth:'] = (likelihood_name[face.surprise_likelihood])
        print(emoji.emojize(max(my_dict, key=my_dict.get), use_aliases=True))

#exemplo de uso
detect_faces("foto.jpg")

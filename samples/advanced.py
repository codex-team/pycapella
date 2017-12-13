from pycapella import Capella

def upload_file_example():
    api = Capella()
    response = api.upload_file("../samples/image.jpg")
    if response:
        print("Success! Image URL is {}".format(response['url']))
    else:
        print("Error!")


def upload_url_example():
    api = Capella()
    response = api.upload_url("https://capella.pics/532117ec-750f-47eb-b4de-6db8c5ae4781")
    if response:
        print("Success! Image URL is {}".format(response['url']))
    else:
        print("Error!")


def upload_file_and_apply_filters(api):
    api.pixelize(150)
    print("Success! Image URL is {}".format(api.get_url()))


def crop_and_resize_image(api):
    api.crop(400, 400)
    api.resize(150, 150)
    print("Success! Image URL is {}".format(api.get_url()))


def crop_resize_and_pixelize_in_one_line(api):
    url = api.pixelize(150).crop(100, 100, 50, 50).resize(1000, 900).pixelize(200).get_url()
    print("Success! Image URL is {}".format(url))


if __name__ == "__main__":
    upload_file_example()
    upload_url_example()

    new_image = Capella()
    response = new_image.upload_file("../samples/image.jpg")
    assert response['success'] == True

    upload_file_and_apply_filters(new_image)
    crop_and_resize_image(new_image)
    crop_resize_and_pixelize_in_one_line(new_image)

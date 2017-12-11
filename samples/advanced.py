from pycapella import CapellaApi


api = CapellaApi({})


def upload_file_example():
    response = api.uploadFile("image.jpg")
    if response:
        print("Success! Image URL is {}".format(response['url']))
    else:
        print("Error!")


def upload_url_example():
    response = api.uploadUrl("https://capella.pics/532117ec-750f-47eb-b4de-6db8c5ae4781")
    if response:
        print("Success! Image URL is {}".format(response['url']))
    else:
        print("Error!")


if __name__ == "__main__":
    upload_file_example()
    upload_url_example()

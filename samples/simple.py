import pycapella

api = pycapella.Capella()

# Save local file 'image.jpg' to the Capella
response = api.upload_file("image.jpg")
assert response['success'] == True
print("Success! Image URL is {}".format(response['url']))

# Save remote image by url to the Capella
response = api.upload_url("https://ifmo.su/public/app/img/products/capella.png")
assert response['success'] == True
print("Success! Image URL is {}".format(response['url']))
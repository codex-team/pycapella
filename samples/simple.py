import pycapella

api = pycapella.CapellaApi({})

# Save local file 'image.jpg' to the Capella
response = api.uploadFile("image.jpg")
assert response['success'] == True
print("Success! Image URL is {}".format(response['url']))

# Save remote image by url to the Capella
response = api.uploadUrl("https://ifmo.su/public/app/img/products/capella.png")
assert response['success'] == True
print("Success! Image URL is {}".format(response['url']))
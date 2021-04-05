import qrcode
import os
from urllib.parse import urlparse
from requests.models import PreparedRequest
import requests.exceptions


# -- Gets the domain and uses it as the image name --------------------
def parse_url(link):
    domain_name = urlparse(f"{link}").netloc
    return '.'.join(domain_name.split('.')[:])


# -- Checks if the entered URL is valid -------------------------------
def validate_URL(url):
    prepared_request = PreparedRequest()
    try:
        if 'http' not in url:
            prepared_request.prepare_url('https://' + url, None)
        else:
            prepared_request.prepare_url(url, None)
        return prepared_request.url
    except requests.exceptions.MissingSchema as e:
        print(e)

# -- Overwrites the default configurations ----------------------------
print("\n-------------------- Configuring QR Image ---------------------")
qr_image = qrcode.QRCode(
    version=1,
    box_size=14,
    border=7
    )

# -- Creates QR image based on specified URL ---------------------------
print("\n-------------------- Creating QR Image ---------------------")
data_url = "https://github.com/rojinebrahimi"

# -- Inputs user's URL -------------------------------------------------
user_url = input("\nEnter the URL in 'http' or 'https' format (leave empty for default URL): ")
if user_url != "" and validate_URL(user_url):
    qr_image.add_data(user_url)
    if 'http' not in user_url:
        image_name = user_url
    else:
        image_name = parse_url(user_url)
else:
    print("\nUsing the default URL...")
    qr_image.add_data(data_url)
    image_name = parse_url(data_url)


# -- Saves the image with the specified configurations ----------------
qr_image.make(fit=True)
created_qr_image = qr_image.make_image(fill='black', back_color='pink')
image_name = image_name + '.png'
created_qr_image.save(image_name)

# -- Checks if the image was actually created -------------------------
current_dir = os.getcwd()
if os.path.exists(f"{current_dir}/{image_name}"):
    print("\nQR Code generated successfully!")
else:
    print("\nQR Code was not generated.")

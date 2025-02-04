import qrcode
from PIL import Image


# link = "https://github.com/home"
# img_name = "GitHub_example.png"
# logo = "github-mark.png"

link = "https://www.linkedin.com"
img_name = "LinkedIn_example.png"
logo = "In-Blue-21.png"


qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)

# Generate QR code image
qr_img = qr.make_image(fill="black", back_color="white").convert("RGB")

# Load the logo image
logo = Image.open(logo)  # Replace with your logo file

# Resize logo with padding
qr_width, qr_height = qr_img.size
logo_size = qr_width // 5  # Resize to 1/5 of QR code width

# Add padding around the logo
padding = logo_size // 6  # Define padding (adjust as needed)
new_logo_size = (logo_size + padding * 2, logo_size + padding * 2)

# Create a white background for the logo
logo_with_padding = Image.new("RGBA", new_logo_size, (255, 255, 255, 255))
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
logo_with_padding.paste(logo, (padding, padding), logo)  # Keep transparency

# Compute position to paste the logo at the center
x = (qr_width - new_logo_size[0]) // 2
y = (qr_height - new_logo_size[1]) // 2

# Paste the logo onto the QR code
qr_img.paste(logo_with_padding, (x, y), logo_with_padding)

# Add white space at the bottom
extra_space = qr_height // 5  # Adjust bottom white space
new_qr_height = qr_height + extra_space
qr_with_space = Image.new("RGB", (qr_width, new_qr_height), "white")
qr_with_space.paste(qr_img, (0, 0))

# Save and show the final QR code
qr_with_space.save(img_name)
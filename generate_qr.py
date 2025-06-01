# generate_qr.py
import qrcode

# URL of your Flask redirector (deployed version if using online)
redirector_url = "https://qr-redirector-2wwg.onrender.com"  # change if hosted online

img = qrcode.make(redirector_url)
img.save("redirect_qr.png")

print(f"QR code saved pointing to {redirector_url}")

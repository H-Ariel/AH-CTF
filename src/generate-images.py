import qrcode
import base64
from PIL import Image, ImageDraw


def text_to_qr(text, filename):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in pixels
        border=4,  # Thickness of the border (boxes)
    )

    qr.add_data(text)
    qr.make(fit=True)

    qr.make_image(fill="black", back_color="white")\
        .resize((400, 400))\
        .save(filename)


def save_as_base64(image_path):
    open(image_path + ".txt", "w").write(base64.b64encode(open(image_path, "rb").read()).decode("utf-8"))


def generate_smile(filename):
    img = Image.new("RGB", (400, 400), "white")
    draw = ImageDraw.Draw(img)
    draw.ellipse((50, 50, 350, 350), fill="white", outline="black", width=5)
    draw.ellipse((120, 120, 170, 170), fill="black")
    draw.ellipse((230, 120, 280, 170), fill="black")
    draw.arc((150, 200, 250, 300), start=0, end=180, fill="black", width=5)
    img.save(filename)


def xor_images(image1_file, image2_file, out_image):
    image1 = Image.open(image1_file)
    image2 = Image.open(image2_file)

    if image1.size != image2.size:
        print("Images must have the same dimensions")
        return

    image1 = image1.convert("RGB")
    image2 = image2.convert("RGB")

    xor_image = Image.new("RGB", image1.size)

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))
            xor_pixel = tuple(c1 ^ c2 for c1, c2 in zip(pixel1, pixel2))
            xor_image.putpixel((x, y), xor_pixel)

    xor_image.save(out_image)


text_to_qr(
    "Congratulations! You've finished the challenge. The iguana reveals its secrets to those who persevere. Remember, LIZARD{L1z@rdM@st3r} is the key to your victory. Stay curious and keep exploring!",
    "flag.png",
)
save_as_base64("flag.png")

generate_smile("smiley.png")
save_as_base64("smiley.png")

text_to_qr(
    "One day, a talented lass or fellow, a special one with face of yellow, will make the Piece of Resistance found from its hiding refuge underground, and with a noble army at the helm, this Master Builder will thwart the Kragle and save the realm, and be the greatest, most interesting, most important person of all times. All this is true because it rhymes.",
    "prophecy_of_vitruvius.png",
)
save_as_base64("prophecy_of_vitruvius.png")


xor_images("flag.png", "smiley.png", "cool_smiley.png")
save_as_base64("cool_smiley.png")

xor_images("flag.png", "prophecy_of_vitruvius.png", "cool_prophecy.png")
save_as_base64("cool_prophecy.png")

xor_images("cool_prophecy.png", "prophecy_of_vitruvius.png", "maybe_flag.png")
save_as_base64("maybe_flag.png")  # this same to flag.png

## pip install image
## pip install qrcode

import qrcode

imagem = qrcode.make("https://www.uol.com.br")
imagem.save("qrcode_uol.png")

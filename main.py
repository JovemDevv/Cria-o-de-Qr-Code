import qrcode

QR_GREEN = (0,255,0)
QR_BLUE = (0,0,128)
QR_CREAM = (245,255,250)


MeusPerfis = {
    'perfil_linkedin': "https://www.linkedin.com/in/ana-caroline-vasconcellos/",
    'perfil_github': "https://www.github.com/JovemDevv/",
    'perfil_twitter': "https://www.twitter.com/carol_crf10/",
    'perfil_instagram': "https://www.instagram.com/anacaroline.vasconcellos/"
}

if __name__ == '__main__':
    cores = [('black', QR_CREAM), ('red',QR_CREAM), (QR_BLUE, QR_CREAM), ('black', QR_GREEN)]
    for i, (meuqrcode, valor) in enumerate(MeusPerfis.items()):
        qr = qrcode.QRCode(None, 
                        qrcode.ERROR_CORRECT_H)
        qr.add_data(valor)
        img = qr.make_image(fill_color=cores[i][0], back_color=cores[i][1])
        img.save(f'img/{meuqrcode}.png')

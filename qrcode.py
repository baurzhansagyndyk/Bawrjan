import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Elbasınıń "Tındık jańarıw" bagdarlaması tärilik kujat. Bul kujatta latın älipbiyine köciw tuwralı naktı mindet koyıldı. Jańa älipbiy jańartıw kaynarı. Älipbiy arkılı ulttık sana küceyet. Älemde bop jatkan jańalıktar osı jazıw arkılı kabıldanat. Sonday-ak bul älipbiy kazak tili töl tuwmısın saktawga mümkindik beret. El bolacagı jas urpak kolında. Latın karpine köciw olardıń bilim men ilim jolındagı izdenisterine jol acat. Bul Kazak Eli cün damıgan otız el katarına kosılıw bagıtındagı iyi kadam. Tınıy jańarıw Kazak Eliniń jarkın bolacagı.')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("aj.jpg")
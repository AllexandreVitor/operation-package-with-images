import cv2

def add_image(img1, img2):
    # Soma duas imagens do mesmo tamanho.
    if img1.shape != img2.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho e número de canais.")
    return cv2.add(img1, img2)

def sub_image(img1, img2):
    # Subtrai imagens do mesmo tamanho.
    if img1.shape != img2.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho e número de canais.")
    return cv2.subtract(img1, img2)
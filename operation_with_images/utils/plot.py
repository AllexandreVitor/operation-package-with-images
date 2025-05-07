import cv2
import matplotlib.pyplot as plt

def plot_image(img1, img2, result):
    # Exibir as duas imagens originais e o resultado da soma lado a lado
    fig, axes = plt.subplots(1, 3, figsize=(10,5))
    ax = axes.ravel()
    ax[0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    ax[0].set_title('Imagem a')
    ax[0].set_axis_off()

    ax[1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    ax[1].set_title('Imagem b')
    ax[1].set_axis_off()

    ax[2].imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    ax[2].set_title('Imagem ab')
    ax[2].set_axis_off()

    plt.tight_layout()
    plt.show()
import cv2
import numpy as np
import matplotlib.pyplot as plt


def indice_rugosidade(imagem_path):
    # Carregar imagem em tons de cinza
    img = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        raise ValueError("Imagem não encontrada ou inválida")

    # Normalizar
    img = img.astype(np.float32) / 255.0

    # Gradientes Sobel
    grad_x = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)

    # Magnitude do gradiente
    grad_mag = np.sqrt(grad_x**2 + grad_y**2)

    # Índice de rugosidade
    rugosidade = np.mean(grad_mag)

    return rugosidade, grad_mag


rug1, grad1 = indice_rugosidade(r"C:\Users\erodr\Downloads\MVP.jpg")
rug2, grad2 = indice_rugosidade(r"C:\Users\erodr\Downloads\XTM.jpg")

print(f"Rugosidade imagem 1: {rug1:.6f}")
print(f"Rugosidade imagem 2: {rug2:.6f}")

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(grad1, cmap="gray")
plt.title("Gradiente – Imagem 1")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(grad2, cmap="gray")
plt.title("Gradiente – Imagem 2")
plt.axis("off")

plt.show()

estoque = {
    "Notebook": 5,
    "Mouse": 12,
    "Teclado": 3,
    "Monitor": 2,
    "Headset": 0
}

removido_headset = estoque.pop("Headset")

removido_webcam = estoque.pop("Webcam", 0)

print(f"Total de Headset: {removido_headset}")

print(estoque)


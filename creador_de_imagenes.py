import os
import requests
from PIL import Image
import io
import datetime
import random

# 🔑 Token de Hugging Face desde los Secrets de GitHub
HF_TOKEN = os.getenv("HF_TOKEN")

# Prompt aleatorio
prompts = [
    "A surreal dreamlike landscape with floating islands",
    "A futuristic cyberpunk city at night full of neon lights",
    "A watercolor painting of a cozy cabin in the forest",
    "A fantasy castle floating in the sky with dragons around",
    "A photorealistic portrait of an astronaut on Mars",
    "A beautiful Japanese garden in spring with cherry blossoms",
    "A futuristic robot drinking coffee in a vintage café",
    "A galaxy inside a glass jar glowing in the dark",
    "A magical library with flying books and candles",
    "An underwater city with glowing jellyfish and corals"
]

prompt = random.choice(prompts)

print(f"✨ Prompt elegido: {prompt}")

# URL del endpoint de Hugging Face (Stable Diffusion)
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# Solicitud a Hugging Face
response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

if response.status_code != 200:
    raise Exception(f"❌ Error {response.status_code}: {response.text}")

# Guardar la imagen
image_bytes = response.content
fecha = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"imagen_{fecha}.png"

with open(filename, "wb") as f:
    f.write(image_bytes)

print(f"✅ Imagen generada y guardada como {filename}")

# Mostrar la imagen (opcional, para debug)
try:
    image = Image.open(io.BytesIO(image_bytes))
    image.show()
except Exception as e:
    print("⚠️ No se pudo mostrar la imagen localmente:", e)

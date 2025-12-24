import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------ Settings ------------------
W = 64
img = np.zeros((W, W), dtype=float)

# ------------------ Draw line x = y ------------------
for x in range(W):
    y = x
    img[y, x] = 1.0

# ------------------ 2D DFT implementation according to definition ------------------
F = np.zeros((W, W), dtype=complex)

for u in range(W):            # horizontal frequency
    for v in range(W):        # vertical frequency
        sum_val = 0 + 0j
        for x in range(W):    # horizontal image coordinate
            for y in range(W): # vertical image coordinate
                f_xy = img[y, x]
                
                angle = -2 * math.pi * (u * x / W + v * y / W)
                sum_val += f_xy * (math.cos(angle) + 1j * math.sin(angle))
        
        F[v, u] = sum_val

# ------------------ Manual calculation of Magnitude and Phase ------------------
magnitude = np.zeros((W, W), dtype=float)
phase = np.zeros((W, W), dtype=float)

for v in range(W):
    for u in range(W):
        Re = F[v, u].real
        Im = F[v, u].imag
        
        # Magnitude = sqrt(Re^2 + Im^2)
        magnitude[v, u] = math.sqrt(Re*Re + Im*Im)
        
        # Phase = atan2(Im, Re) - manual implementation
        if Re > 0:
            phase[v, u] = math.atan(Im / Re)
        elif Re < 0 and Im >= 0:
            phase[v, u] = math.atan(Im / Re) + math.pi
        elif Re < 0 and Im < 0:
            phase[v, u] = math.atan(Im / Re) - math.pi
        elif Re == 0 and Im > 0:
            phase[v, u] = math.pi/2
        elif Re == 0 and Im < 0:
            phase[v, u] = -math.pi/2
        else:
            phase[v, u] = 0.0

# ------------------ Display results ------------------
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray', origin='upper')
plt.title("Original Image (Line: x = y)")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(magnitude, cmap='gray', origin='upper')
plt.title("Magnitude |F(u,v)|")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(phase, cmap='gray', origin='upper')
plt.title("Phase")
plt.axis("off")

plt.tight_layout()
plt.show()

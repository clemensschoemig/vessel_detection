import matplotlib.pyplot as plt
import rasterio

print("hallo github")


with rasterio.open(r"C:\Users\cleme\Desktop\radar_files\suez_cropped_package_use\subset_TC_package_basis_db.tif") as src:
    band = src.read(1)
    print(src.crs, src.shape)

plt.imshow(band, cmap="viridis")
plt.colorbar()
plt.show()
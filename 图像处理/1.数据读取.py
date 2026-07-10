'''
| 格式              | 推荐库           | 返回数组形状            | 是否保留地理信息 | 推荐指数  |
| --------------- | ------------- | ----------------- | -------- | ----- |
| PNG/JPG/BMP     | OpenCV、PIL    | (H,W,C)           | ✗        | ⭐⭐⭐⭐⭐ |
| TIFF            | Rasterio      | (B,H,W)           | ✓        | ⭐⭐⭐⭐⭐ |
| GeoTIFF         | Rasterio      | (B,H,W)           | ✓        | ⭐⭐⭐⭐⭐ |
| IMG             | GDAL          | (B,H,W)           | ✓        | ⭐⭐⭐⭐⭐ |
| ENVI（.hdr+.img） | Spectral、GDAL | (H,W,B) 或 (B,H,W) | ✓        | ⭐⭐⭐⭐⭐ |
| BIL/BSQ/BIP     | GDAL          | (B,H,W)           | ✓        | ⭐⭐⭐⭐☆ |
| JP2             | GDAL          | (B,H,W)           | ✓        | ⭐⭐⭐⭐☆ |
| HDF/HDF5        | h5py、GDAL     | 视数据而定             | 部分支持     | ⭐⭐⭐⭐☆ |
| MAT             | scipy.io、h5py | 原始存储形状            | ✗        | ⭐⭐⭐⭐⭐ |
| NPY/NPZ         | NumPy         | 原始存储形状            | ✗        | ⭐⭐⭐⭐⭐ |
| NetCDF          | netCDF4       | 原始存储形状            | 部分支持     | ⭐⭐⭐⭐☆ |
| CSV/Excel       | pandas        | 表格数据              | ✗        | ⭐⭐⭐⭐☆ |
| RAW             | NumPy         | 需手动指定形状           | ✗        | ⭐⭐⭐☆☆ |
'''
import numpy as np
#opencv

import cv2
#读取图片
img = cv2.imread('test.jpg')
#显示图片
cv2.imshow('image', img)

#PIL
#读取图片
from PIL import Image
img = np.array(Image.open('test.jpg'))

#rasterio
import rasterio
with rasterio.open('test.jpg') as src:
    img = src.read(1)

#GDAL
from osgeo import gdal

dataset = gdal.Open('test.jpg')
img = dataset.ReadAsArray()

#numpy
img = np.fromfile('test.jpg', dtype=np.uint8)
img = np.load('test.npy')

#scipy
from scipy import io as sio

img = sio.loadmat('test.mat')['img']

#h5py
import h5py

f = h5py.File("data.h5","r")

print(f.keys())

img = f["image"][:]


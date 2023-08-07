
import pydicom
from pydicom.data import get_testdata_file
from viewers import pydicom_PIL
import os

dir = 'data'
converted_dir = 'converted'

length = len(os.listdir(dir))

for index, file in enumerate(os.listdir(dir)):
    print(f"{file} {index+1}/{length}")
    ds = pydicom.dcmread(f'{dir}/{file}')
    filename = file.split(".")[0]
    pydicom_PIL.get_PIL_image(ds).save(f"{converted_dir}/{filename}.png")


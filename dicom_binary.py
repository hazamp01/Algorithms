import pydicom as dicom
import PIL # optional
import pandas as pd
import matplotlib.pyplot as plt

# specify your image path
image_path = '/Users/mohanpraveenhazaru/Documents/audit_log/gehc-ai-lf-inference-package/test/input/03.0000002a.dcm'
ds = dicom.dcmread(image_path)
plt.imshow( ds.pixel_array)

plt.show()


import os
import pydicom
from pydicom.data import get_testdata_files


filename ="/Users/mohanpraveenhazaru/Documents/audit_log/gehc-ai-lf-inference-package/test/input/03.0000002a.dcm"
ds = pydicom.dcmread(filename)

new_ds = ds.pixel_array
print new_ds
output = new_ds.astype('int16').tofile("sample.bin")
print (output)



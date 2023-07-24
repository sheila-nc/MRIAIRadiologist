
import dicom2nifti
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import mri_normalizer
from nilearn import plotting

or_dir = "D:/Duke-Breast-Cancer-MRI/manifest-1654812109500/Duke-Breast-Cancer-MRI/Breast_MRI_013/01-01-1990-NA-MRI BREAST BILATERAL WWO CONTRAST W 3D-95246/500.000000-ax dynamic-90045"
or_dir2 = "D:/Duke-Breast-Cancer-MRI/manifest-1654812109500/Duke-Breast-Cancer-MRI/Breast_MRI_013/01-01-1990-NA-MRI BREAST BILATERAL WWO CONTRAST W 3D-95246/500.000000-ax dynamic-90045"
nifti_img = "C:/Users/sheil/OneDrive/Documentos/Uni/Internship CDSS/MRIAIRadiologist/test.nii"

dicom2nifti.dicom_series_to_nifti(or_dir, nifti_img, reorient_nifti=True)

nifti_load = nib.load(nifti_img)

#plotting.plot_img(nifti_load)
#plt.show()
#print(nifti_load.get_fdata())

norm = mri_normalizer.Normalizer()
normalized_img = norm.normalize_z_score(nifti_load, 'nomask', 1)



plotting.plot_img(normalized_img)
plt.show()

#print(normalized_img)
test = normalized_img.get_fdata()
print(test)
plt.imshow(test[:,:,25], cmap='gray')
plt.show()



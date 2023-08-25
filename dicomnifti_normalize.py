
import dicom2nifti
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import mri_normalizer
from nilearn import plotting
import os
import glob

or_dir = "data\\Duke-Breast-Cancer-MRI"
or_dir2 = "D:/Duke-Breast-Cancer-MRI/manifest-1654812109500/Duke-Breast-Cancer-MRI/Breast_MRI_013/01-01-1990-NA-MRI BREAST BILATERAL WWO CONTRAST W 3D-95246/3.000000-ax t1-41554"
nifti_img = "data/savedNifti.nii"


def normalizeNifti(
        dcm_dir: str, 
        save_dir: str
        ):
    """
    @desc: Convert the DICOM image to Nifti and normalize it. Returns the nifti
    image normalized.
    """
    dicom2nifti.dicom_series_to_nifti(dcm_dir, save_dir, reorient_nifti=True)

    nifti_load = nib.load(save_dir)

    norm = mri_normalizer.Normalizer()
    normalized_img = norm.normalizeDICOM(nifti_load, 'nomask', 1)

    return normalized_img


def get_all_patients_normalized(
        dataset_dir: str
        ) -> list:
    """
    @desc: Iterate through all the patients folders and normalize all the DICOM
    images with nifti, save them in a list and return the list of normalized
    Nifti images.
    """

    mri_modality = 't1'
    normalized_list=[]

    patient_id = os.listdir(dataset_dir)[1:]

    for patient in patient_id:
        dcm_dir = os.path.join(dataset_dir, patient,'*',f'*{mri_modality}*')
        dcm_dir = glob.glob(dcm_dir)
        if(dcm_dir!=[]):
            normalized=normalizeNifti(dcm_dir[0], nifti_img)
            normalized_list.append(normalized)
    return normalized_list


normalized_list = get_all_patients_normalized(or_dir)
plotting.plot_img(normalized_list[0])
plt.show()

#print(normalized_img)
#test = normalized_img.get_fdata()
#print(test)
#plt.imshow(test[:,:,25], cmap='gray')
#plt.show()



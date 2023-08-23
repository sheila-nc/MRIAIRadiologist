import pydicom
import SimpleITK as sitk
import sys
import os
import matplotlib.pyplot as plt
from pydicom import dcmread
from pydicom.data import get_testdata_file
import numpy as np
import glob


def imgToArrayMaxMin(
        dcm_dir: str
        ) -> int:
    """
    @desc: read a DICOM image and transforms it into an array. Take max and min 
    from array and returns it.
    """
    reader = sitk.ImageSeriesReader()
    dcm_names = reader.GetGDCMSeriesFileNames(dcm_dir)
    reader.SetFileNames(dcm_names)
    image = reader.Execute()

    img_array = sitk.GetArrayFromImage(image)
    max = np.max(img_array)
    min = np.min(img_array)
    return max,min

def get_all_patients_maxMin(
        dataset_dir: str
        ) -> list:
    """
    @desc: Iterates through all the patients and gets all the max and min pixel 
    values to identify the outliers. It returns the max and min values in lists.
    """
    max_list = []
    min_list = []

    mri_modality = 't1'

    patient_id = os.listdir(dataset_dir)[1:]

    for patient in patient_id:
        dcm_dir = os.path.join(dataset_dir, patient,'*',f'*{mri_modality}*')
        dcm_dir = glob.glob(dcm_dir)
        if(dcm_dir!=[]):
            max, min = imgToArrayMaxMin(dcm_dir[0])
            max_list.append(max)
            min_list.append(min)
    return max_list,min_list

def plotMaxMinPixel():
    max_list, min_list = get_all_patients_maxMin("D:\\Duke-Breast-Cancer-MRI\\manifest-1654812109500\\Duke-Breast-Cancer-MRI")
    plt.title("Max pixel values")
    plt.plot(max_list)
    plt.show()

    plt.title("Min pixel values")
    plt.plot(min_list)
    plt.show()

    max = np.max(max_list)
    mean = np.mean(max_list)

    print(np.max(max_list))
    print(np.mean(max_list))


plotMaxMinPixel()

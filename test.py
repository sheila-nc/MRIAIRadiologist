import pydicom
import SimpleITK as sitk
import sys
import os
import matplotlib.pyplot as plt
from pydicom import dcmread
from pydicom.data import get_testdata_file
import numpy as np

path2 = "C:/Users/sheil/OneDrive/Documentos/Uni/Internship CDSS/MRIAIRadiologist/1-066.dcm"
path = "D:/Duke-Breast-Cancer-MRI/manifest-1654812109500/Duke-Breast-Cancer-MRI/Breast_MRI_001/01-01-1990-NA-MRI BREAST BILATERAL WWO-97538/26.000000-ax t1 tse c-58582"
dir = "D:/Duke-Breast-Cancer-MRI/manifest-1654812109500/Duke-Breast-Cancer-MRI"
path_seg = "d:/Duke-Breast-Cancer-MRI/2D_Breast_and_FGT_MRI_Segmentations/manifest-1654811613950/Duke-Breast-Cancer-MRI/Breast_MRI_002/01-01-1990-NA-MRI BREAST BILATERAL W  WO-51972/300.000000-Segmentation-70895"


def simpleITK_series_reader(path, path2):
    reader = sitk.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(path)
    reader.SetFileNames(dicom_names)

    image = reader.Execute()

    size = image.GetSize()
    print("Image size:", size[0], size[1], size[2])

    print("Writing image:", path2)

    sitk.WriteImage(image, path2)

    if "SITK_NOSHOW" not in os.environ:
        sitk.Show(image, "Dicom Series")


def get_first_img(dir):
    dir_list = os.listdir(dir)
    img_list = []
    for folder in dir_list:
        if folder!= "LICENSE":
            subdir_path = dir + "/" + folder
            subdir_list = os.listdir(subdir_path)
            subdir2_path = subdir_path + "/" + subdir_list[0]
            subdir2_list = os.listdir(subdir2_path)
            subdir3_path = subdir2_path + "/" + subdir2_list[0]
            result = os.listdir(subdir3_path)[0]
            img_list.append(subdir3_path + "/" + result)
    return img_list


def get_patients_names(path_list):
    name_count = {}
    
    for path in path_list:
        dcm_data = pydicom.dcmread(path)
        patient_name = str(dcm_data.PatientName)[0:15].strip()  # Remove leading/trailing whitespaces
        
        # Increment the count for the patient name in the dictionary
        name_count[patient_name] = name_count.get(patient_name, 0) + 1

    non_repeated_names = [name for name, count in name_count.items() if count == 1]
    num_non_repeated_names = len(non_repeated_names)
    
    return num_non_repeated_names


def imgToArrayMaxMin(path):
    reader = sitk.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(path)
    reader.SetFileNames(dicom_names)
    image = reader.Execute()

    img_array = sitk.GetArrayFromImage(image)
    max = np.max(img_array)
    min = np.min(img_array)
    return max,min

def get_all_patients_maxMin(dir):
    dir_list = os.listdir(dir)
    max_list = []
    min_list = []
    for folder in dir_list:
        if folder!= "LICENSE":
            subdir_path = dir + "/" + folder
            subdir_list = os.listdir(subdir_path)
            subdir2_path = subdir_path + "/" + subdir_list[0]
            subdir2_list = os.listdir(subdir2_path)
            subdir3_path = subdir2_path + "/" + subdir2_list[0]
            print(subdir3_path)
            max, min = imgToArrayMaxMin(subdir3_path)
            max_list.append(max)
            min_list.append(min)
    return max_list,min_list



#min and max values from a slice
max_list, min_list = get_all_patients_maxMin(dir)

plt.title("Max pixel values")
plt.plot(max_list)
plt.show()

plt.title("Min pixel values")
plt.plot(min_list)
plt.show()


#with pydicom
dcm_data = pydicom.dcmread("C:/Users/sheil/OneDrive/Documentos/Uni/Internship CDSS/1-37.dcm")

"""
Image representation with matplot
"""
im = dcm_data.pixel_array

#plt.imshow(im, cmap='gray')
#plt.axis('off')
#plt.show()

#img_path_list = get_first_img(dir)
#num_patients = get_patients_names(img_path_list)
#print("Number of patients: " + num_patients)

#image representation with simpleITK
#simpleITK_series_reader(path_seg, path2)




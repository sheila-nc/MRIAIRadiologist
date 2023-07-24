import nibabel as nib
import numpy

class Normalizer(object):
    def __init__(self):
        pass

    def translate_3d_volume(self, nifti_image):
        nifti_image_arr = numpy.asanyarray(nifti_image.dataobj)
        min_pixel_value = numpy.min(nifti_image_arr)
        nifti_image_arr = nifti_image_arr + abs(min_pixel_value)
        translated = nib.Nifti1Image(nifti_image_arr, nifti_image.affine,\
                                                            nifti_image.header)
        return translated

    def scale_3d_volume(self, nifti_image, scaled_value):
        nifti_image_arr = numpy.asanyarray(nifti_image.dataobj)
        nifti_image_arr = nifti_image_arr * scaled_value
        scaled_nifti_image = nib.Nifti1Image(nifti_image_arr,\
                                        nifti_image.affine, nifti_image.header)
        return scaled_nifti_image

    def normalize_z_score(self, nifti_image, mask, scaled_value):
        import pdb; pdb.set_trace()
        img_data = numpy.asanyarray(nifti_image.dataobj)
        if mask == 'nomask':
            mask_data = img_data
        logical_mask = mask_data == 1
        mean = img_data[logical_mask].mean() 
        std = img_data[logical_mask].std() 
        normalized = nib.Nifti1Image((img_data - mean) / std, \
                                            nifti_image.affine, nifti_image.header)
        normalized = self.translate_3d_volume(normalized)
        normalized = self.scale_3d_volume(normalized, scaled_value)
        return normalized
    



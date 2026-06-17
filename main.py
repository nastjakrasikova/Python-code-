import numpy as np
import pandas as pd
import nibabel as nib
import statsmodels.api as sm
import statsmodels.formula.api as smf

# import segmentation and parcellation
def run_vascular_analysis():
vessel_nii = nib.load("subject1_session1_refined_vessels.nii.gz")
    vessel_mask = vessel_nii.get_fdata()
# load the Schaefer 2018 Local-Global Atlas
atlas_nii = nib.load("Schaefer2018_LocalGlobal_Parcellation_MNI152_1mm.nii.gz")
    atlas_data = atlas_nii.get_fdata()
# align for the same matrix space 
assert vessel_mask.shape == atlas_data.shape
# region of interests and their labels 
roi_labels = {
        "Precuneus": list(range(389, 411)),          # Labels 389–410
        "Parahippocampal_Gyrus": list(range(479, 485)), # Labels 479–484
        "Superior_Frontal_Gyrus": list(range(921, 926)) # Labels 921–925
    }


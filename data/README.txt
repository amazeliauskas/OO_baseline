# Description of files in data folder. Files with ALICE use |y|<0.8, ATLAS |y|<2.5, CMS |y|<1.0

# Experimental data
ALICE_5.02TeV_hadron_spectra.csv
# This is 5.02TeV hadron yield from 10.17182/hepdata.86210.v1/t4. See the header for data structure.

# FF uncertainties in 5.02TeV spectra
ALICE_pp_FF_5020GeV_CT18ANLO_BKK_SCALE_spectra.txt
ALICE_pp_FF_5020GeV_CT18ANLO_NNFF11_HadronSum_nlo_FF_spectra.txt
ALICE_pp_FF_5020GeV_CT18ANLO_NPC23_CHHAsum_nlo_FF_spectra.txt
# These are spectra of scale (for BKK) and FF uncertainties in 5.02TeV spectra. No PDF uncertainties. pT is chosen by 3-point Gauss-Legendre quadrature

# Binned spectra.
int_ALICE_pp_FF_ref_5020GeV_CT18ANLO_BKK_spectra.txt
int_ALICE_pp_FF_ref_5020GeV_CT18ANLO_NNFF11_HadronSum_nlo_spectra.txt
int_ALICE_pp_FF_ref_5020GeV_CT18ANLO_NPC23_CHHAsum_nlo_spectra.txt
#  This is integrated spectra in each bin matched to the experiment. Note that uncertainties are also integrated. Technically one should first integrate spectra for each scale and FF variation and then compute uncertainties. However the spectra are quite smooth and it is not likely to change the end band significantly and we ignore this difference. File structure is
# pTmin pTmax pTc LO LO_scale_min LO_scale_max LO_FF_min LO_FF_max NLO NLO_scale_min NLO_scale_max NLO_FF_min NLO_FF_max

# Ne/O ratio
ALICE_NeNe_PDF_5360GeV_EPPS21nlo_CT18Anlo_Ne20_EPPS21nlo_CT18Anlo_O16_BKK_PDF_ONe_ratio.txt
# This is the ratio of hadron spectra in NeNe and OO collisions with scale and 68% PDF uncertainties.
# The data structure is
# pT	yLOcentral	yLOminus	yLOplus	yPDFLOminus	yPDFLOplus	yNLOcentral	yNLOminus	yNLOplus	yPDFNLOminus	yPDFNLOplus

# FF uncertainties
ALICE_OO_FF_err_5360GeV_CT18ANLO_NNFF11_HadronSum_nlo_FF_spectra.txt
ALICE_OO_FF_err_5360GeV_CT18ANLO_NPC23_CHHAsum_nlo_FF_spectra.txt
ALICE_OO_FF_err_5360GeV_EPPS21nlo_CT18Anlo_O16_NNFF11_HadronSum_nlo_FF_spectra.txt
ALICE_OO_FF_err_5360GeV_EPPS21nlo_CT18Anlo_O16_NPC23_CHHAsum_nlo_FF_spectra.txt
# These are hadro spectra in pp and OO collisions with scale and 68% FF confidence intervals. 
# pT	yLOcentral	yLOminus	yLOplus	yPDFLOminus	yPDFLOplus	yNLOcentral	yNLOminus	yNLOplus	yPDFNLOminus	yPDFNLOplus


# FF uncertainties in RAA
ALICE_OO_FF_err_5360GeV_EPPS21nlo_CT18Anlo_O16_CT18ANLO_NNFF11_HadronSum_nlo_FF_ratio.txt
ALICE_OO_FF_err_5360GeV_EPPS21nlo_CT18Anlo_O16_CT18ANLO_NPC23_CHHAsum_nlo_FF_ratio.txt
# these are hadron RAA with scale and FF uncertainties.
# pT	yLOcentral	yLOminus	yLOplus	yPDFLOminus	yPDFLOplus	yNLOcentral	yNLOminus	yNLOplus	yPDFNLOminus	yPDFNLOplus

# PDF uncertainties in spectra 
ALICE_OO_PDF_5360GeV_CT18ANLO_BKK_PDF_spectra.txt
ALICE_OO_PDF_5360GeV_EPPS21nlo_CT18Anlo_O16_BKK_PDF_spectra.txt
ALICE_OO_PDF_5360GeV_nNNPDF30_nlo_as_0118_p_BKK_PDF_spectra.txt
ALICE_OO_PDF_5360GeV_nNNPDF30_nlo_as_0118_A16_Z8_BKK_PDF_spectra.txt
ALICE_OO_PDF_5360GeV_TUJU21_nlo_1_1_BKK_PDF_spectra.txt
ALICE_OO_PDF_5360GeV_TUJU21_nlo_16_8_BKK_PDF_spectra.txt
# these are hadron OO and pp spectra at 5.36 TeV with scale and PDF uncertainties
# pT	yLOcentral	yLOminus	yLOplus	yPDFLOminus	yPDFLOplus	yNLOcentral	yNLOminus	yNLOplus	yPDFNLOminus	yPDFNLOplus


# PDF uncertainties in RAA
ALICE_OO_PDF_5360GeV_EPPS21nlo_CT18Anlo_O16_CT18ANLO_BKK_PDF_ratio.txt
ALICE_OO_PDF_5360GeV_nNNPDF30_nlo_as_0118_A16_Z8_nNNPDF30_nlo_as_0118_p_BKK_PDF_ratio.txt
ALICE_OO_PDF_5360GeV_TUJU21_nlo_16_8_TUJU21_nlo_1_1_BKK_PDF_ratio.txt
# these are hadron OO/pp RAA at 5.36 TeV with PDF uncertainties
# pT	yLOcentral	yLOminus	yLOplus	yPDFLOminus	yPDFLOplus	yNLOcentral	yNLOminus	yNLOplus	yPDFNLOminus	yPDFNLOplu

# Scale uncertainties in pi0 RAA
ALICE_OO_pi0_SCALE_5360GeV_EPPS21nlo_CT18Anlo_O16_CT18ANLO_NPC23_PI0_nlo_SCALE_ratio.txt
# these are pi0 RAA with only scale uncertainties.
# pT	yLO	yLOminus	yLOplus	yNLO	yNLOminus	yNLOplus

# |y|<2.5 results 
ATLAS_OO_PDF_5360GeV_EPPS21nlo_CT18Anlo_O16_CT18ANLO_BKK_PDF_ratio.txt

# |y|<1.0 results
CMS_OO_PDF_5360GeV_EPPS21nlo_CT18Anlo_O16_CT18ANLO_BKK_PDF_ratio.txt



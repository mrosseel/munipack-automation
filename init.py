#### DO NOT TOUCH ####
import multiprocessing
import numpy as np

aperture_range = np.arange(0.2, 10, 0.2)
all = range(1, 10000)
thou = range(1, 1000)
selection = [58, 137, 138, 886]
selection2 = (1, 2, 3, 73, 138, 143, 264, 2675, 1045, 847, 1193)
custom_muniwin = range(5776, 10000)
# custom_charts = range(1,5776)
custom_charts = range(1, 2164)
wwcra_candidates = [6314,
                    6291,
                    5978,
                    5745,
                    5557,
                    5430,
                    4962,
                    3368,
                    2659,
                    2535,
                    2058,
                    1870,
                    1858,
                    1636,
                    1619,
                    1324,
                    464,
                    454,
                    441,
                    440,
                    435,
                    427,
                    420,
                    378,
                    363,
                    313,
                    290,
                    277,
                    227,
                    225,
                    205,
                    160,
                    159,
                    141,
                    132,
                    117,
                    111,
                    107,
                    1
                    ]
wwcra_certain_candidates = [6314,
                            5978,
                            5557,
                            5430,
                            4962,
                            3368,
                            2535,
                            2058,
                            1870,
                            1636,
                            464,
                            441,
                            427,
                            363,
                            290,
                            277,
                            227,
                            205,
                            141]

#### SETTINGS for DO_MUNIWIN.PY ####

codedir = './'
#basedir = codedir + 'inputfiles/RTGru/'
# basedir = codedir + 'inputfiles/WWCrA_allflat/'
basedir = codedir + 'inputfiles/testing/'
#basedir =  codedir + 'inputfiles/WWCrA2015/'
#basedir =  codedir + 'inputfiles/WWCrA_bigger/'
star_list = all
nr_threads = multiprocessing.cpu_count()*2

do_convert_fits=0
do_photometry=0
do_match=0
do_munifind=0
do_lightcurve=0
do_lightcurve_resume=0
do_pos=0
do_pos_resume=0
do_calibrate=1
do_ml=0
do_charting=1
do_phase_diagram=1
do_field_charts=1
do_reporting=0


#### DO NOT TOUCH ####
# standard directories
fitsdir = basedir + "fits/"
convfitsdir = basedir + "converted_fits/"
photometrydir = basedir + "photometry/"
matchedphotometrydir = basedir + "matched_photometry/"
resultdir = basedir + "results/"
lightcurvedir = resultdir + "lightcurves/"
posdir = resultdir + "positions/"
worldposdir = resultdir + "world_positions/"
chartsdir = resultdir + "charts/"
phasedir = resultdir + "phasediagrams/"
vsxcatalogdir = codedir + "vsx_catalog.bin"
aavsoreportsdir = resultdir + "aavso_reports/"
fieldchartsdirs = resultdir + "field_charts/"
#### DO NOT TOUCH ####

### CALIBRATION ###
reference_header = basedir + 'new-image.fits'
ra_deg = 271.4032917
dec_deg = -43.8326111
sitelat = '-22 57 10'
sitelong = '-68 10 49'
sitealt= 350 # TODO WRONG !!!!
### CALIBRATION

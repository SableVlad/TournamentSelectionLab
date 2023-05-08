import time
from multiprocessing import Pool
from constants import fh_pm, fhd_pm, fx2_pm, env, PM
from functions import *
from tournament import DuplicatesTournament, NoDuplicatesTournament
from plots import *
from program import main, main_noise
from excel import save_avg_to_excel


release_sm = [DuplicatesTournament, NoDuplicatesTournament]
testing_sm = [DuplicatesTournament, NoDuplicatesTournament]
selection_methods = testing_sm if env == 'test' else release_sm
release_functions = [
    (FH(), selection_methods, 'FH', N, 100, 0),
]
"""
    (FH(), selection_methods, 'FH_pm', N, 100, fh_pm),
    (FHD(10), selection_methods, 'FHD_10', N, 100, 0),
    (FHD(10), selection_methods, 'FHD_10_pm', N, 100, fhd_pm),
    (FHD(150), selection_methods, 'FHD_150', N, 100, 0),
    (Fx(0, 10.23), selection_methods, 'Fx', N, 10, 0),
    (Fx2(0, 10.23), selection_methods, 'Fx2', N, 10, 0),
    (Fx2(0, 10.23), selection_methods, 'Fx2_pm', N, 10, fx2_pm),
    (Fx4(0, 10.23), selection_methods, 'Fx4', N, 10, 0),
    (F5122subx2(), selection_methods, '5_12_sub_X2', N, 10, 0),
    (F5122subx2(), selection_methods, '5_12_sub_X2_pm', N, 10, fx2_pm),
    (F5124subx4(), selection_methods, '5_12_sub_X4', N, 10, 0)
]
"""
test_functions = [
    #(Fconst(), selection_methods, 'FConst', N, 100, 0),
    #(Fe025x(), selection_methods, 'Fe025x', N, 10, 0),
    #(Fe025x(), selection_methods, 'Fe025x_pm', N, 10, PM),
    #(Fe1x(), selection_methods, 'Fe1x', N, 10, 0),
    #(Fe1x(), selection_methods, 'Fe1x_pm', N, 10, PM),
    (Fe2x(), selection_methods, 'Fe2x', N, 10, 0),
    #(Fe2x(), selection_methods, 'Fe2x_pm', N, 10, PM),
]
"""
test_functions = [
    (FH(), selection_methods, 'FH', N, 100, 0),
    (FH(), selection_methods, 'FH_pm', N, 100, PM/10),
    (FHD(10), selection_methods, 'FHD_10', N, 100, 0),
    (FHD(10), selection_methods, 'FHD_10_pm', N, 100, PM/10),
    (Fx2(0, 10.23), selection_methods, 'Fx2', N, 10, 0),
    (Fx2(0, 10.23), selection_methods, 'Fx2_pm', N, 10, PM),    
]
"""
functions = test_functions if env == 'test' else release_functions


if __name__ == '__main__':
    p_start = time.time()
    results = {}
    noise_results = {}

    with Pool(12) as p:
        res_list = p.starmap(main, functions)

        for res in res_list:
            results[res[0]] = res[1]

        noise_results['FConst'] = main_noise(selection_methods)
        save_avg_to_excel(results, noise_results)

    p_end = time.time()
    print('Program calculation (in sec.): ' + str((p_end - p_start)))
#%%

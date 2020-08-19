#!/usr/bin/env python
u"""
test_download_and_read.py (08/2020)
"""
import warnings
import pytest
import icesat2_toolkit.utilities
from icesat2_toolkit.read_ICESat2_ATL03 import read_HDF5_ATL03
from icesat2_toolkit.read_ICESat2_ATL06 import read_HDF5_ATL06
from icesat2_toolkit.read_ICESat2_ATL07 import read_HDF5_ATL07
from icesat2_toolkit.read_ICESat2_ATL12 import read_HDF5_ATL12

#-- PURPOSE: Download an ATL03 file from NSIDC and check that read program runs
def test_ATL03_download_and_read(username,password):
    HOST = ['https://n5eil01u.ecs.nsidc.org','ATLAS','ATL03.003','2018.10.14',
        'ATL03_20181014000347_02350101_003_01.h5']
    icesat2_toolkit.utilities.from_nsidc(HOST,username=username,
        password=password,local=HOST[-1],verbose=True)
    IS2_atl03_mds,IS2_atl03_attrs,IS2_atl03_beams = read_HDF5_ATL03(HOST[-1],
        ATTRIBUTES=False, VERBOSE=True)
    assert all(gtx in IS2_atl03_mds.keys() for gtx in IS2_atl03_beams)

#-- PURPOSE: Download an ATL06 file from NSIDC and check that read program runs
def test_ATL06_download_and_read(username,password):
    HOST = ['https://n5eil01u.ecs.nsidc.org','ATLAS','ATL06.003','2018.10.14',
        'ATL06_20181014001049_02350102_003_01.h5']
    icesat2_toolkit.utilities.from_nsidc(HOST,username=username,
        password=password,local=HOST[-1],verbose=True)
    IS2_atl06_mds,IS2_atl06_attrs,IS2_atl06_beams = read_HDF5_ATL06(HOST[-1],
        ATTRIBUTES=False, HISTOGRAM=False, QUALITY=False, VERBOSE=True)
    assert all(gtx in IS2_atl06_mds.keys() for gtx in IS2_atl06_beams)

#-- PURPOSE: Download an ATL07 file from NSIDC and check that read program runs
def test_ATL07_download_and_read(username,password):
    HOST = ['https://n5eil01u.ecs.nsidc.org','ATLAS','ATL07.003','2018.10.14',
        'ATL07-01_20181014000347_02350101_003_02.h5']
    icesat2_toolkit.utilities.from_nsidc(HOST,username=username,
        password=password,local=HOST[-1],verbose=True)
    IS2_ATL07_mds,IS2_ATL07_attrs,IS2_ATL07_beams = read_HDF5_ATL07(HOST[-1],
        ATTRIBUTES=False, VERBOSE=True)
    assert all(gtx in IS2_ATL07_mds.keys() for gtx in IS2_ATL07_beams)

#-- PURPOSE: Download an ATL12 file from NSIDC and check that read program runs
def test_ATL12_download_and_read(username,password):
    HOST = ['https://n5eil01u.ecs.nsidc.org','ATLAS','ATL12.003','2018.10.14',
        'ATL12_20181014031222_02370101_003_01.h5']
    icesat2_toolkit.utilities.from_nsidc(HOST,username=username,
        password=password,local=HOST[-1],verbose=True)
    IS2_ATL12_mds,IS2_ATL12_attrs,IS2_ATL12_beams = read_HDF5_ATL12(HOST[-1],
        ATTRIBUTES=False, VERBOSE=True)
    assert all(gtx in IS2_ATL12_mds.keys() for gtx in IS2_ATL12_beams)

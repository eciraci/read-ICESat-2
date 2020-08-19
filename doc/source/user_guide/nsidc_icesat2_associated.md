nsidc_icesat2_associated.py
=================================

 - Downloads an ICESat-2 product associated with an input file of a different product.  

#### Calling Sequence
```bash
python nsidc_icesat2_associated.py --user=<username> --directory=<outgoing> \
	--product=ATL03 --mode=0o775 ATL06_files
```
[Source code](https://github.com/tsutterley/read-ICESat-2/blob/master/scripts/nsidc_icesat2_associated.py)  

#### Command Line Options
 - `-U X`, `--user=X`: username for NASA Earthdata Login  
 - `-N X`, `--netrc=X`: path to .netrc file for alternative authentication  
 - `-D X`, `--directory`: local working directory for receiving data  
 - `--product=X`: ICESat-2 data product to download  
 - `--auxiliary`: Sync ICESat-2 auxiliary files for each HDF5 file  
 - `-M X`, `--mode=X`: Local permissions mode of the directories and files synced  

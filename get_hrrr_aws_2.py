import subprocess
from datetime import datetime, timedelta

header = "https://noaa-hrrr-bdp-pds.s3.amazonaws.com/"
time = datetime(2016,8,30,0)
d = time.strftime("%Y%m%d")
subprocess.call(['mkdir', '-p', d])
for h in range(19):
    f = f'hrrr.t12z.wrfprsf{h:02d}.grib2'
    # f = f'hrrr.t{h:02d}z.wrfprsf00.grib2'
    # print(f)
    subprocess.call(['wget', f'{header}hrrr.{d}/conus/{f}'])
    subprocess.call(['mv',f, d])
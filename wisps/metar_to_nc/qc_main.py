import qc_clouds
import qc_precip   
import qc_temp     
import qc_winds
#import qc_winds_mod
import qc_main     
import qc_pressure 
import qc_weather
import qc_error
import pdb
import time


def qc(station_dict):
    all_errors = []

    print "starting QC"
    station_list = station_dict.values()

    start = time.time()
    print "QC Temperature"
    all_errors += qc_temp.qc_temp(station_list)
    end = time.time()
    print end-start

    start = time.time()
    print "QC Pressure"
    all_errors +=  qc_pressure.qc_pressure(station_list)
    end = time.time()
    print end-start

    start = time.time()
    print "QC Clouds"
    all_errors += qc_clouds.qc_clouds(station_list)
    end = time.time()
    print end-start

    start = time.time()
    print "QC Winds"
    all_errors += qc_winds.qc_winds(station_list)
    end = time.time()
    print end-start

    start = time.time()
    print "QC Weather"
    all_errors += qc_weather.qc_weather(station_list)
    end = time.time()
    print end-start

    start = time.time()
    print "QC precip"
    all_errors += qc_precip.qc_precip(station_list)
    end = time.time()
    print end-start

    all_errors += qc_error.all_qc_errors

    type(all_errors)

    flatten = lambda l: [item for sublist in l for item in sublist]
    #all_errors = flatten(all_errors)
    tmp_errors = []
    for i in all_errors:
        if i is not None:
            try:
                if len(i) > 0:
                    tmp_errors += i
            except :
                tmp_errors.append(i)

    all_errors = tmp_errors

    qc_error.stats(all_errors,50)
    all_errors = sorted(all_errors, key=lambda err: err.station_name)
    with open('all_errors', 'w') as mmk:
        mmk.write(str(all_errors))

    pdb.set_trace()


    return station_dict

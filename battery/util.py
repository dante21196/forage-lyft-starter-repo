def battery_service_year(cdate,duration):
    ndate=cdate.replace(year=cdate.year+duration)
    return ndate
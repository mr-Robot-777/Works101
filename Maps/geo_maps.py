import pygeoip

gip = pygeoip.GeoIP(GeoLiteCity.dat)
res=gip.record_by_addr('enter ip:')
for key,val in res.items():
    print('%s : %s' % (key, val))

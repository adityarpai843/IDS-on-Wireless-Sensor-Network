from Ping import Ping

ip=['aaaa::212:7402:2:202','aaaa::212:7403:3:303','aaaa::212:7404:4:404','aaaa::212:7405:5:505','aaaa::212:7406:6:606']
print('Ping',len(ip),'nodes')
p=Ping()
p.ping(ip)
p.toCSV(ip,'Cooja 4x4 Square grid','Normal','Normal')


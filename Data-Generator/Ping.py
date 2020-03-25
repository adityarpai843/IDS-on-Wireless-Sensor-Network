import subprocess
import csv

class Ping:

    count = '200'
    time = '5'

    def __init__(self,count='1',time='1'):
        
        self.count = time
        self.time = time

    def ping(self,ip):
        for node in ip:
            print('Ping',node)
            proc = subprocess.Popen(['ping6','-c',self.count,'-i',self.time,node],stdout=subprocess.PIPE)
            output = proc.communicate()[0]
            print(output.decode('utf-8'))
            f = open(node,'w')
            f.write(output.decode('utf-8'))
            f.close()    

    def toCSV(self,ip,experiment_name,label,label2):
        fields = ['Experiment','node_id','label','label2','loss']
        data = []
        print('code to csv')
        for node in ip:
            packstats = []
            file_txt = open(node,'r')
            for line in file_txt:
                if line.find('packets transmitted')>=0:
                    packstats = line.split(',')
                    break
            print(packstats)
            file_csv = open('stats_per_node.csv','w')
            csv_writer = csv.writer(file_csv)
            csv_writer.writerow(fields)
            if (len(packstats) == 5):
                loss = packstats[3].split(' ')[1]
            else:
                loss = packstats[2].split(' ')[1]
            print('Final Loss is',loss)
            data = data+[[experiment_name,node,label,label2,loss]]
            print(data)
        csv_writer.writerows(data)
        file_csv.close()



  



         

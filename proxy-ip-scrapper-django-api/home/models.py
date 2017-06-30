from django.db import models


class IPdata(models.Model):

    ip_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, primary_key=True)
    country = models.CharField(max_length=100)
    port_no = models.PositiveIntegerField()
    anonymity = models.CharField(max_length=50, default="Low")
    HTTPS = models.CharField(max_length=50, default="Not Specified")
    last_updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):

        return self.ip_address + ' , ' + self.country + ' , ' + str(self.port_no) + ' , ' + self.anonymity + ' , ' \
               + str(self.last_updated) + ' , ' + self.HTTPS


#        if self.last_updated != None:
#            return self.ip_address + ' , ' +  self.country + ' , ' +  str(self.port_no) + ' , ' +  self.anonymity + ' , '\
#            +  str(self.last_updated) + ' , ' +  self.HTTPS
#        else:
#            return self.ip_address + ' , ' + self.country + ' , ' + str(self.port_no) + ' , ' + self.anonymity + ' , ' \
#                    + ' , ' + self.HTTPS + " ,Object is not saved"
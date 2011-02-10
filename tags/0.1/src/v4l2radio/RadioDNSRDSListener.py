# RadioDNSRDSListener
# Listener class for RDSDecoder which implements basic RadioDNS functionality
#
# Copyright (C) 2010 <andy.buckingham _AT_ thisisglobal.com>
#
# This library is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free 
# Software Foundation; either version 2.1 of the License, or (at your option) 
# any later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT 
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA


__all__ = ["RadioDNSRDSListener"]


from RDSDecoder import RDSDecoderListener
import dns.resolver


class RadioDNSRDSListener(RDSDecoderListener):
    """
    RDSDecoderListener sub-class for monitoring RDS changes that affect
    RadioDNS service resolution
    """
    
    def __init__(self, radio, country = 'gb'):
        
        self.radio = radio
        self.country = country
        

    def on_pi_change(self, pi):
        
        self.__check_radiodns_values()
        

    def on_ecc_change(self, ecc):
        
        self.__check_radiodns_values()
        

    def on_ps_change(self, ps):
        
        print "PS:", ps
        

    def on_rt_change(self, rt):
        
        print "RT:", rt
        

    def __check_radiodns_values(self):
        
        frequency = self.radio.get_frequency()
        pi = self.radio.rds.pi
        ecc = self.radio.rds.ecc
        
        if not pi: return
        
        if ecc and pi:
            radiodns_fqdn = "%s.%s.%s.fm.radiodns.org" % (frequency,
                                                               pi[2:],
                                                               ecc[2:])
        else:
            radiodns_fqdn = "%s.%s.%s.fm.radiodns.org" % (frequency,
                                                               pi[2:],
                                                               self.country)
        print "RadioDNS FQSN:", radiodns_fqdn
        
        try:
            answers = dns.resolver.query(radiodns_fqdn)
            print "Authoritative RadioDNS FQDN:", answers[0]
        except dns.resolver.NXDOMAIN:
            print "RadioDNS did not recognise service parameters"
        

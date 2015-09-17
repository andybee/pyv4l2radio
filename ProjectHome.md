**Heavily based upon the original work of Martin Grimme, this library provides a simplified version of his [pyFMRadio](http://pyfmradio.garage.maemo.org/) library for controlling any [V4L2](http://linux.bytesex.org/v4l2/) FM radio via the kernel driver support.**

Added to this the package includes an [RDS](http://www.rds.org.uk/) decoder handling a relatively small number of group types and, from that, provides a demonstrative implementation of RadioDNS. Due to the recent harmonisation of RBDS and RDS it should also decode RBDS without problem.

Developed against and tested with a [Silicon Laboratories USB FM radio](http://www.silabs.com/products/mcu/Pages/USBFMRadioRD.aspx) (based on Si4701 chipset), though it should work with any V4L2 compatible FM radio.

This package depends on [dnspython](http://www.dnspython.org/).
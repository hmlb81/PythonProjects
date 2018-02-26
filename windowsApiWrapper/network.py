import enum
import ctypes

class AddressFamily(enum.Enum) : 
    UNSPEC = 0 #AF_UNSPEC: unspecified
    INET = 2 #AF_INET: IPv4 address
    INET6 = 23 #AF_INET6: IPv6 address
    
class GetAdapterAddressFlags(enum.Enum) : 
    SKIP_UNICAST = 0x0001 #GAA_FLAG_SKIP_UNICAST: do not return unicast addresses.
    SKIP_ANYCAST = 0x0002 #GAA_FLAG_SKIP_ANYCAST: do not return IPV6 anycast addresses.
    SKIP_MULTICAST = 0x0004 #GAA_FLAG_SKIP_MULTICAST: do not return multicast addresses.
    SKIP_DNS_SERVER = 0x0008 #GAA_FLAG_SKIP_DNS_SERVER: do not return addresses of DNS server
    INCLUDE_PREFIX = 0x0010 #GAA_FLAG_INCLUDE_PREFIX: return a list of IP Address prefixes on this adapter
    SKIP_FRIENTLY_NAME = 0x0020 #GAA_FLAG_SKIP_FRIENDLY_NAME: do not return the adapter friendly name.
    INCLUDE_WINS_INFO = 0x0040 #GAA_FLAG_INCLUDE_WINS_INFO: return addresses of Windows Internet Name Service(WINS) server.
    INCLUDE_GATEWAYS = 0x0080 #GAA_FLAG_INCLUDE_GATEWAYS: return the addresses of default gateways.
    INCLUDE_ALL_INTERFACCES = 0x0100 #GAA_FLAG_INCLUDE_ALL_INTERFACES: return addresses for all NDIS interfaces.
    INCLUDE_ALL_COMPARTMENTS = 0x0200 #GAA_FLAG_INCLUDE_ALL_COMPARTMENTS: return addresses in all routing compartments.
    INCLUDE_TUNNEL_BINDINGORDER = 0x0400 #GAA_FLAG_INCLUDE_TUNNEL_BINDINGORDER: return the adapter addresses sorted in tunnel binding order.
    
#iphelper api wrapper
class iphelperApiWrapper : 
    def getAdaptersAddresses(self) :
        return None #TODO:implementing later

iphelperApiWrapperInstance = iphelperApiWrapper()
    

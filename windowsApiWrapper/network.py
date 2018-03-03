import enum
import ctypes

class AddressFamily(enum.Enum) : 
    UNSPEC = 0 #AF_UNSPEC: unspecified
    INET = 2 #AF_INET: IPv4 address
    INET6 = 23 #AF_INET6: IPv6 address
    
class GetAdapterAddressFlags(enum.Enum) : 
    NONE = 0 #none flags specified
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

class IPPrefixOrigin(enum.Enum) : 
    Other = 0 #IpPrefixOriginOther
    Manual = 1 #IpPrefixOriginManual
    WellKnown = 2 #IpPrefixOriginWellKnown
    Dhcp = 3 #IpPrefixOriginDhcp
    RouterAdvertisement = 4 #IpPrefixOriginRouterAdvertisement
    Unchanged = 16 #IpPrefixOriginUnchanged

class IPDadState(enum.Enum) : 
    Invalid = 0 #IpDadStateInvalid
    Tentative = 1 #IpDadStateTentative
    Duplicate = 2 #IpDadStateDuplicate
    Deprecated = 3 #IpDadStateDeprecated
    Preferred = 4 #IpDadStatePreferred
    
class IFOperStatus(enum.Enum) :
    Up = 1 #IfOperStatusUp
    Down = 2 #IfOperStatusDown
    Testing = 3 #IfOperStatusTesting
    Unknown = 4 #IfOperStatusUnknown
    Dormant = 5 #IfOperStatusDormant
    NotPresent = 6 #IfOperStatusNotPresent
    LowerLayerDown = 7 #IfOperStatusLowerLayerDown 
    
class Sockaddr(ctypes.Structure) : 
    _fields_ = [
        ("sa_family", ctypes.c_ushort),
        ("sa_data", ctypes.c_char * 14)
    ]

class SocketAddress(ctypes.Structure) : 
    _fields_ = [
        ("sockaddr", ctypes.POINTER(Sockaddr)),
        ("sockaddrLength", ctypes.c_int)
    ]
    
class NetLuidInfo(ctypes.Structure) :
    _fields_ = [
        ("reserved", ctypes.c_uint64, 24), #24 bit width
        ("netLuidIndex", ctypes.c_uint64, 24), #24 bit width
        ("iftype", ctypes.c_uint64, 16) #16 bit width
    ]
     
class NetLuid(ctypes.Union) : 
    _fields_ = [
        ("value", ctypes.c_ulonglong),
        ("info", NetLuidInfo)
    ]      
    
#IPAdapterUnicastAddress member 0
class IPAdapterUnicastAddressLayout(ctypes.Structure) : 
    _fields_ = [
        ("length", ctypes.c_ulong),
        ("flags", ctypes.c_ulong)
    ]

class IPAdapterUnicastAddress(ctypes.Structure) : 
    _fields_ = [
        ("layout", IPAdapterUnicastAddressLayout),
        ("next", ctypes.c_voidp), #IPAdapterUnicastAddress in actual, use void* temporily
        ("address", SocketAddress),
        ("prefixOrigin", ctypes.c_int), #IP_PREFIX_ORIGIN in actual
        ("suffixOrigin", ctypes.c_int), #IP_PREFIX_ORIGIN in actual
        ("dadState", ctypes.c_int), #IP_DAD_STATE in actual
        ("validLifetime", ctypes.c_ulong),
        ("preferredLifetime", ctypes.c_ulong),
        ("leaseLifetime", ctypes.c_ulong),
        ("onlinkPrefixLength", ctypes.c_ubyte)
    ]

class IPAdapterAnycastAddressLayoutValue(ctypes.Structure) : 
    _fields_ = [
        ("length", ctypes.c_ulong),
        ("flags", ctypes.c_ulong)
    ]
    
#IPAdapterAnycastAddress member 0    
class IPAdapterAnycastAddressLayout(ctypes.Union) : 
    _fields_ = [
        ("alignment", ctypes.c_ulonglong),
        ("value", IPAdapterAnycastAddressLayoutValue)
    ]

class IPAdapterAnycastAddress(ctypes.Structure) :
    _fields_ = [
        ("layout", IPAdapterAnycastAddressLayout),
        ("next", ctypes.c_voidp), #IPAdapterAnycastAddress* in actual, use void* temporily
        ("address", SocketAddress)
    ]
    
class IPAdapterMulticastAddressLayoutValue(ctypes.Structure) : 
    _fields_ = [
        ("length", ctypes.c_ulong),
        ("flags", ctypes.c_ulong)
    ]
       
class IPAdapterMulticastAddressLayout(ctypes.Union) : 
    _fields_ = [
        ("alignment", ctypes.c_ulonglong),
        ("value", IPAdapterMulticastAddressLayoutValue)
    ]
   
class IPAdapterMulticastAddress(ctypes.Structure) : 
    _fields_ = [
        ("layout", IPAdapterMulticastAddressLayout),
        ("next", ctypes.c_voidp), #IPAdapterMulticastAddress* in actual, use void* temporily
        ("address", SocketAddress)
    ]
    
class IPAdapterDnsServerAddressLayoutValue(ctypes.Structure) :
    _fields_ = [
        ("length", ctypes.c_ulong),
        ("reserved", ctypes.c_ulong)
    ]
        
class IPAdapterDnsServerAddressLayout(ctypes.Union) : 
    _fields_ = [
        ("alignment", ctypes.c_ulonglong),
        ("value", IPAdapterDnsServerAddressLayoutValue)
    ]
       
class IPAdapterDnsServerAddress(ctypes.Structure) :
    _fields_ = [
        ("layout", IPAdapterDnsServerAddressLayout),
        ("next", ctypes.c_voidp), #IPAdapterDnsServerAddress* in actual, use void* temporily
        ("address", SocketAddress)
    ]
    
class IPAdapterPrefixLayoutValue(ctypes.Structure) : 
    _fields_ = [
        ("length", ctypes.c_ulong),
        ("flags", ctypes.c_ulong)
    ]
    
class IPAdapterPrefixLayout(ctypes.Union) : 
    _fields_ = [
        ("alignment", ctypes.c_ulonglong),
        ("value", IPAdapterPrefixLayoutValue)
    ]
    
class IPAdapterPrefix(ctypes.Structure) :
    _fields_ = [
        ("layout", IPAdapterPrefixLayout),
        ("next", ctypes.c_voidp), #_IP_ADAPTER_PREFIX in actual, use void* temporily
        ("address", SocketAddress),
        ("prefixLength", ctypes.c_ulong)
    ]
    
class IPAdapterWinsServerAddressLayoutValue(ctypes.Structure) :
    _fields_ = [
        ("length", ctypes.c_ulong),
        ("reserved", ctypes.c_ulong)
    ]
    
class IPAdapterWinsServerAddressLayout(ctypes.Union) :
    _fields_ = [
        ("alignment", ctypes.c_ulonglong),
        ("value", IPAdapterWinsServerAddressLayoutValue)
    ]
    
class IPAdapterWinsServerAddress(ctypes.Structure) :
    _fields_ = [
        ("layout", IPAdapterWinsServerAddressLayout),
        ("next", ctypes.c_voidp), #_IP_ADAPTER_WINS_SERVER_ADDRESS* in actual, use void* temporily
        ("address", SocketAddress)
    ]  
    
class IPAdapterGatewayAddressLayoutValue(ctypes.Structure) :
    _fields_ = [
        ("length", ctypes.c_ulong),
        ("reserved", ctypes.c_ulong)
    ]
        
class IPAdapterGatewayAddressLayout(ctypes.Union) : 
    _fields_ = [
        ("alignment", ctypes.c_ulonglong),
        ("value", IPAdapterGatewayAddressLayoutValue)
    ]
       
class IPAdapterGatewayAddress(ctypes.Structure) : 
    _fields_ = [
        ("layout", IPAdapterGatewayAddressLayout),
        ("next", ctypes.c_voidp), #_IP_ADAPTER_GATEWAY_ADDRESS* in actual, use void* temporily
        ("address", SocketAddress)
    ]
    
class IPAdapterAddressLayoutValue(ctypes.Structure) : 
    _fields_ = [
        ("length", ctypes.c_ulong),
        ("ifindex", ctypes.c_ulong)
    ]

#IP_ADAPTER_ADDRESSES structure member 0    
class IPAdapterAddressesLayout(ctypes.Union) : 
    _fields_ = [
        ("alignment", ctypes.c_ulonglong),
        ("value", IPAdapterAddressLayoutValue)
    ]

class IPAdapterAddresses(ctypes.Structure) : 
    _fields_ = [
        ("layout", IPAdapterAddressesLayout),
        ("next", ctypes.c_voidp), #IPAdapterAddresses pointer in actual, used void* temporily
        ("adapterName", ctypes.c_char_p),
        ("firstUnicastAddress", ctypes.POINTER(IPAdapterUnicastAddress)),
        ("firstAnycastAddress", ctypes.POINTER(IPAdapterAnycastAddress)),
        ("firstMulticastAddress", ctypes.POINTER(IPAdapterMulticastAddress)),
        ("firstDnsServerAddress", ctypes.POINTER(IPAdapterDnsServerAddress)),
        ("dnsSuffix", ctypes.c_wchar_p),
        ("description", ctypes.c_wchar_p),
        ("friendlyName", ctypes.c_wchar_p),
        ("physicalAddress", ctypes.c_byte * 8), #MAX_ADAPTER_ADDRESS_LENGTH = 8
        ("physicalAddressLength", ctypes.c_ulong),
        ("flags", ctypes.c_ulong),
        ("mtu", ctypes.c_ulong),
        ("iftype", ctypes.c_ulong),
        ("operStatus", ctypes.c_ulong), #IF_OPER_STATUS
        ("ipv6IfIndex", ctypes.c_ulong),
        ("zoneIndices", ctypes.c_ulong * 16),
        ("firstPrefix", ctypes.POINTER(IPAdapterPrefix)),
        ("transmitLinkSpeed", ctypes.c_uint64),
        ("receiveLinkSpeed", ctypes.c_uint64),
        ("firstWinsServerAddress", ctypes.POINTER(IPAdapterWinsServerAddress)), #PIP_ADAPTER_WINS_SERVER_ADDRESS_LH
        ("firstGatewayAddress", ctypes.POINTER(IPAdapterGatewayAddress)), #PIP_ADAPTER_GATEWAY_ADDRESS_LH
        ("ipv4Metric", ctypes.c_ulong),
        ("ipv6Metric", ctypes.c_ulong),
        ("luid", NetLuid), #IF_LUID
        ("dhcp4Server", SocketAddress),
        ("compartmentId", ctypes.c_ulong) #NET_IF_COMPARTMENT_ID
    ]
    #typedef struct _IP_ADAPTER_ADDRESSES {
      #NET_IF_NETWORK_GUID                NetworkGuid;
      #NET_IF_CONNECTION_TYPE             ConnectionType;
      #TUNNEL_TYPE                        TunnelType;
     # SOCKET_ADDRESS                     Dhcpv6Server;
    #  BYTE                               Dhcpv6ClientDuid[MAX_DHCPV6_DUID_LENGTH];
   #   ULONG                              Dhcpv6ClientDuidLength;
  #    ULONG                              Dhcpv6Iaid;
 #     PIP_ADAPTER_DNS_SUFFIX             FirstDnsSuffix;
#    } IP_ADAPTER_ADDRESSES, *PIP_ADAPTER_ADDRESSES;
    
    
    
#iphelper api wrapper
class iphelperApiWrapper : 
    def __init__(self) : 
        self._dll = ctypes.windll.Iphlpapi
    
    #family as AddressFamily enumeration
    def getAdaptersAddresses(self, family, flags) :
        familyValue = ctypes.c_ulong(family.value)
        flagsValue = ctypes.c_ulong(flags.value)
        reservedValue = None
        addresses = IPAdapterAddresses()
        return None #TODO:implementing later

iphelperApiWrapperInstance = iphelperApiWrapper()
    

import ctypes
import enum
import itertools
from . import commonDefinitions

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
    
class NetIFConnectionType(enum.Enum) : 
    Dedicated = 1 #NET_IF_CONNECTION_DEDICATED
    Passive = 2 #NET_IF_CONNECTION_PASSIVE
    Demand = 3 #NET_IF_CONNECTION_DEMAND
    Maximum = 4 #NET_IF_CONNECTION_MAXIMUM    
    
class TunnelType(enum.Enum) :
    NONE = 0 # TUNNEL_TYPE_NONE
    Other = 1 #TUNNEL_TYPE_OTHER
    Direct = 2 #TUNNEL_TYPE_DIRECT
    IP6To4 = 11 #TUNNEL_TYPE_6TO4
    ISATAP = 13 #TUNNEL_TYPE_ISATAP
    Teredo = 14 #TUNNEL_TYPE_TEREDO
    IpHttps = 15 #TUNNEL_TYPE_IPHTTPS
    
class Sockaddr(ctypes.Structure) : 
    sa_data_size = 14
    
    _fields_ = [
        ("sa_family", ctypes.c_ushort),
        ("sa_data", ctypes.c_char * sa_data_size)
    ]
    
    def __init__(self) :
        self.sa_family = 0
        self.sa_data = bytes(itertools.repeat(0, self.sa_data_size))
        
    def __str__(self) :
        return "Sockaddr(sa_family={0}, sa_data={1})".format(self.sa_family, self.sa_data)

class SocketAddress(ctypes.Structure) : 
    _fields_ = [
        ("sockaddr", ctypes.POINTER(Sockaddr)),
        ("sockaddrLength", ctypes.c_int)
    ]
    
    def __init__(self) :
        self.sockaddr = None
        self.sockaddrLength = 0
    
class NetLuidInfo(ctypes.Structure) :
    _fields_ = [
        ("reserved", ctypes.c_uint64, 24), #24 bit width
        ("netLuidIndex", ctypes.c_uint64, 24), #24 bit width
        ("iftype", ctypes.c_uint64, 16) #16 bit width
    ]
    
    def __init__(self) :
        self.reserved = 0
        self.netLuidIndex = 0
        self.iftype = 0
        
    def __str__(self) :
        return "NetLuidInfo(netLuidIndex={0}, iftype={1})".format(self.netLuidIndex, self.iftype)
     
class NetLuid(ctypes.Union) : 
    _fields_ = [
        ("value", ctypes.c_ulonglong),
        ("info", NetLuidInfo)
    ]     
    
    def __init__(self) :
        self.value = 0
        self.info = NetLuidInfo()
        
    def __str__(self) :
        return self.info.__str__()
    
class IPAdapterAddressCommonLayout(ctypes.Structure) :
    _fields_ = [
        ("length", ctypes.c_ulong),
        ("flags", ctypes.c_ulong)
    ]
    
    def __int__(self) :
        self.length = 0
        self.flags = 0
        
    def __str__(self) :
        return "IPAdapterAddressCommonLayout(length={0}, flags={1})".format(self.length, self.flags)

#IPAdapterAnycastAddress member 0    
class IPAdapterAddressCommonAlignedLayout(ctypes.Union) : 
    _fields_ = [
        ("alignment", ctypes.c_ulonglong),
        ("value", IPAdapterAddressCommonLayout)
    ]
    
    def __init__(self) :
        self.alignment = 0
        self.value = IPAdapterAddressCommonLayout()
        
    def __str__(self) :
        return self.value.__str__()
    
class IPAdapterUnicastAddress(ctypes.Structure) : 
    _fields_ = [
        ("layout", IPAdapterAddressCommonLayout),
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
    
class IPAdapterAnycastAddress(ctypes.Structure) :
    _fields_ = [
        ("layout", IPAdapterAddressCommonAlignedLayout),
        ("next", ctypes.c_voidp), #IPAdapterAnycastAddress* in actual, use void* temporily
        ("address", SocketAddress)
    ]
    
class IPAdapterMulticastAddress(ctypes.Structure) : 
    _fields_ = [
        ("layout", IPAdapterAddressCommonAlignedLayout),
        ("next", ctypes.c_voidp), #IPAdapterMulticastAddress* in actual, use void* temporily
        ("address", SocketAddress)
    ]
    
class IPAdapterDnsServerAddress(ctypes.Structure) :
    _fields_ = [
        ("layout", IPAdapterAddressCommonAlignedLayout),
        ("next", ctypes.c_voidp), #IPAdapterDnsServerAddress* in actual, use void* temporily
        ("address", SocketAddress)
    ]
    
class IPAdapterPrefix(ctypes.Structure) :
    _fields_ = [
        ("layout", IPAdapterAddressCommonAlignedLayout),
        ("next", ctypes.c_voidp), #_IP_ADAPTER_PREFIX in actual, use void* temporily
        ("address", SocketAddress),
        ("prefixLength", ctypes.c_ulong)
    ]
    
class IPAdapterWinsServerAddress(ctypes.Structure) :
    _fields_ = [
        ("layout", IPAdapterAddressCommonAlignedLayout),
        ("next", ctypes.c_voidp), #_IP_ADAPTER_WINS_SERVER_ADDRESS* in actual, use void* temporily
        ("address", SocketAddress)
    ]  
        
class IPAdapterGatewayAddress(ctypes.Structure) : 
    _fields_ = [
        ("layout", IPAdapterAddressCommonAlignedLayout),
        ("next", ctypes.c_voidp), #_IP_ADAPTER_GATEWAY_ADDRESS* in actual, use void* temporily
        ("address", SocketAddress)
    ]
    
class IPAdapterDnsSuffix(ctypes.Structure) :
    _fields_ = [
        ("next", ctypes.c_voidp), #_IP_ADAPTER_DNS_SUFFIX* in actual, use void* temporily
        ("suffixString", ctypes.c_wchar * 256) #MAX_DNS_SUFFIX_STRING_LENGTH=256
    ]

class IPAdapterAddresses(ctypes.Structure) : 
    _fields_ = [
        ("layout", IPAdapterAddressCommonAlignedLayout),
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
        ("compartmentId", ctypes.c_ulong), #NET_IF_COMPARTMENT_ID
        ("networkGuid", commonDefinitions.Guid),
        ("connectionType", ctypes.c_ulong), #NET_IF_CONNECTION_TYPE
        ("tunnelType", ctypes.c_ulong), #TUNNEL_TYPE
        ("dhcpv6Server", SocketAddress),
        ("dhcpv6ClientDuid", ctypes.c_byte * 130), #MAX_DHCPV6_DUID_LENGTH=130
        ("dhcpv6ClientDuidLength", ctypes.c_ulong),
        ("dhcpv6Iaid", ctypes.c_ulong),
        ("firstDnsSuffix", ctypes.POINTER(IPAdapterDnsSuffix))
    ]
    
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
        size = ctypes.c_ulong(0)
        ret = self._dll.GetAdaptersAddresses(familyValue, flagsValue, reservedValue, ctypes.byref(addresses), ctypes.byref(size))
        
        retValue = commonDefinitions.SystemErrorCodes(ret)
        return None #TODO:implementing later

iphelperApiWrapperInstance = iphelperApiWrapper()



    

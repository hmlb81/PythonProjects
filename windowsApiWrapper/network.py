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
        ("firstMulticastAddress", ctypes.POINTER(IPAdapterMulticastAddress))
    ]
    #typedef struct _IP_ADAPTER_ADDRESSES {
      #PIP_ADAPTER_DNS_SERVER_ADDRESS     FirstDnsServerAddress;
      #PWCHAR                             DnsSuffix;
      #PWCHAR                             Description;
      #PWCHAR                             FriendlyName;
      #BYTE                               PhysicalAddress[MAX_ADAPTER_ADDRESS_LENGTH];
      #DWORD                              PhysicalAddressLength;
      #DWORD                              Flags;
      #DWORD                              Mtu;
      #DWORD                              IfType;
      #IF_OPER_STATUS                     OperStatus;
      #DWORD                              Ipv6IfIndex;
      #DWORD                              ZoneIndices[16];
      #PIP_ADAPTER_PREFIX                 FirstPrefix;
      #ULONG64                            TransmitLinkSpeed;
      #ULONG64                            ReceiveLinkSpeed;
      #PIP_ADAPTER_WINS_SERVER_ADDRESS_LH FirstWinsServerAddress;
      #PIP_ADAPTER_GATEWAY_ADDRESS_LH     FirstGatewayAddress;
      #ULONG                              Ipv4Metric;
      #ULONG                              Ipv6Metric;
      #IF_LUID                            Luid;
      #SOCKET_ADDRESS                     Dhcpv4Server;
      #NET_IF_COMPARTMENT_ID              CompartmentId;
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
    

import enum

class AddressFamily(enum.Enum) : 
    UNSPEC = 0 #AF_UNSPEC: unspecified
    INET = 2 #AF_INET: IPv4 address
    INET6 = 23 #AF_INET6: IPv6 address
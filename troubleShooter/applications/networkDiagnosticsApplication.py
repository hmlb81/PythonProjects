import logging
import windowsApiWrapper.network

#network diagnostics
class networkDiagnosticsApplication : 
    #collect network adapters information
    def collectNetworkAdaptersInformation(self) :
        family = windowsApiWrapper.network.AddressFamily.UNSPEC
        flags = windowsApiWrapper.network.GetAdapterAddressFlags.NONE
        print(windowsApiWrapper.network.iphelperApiWrapperInstance.getAdaptersAddresses(family, flags))
        logging.info("networkDiagnosticsApplications.collectNetworkAdaptersInformations called.") #TODO implementing later

instance = networkDiagnosticsApplication() 
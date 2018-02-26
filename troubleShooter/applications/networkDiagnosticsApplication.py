import logging
import windowsApiWrapper.network

#network diagnostics
class networkDiagnosticsApplication : 
    #collect network adapters information
    def collectNetworkAdaptersInformation(self) :
        print(windowsApiWrapper.network.iphelperApiWrapperInstance.getAdaptersAddresses())
        logging.info("networkDiagnosticsApplications.collectNetworkAdaptersInformations called.") #TODO implementing later

instance = networkDiagnosticsApplication() 
import PyInstaller.__main__

class packagingApplication : 
    @staticmethod
    def getInstance() :
        return _instance

    def printDescription(self) :
        print("for packaging py to exe")
        
    def pack(self, packageName, pythonFilePath) :
        options = [
            "--name={0}".format(packageName),
            "--onefile",
            "--console", #"--windowed",
            #"--add-binary={0}",
            #"--add-data={0}",
            #"--icon={0}",
            pythonFilePath
        ]
        PyInstaller.__main__.run(options)

_instance = packagingApplication()
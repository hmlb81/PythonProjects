class collectionsHelper : 
    @staticmethod
    def getInstance() :
        return _instance
    
    def firstOrDefault(self, items, defaultValue, predicator) :
        for item in items :
            isMatch = predicator(item)
            if isMatch :
                return item
        
        return defaultValue

_instance = collectionsHelper()
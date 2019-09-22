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
    
    def checkAndPopLastElement(self, items, defaultValue) :
        itemCount = len(items)
        if (itemCount <= 0) :
            return defaultValue
        
        return items.pop()

_instance = collectionsHelper()
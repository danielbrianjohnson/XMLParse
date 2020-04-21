import csv
import xml.etree.ElementTree as ET
  
def getConfig(configFile):
    f = open("config.txt", "r")
    configArray = []
    for line in f:
        if line[0] != '#' and line != '\n':
            configArray.append(line[0].strip())
    return configArray


          
  
def parseXML(thingToParse):
    if thingToParse == 1:
        print "Get DAs defined in VSEconfig"


  
  
def savetoCSV(newsitems, filename): 
  
    # specifying the fields for csv file 
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media'] 
  
    # writing to csv file 
    with open(filename, 'w') as csvfile: 
  
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
  
        # writing headers (field names) 
        writer.writeheader() 
  
        # writing data rows 
        writer.writerows(newsitems) 
  
      
def main():
    # Parse the file
    tree = ET.parse('VSEconfig.xml')

    # Get the file root
    root = tree.getroot()

    testFile = open("test.csv", "a")
    test = {}
    for neighbors in root.iter('GenericBattleManager'):
            BM = neighbors.get('name')
            testFile.write(BM)

            for neighbor in neighbors.iter('Asset'):
                asset =  neighbor.attrib.get('name')
                testFile.write(",")
                testFile.write(asset)
            testFile.write("\n")
    testFile.close();



    #print dicti

   #33 print "3333"
    #for asset in root.iter('GenericBattleManager'):
    #    assetName = asset.find('Asset')
    #    BM = asset.get('name')
    #    print(BM, assetName)

    # get config prompts
    #actionsToDo = getConfig('config.txt')
    #print actionsToDo

    # parse xml file and save to csv
    #for action in actionsToDo:
     #   newsitems = parseXML(action)
    #    savetoCSV(newsitems, action)
      
      
if __name__ == "__main__": 
  
    # calling main function 
    main() 

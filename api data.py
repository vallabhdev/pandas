import json
import csv
import requests

url = "https://animals-endangered-environmentalism.p.rapidapi.com/taxonomy/class"

querystring = {"q":"mammalia"}

headers = {
    'x-rapidapi-host': "animals-endangered-environmentalism.p.rapidapi.com",
    'x-rapidapi-key': "95afa53298msh4276afcac645857p19ff34jsnd46209186d72"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


apidata=response.text
apidata.encode("utf-8")
fetchdata=json.loads(apidata)
#print(fetchdata[0])


scientificname=[]
family=[]
Class=[]
yearassessed=[]
commonname=[]
yearpublished=[]
kingdom=[]
phylum=[]
populationTrend=[]
genus=[]
numberofmatureindividuals=[]


native=[]
numberoflocation=[]
extantResident=[]
continuingDeclineOfMatureIndividuals=[]
currentPopulationTrend=[]
threats=[]
habitatAndEcologysystem=[]
generationLengthYears=[]
habitatType=[]
habitatname=[]
conservationActions=[]
iucnRedListCategoryAndCriteria=[]
useAndTrade=[]






"""estimatedExtentOfOccurrenceEooKm2=[]
estimatedAreaOfOccupancyAooKm2=[]
extremeFluctuationsInExtentOfOccurrenceEoo=[]
extremeFluctuationsInTheNumberOfLocations=[]
#residentialCommercialDevelopment=[]
#humanIntrusionsDisturbance=[]"""



i=0
for i in range(len(fetchdata)):
    scientificname.append(fetchdata[i]['scientificName'])
    family.append(fetchdata[i]['family'])
    Class.append(fetchdata[i]['class'])
    yearassessed.append((fetchdata[i]['yearAssessed']))
    commonname.append(fetchdata[i]['commonName'])
    yearpublished.append((fetchdata[i]['yearPublished']))
    kingdom.append(fetchdata[i]['kingdom'])
    phylum.append(fetchdata[i]['phylum'])
    populationTrend.append(fetchdata[i]['populationTrend'])
    genus.append(fetchdata[i]['genus'])
    numberofmatureindividuals.append((fetchdata[i]['numberOfMatureIndividuals']))




    try:
        native.append(fetchdata[i]['data']['geographicRange']['native'])
    except:
        pass
    numberoflocation.append(fetchdata[i]['data']['geographicRange']['numberOfLocations'])
    try:
        extantResident.append(fetchdata[i]['data']['geographicRange']['extantResident'])
    except:
        pass
        #extantResident.append('NULL')
    continuingDeclineOfMatureIndividuals.append(fetchdata[i]['data']['population']['continuingDeclineOfMatureIndividuals'])
    currentPopulationTrend.append(fetchdata[i]['data']['population']['currentPopulationTrend'])
    threats.append(fetchdata[i]['data']['threats'])
    habitatAndEcologysystem.append(fetchdata[i]['data']['habitatAndEcology']['system'])
    generationLengthYears.append(fetchdata[i]['data']['habitatAndEcology']['generationLengthYears'])
    habitatType.append(fetchdata[i]['data']['habitatAndEcology']['habitatType'])
    habitatname.append(fetchdata[i]['data']['habitatAndEcology']['name'])
    conservationActions.append(fetchdata[i]['data']['conservationActions'])
    iucnRedListCategoryAndCriteria.append(fetchdata[i]['data']['assessmentInformation']['iucnRedListCategoryAndCriteria'])
    useAndTrade.append(fetchdata[i]['data']['useAndTrade']['details']['useAndTrade'])




rows=zip(scientificname,family,Class,yearassessed,commonname,yearpublished,kingdom,phylum,populationTrend,genus,
         numberofmatureindividuals,native,numberoflocation,extantResident,continuingDeclineOfMatureIndividuals,
         currentPopulationTrend,threats,habitatAndEcologysystem,generationLengthYears,habitatType,habitatname,
         conservationActions,iucnRedListCategoryAndCriteria,useAndTrade)
header=['scientificname','family','Class','yearassessed','commonname','yearpublished','kingdom','phylum','populationtrend','genus',
         'numberofmatureindividuals','native','numberoflocation','extantresident','continuingDeclineOfMatureIndividuals',
         'currentPopulationTrend','threats','habitatAndEcologysystem','generationLengthYears','habitatType','habitatname',
         'conservationActions','iucnRedListCategoryAndCriteria','useAndTrade']

with open('bytaxonomymammalia.csv', "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in rows:
        try:
            writer.writerow(row)
        except:
            pass


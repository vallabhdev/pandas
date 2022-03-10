import json
import csv
import requests

#giving url and query that what to find
url = "https://animals-endangered-environmentalism.p.rapidapi.com/taxonomy/class"
querystring = {"q":"mammalia"}

#header of api
headers = {
    'x-rapidapi-host': "animals-endangered-environmentalism.p.rapidapi.com",
    'x-rapidapi-key': "95afa53298msh4276afcac645857p19ff34jsnd46209186d72"
    }

#response we are getting in the form of data
response = requests.request("GET", url, headers=headers, params=querystring)


#transforming data into list
apidata=response.text
apidata.encode("utf-8")
fetchdata=json.loads(apidata)
#print(fetchdata[0])


#declaring variable names or features of csv
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




#fetching data
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

    #if it has no data, it won't give error
    try:
        native.append(fetchdata[i]['data']['geographicRange']['native'])
    except:
        pass
    numberoflocation.append(fetchdata[i]['data']['geographicRange']['numberOfLocations'])
    try:
        extantResident.append(fetchdata[i]['data']['geographicRange']['extantResident'])
    except:
        pass

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



#defining row and header of csv file
rows=zip(scientificname,family,Class,yearassessed,commonname,yearpublished,kingdom,phylum,populationTrend,genus,
         numberofmatureindividuals,native,numberoflocation,extantResident,continuingDeclineOfMatureIndividuals,
         currentPopulationTrend,threats,habitatAndEcologysystem,generationLengthYears,habitatType,habitatname,
         conservationActions,iucnRedListCategoryAndCriteria,useAndTrade)
header=['scientificname','family','Class','yearassessed','commonname','yearpublished','kingdom','phylum','populationtrend','genus',
         'numberofmatureindividuals','native','numberoflocation','extantresident','continuingDeclineOfMatureIndividuals',
         'currentPopulationTrend','threats','habitatAndEcologysystem','generationLengthYears','habitatType','habitatname',
         'conservationActions','iucnRedListCategoryAndCriteria','useAndTrade']



#storing data into csv
with open('bytaxonomymammalia.csv', "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in rows:
        try:
            writer.writerow(row)
        except:
            pass






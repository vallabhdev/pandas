import json
import csv
import requests

"""response = requests.get("https://animals-endangered-environmentalism.p.rapidapi.com/population/1")
print(response.status_code)"""


url = "https://animals-endangered-environmentalism.p.rapidapi.com/population/1"

querystring = {"type":"equal"}

headers = {
    'x-rapidapi-host': "animals-endangered-environmentalism.p.rapidapi.com",
    'x-rapidapi-key': "95afa53298msh4276afcac645857p19ff34jsnd46209186d72"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
apidata=response.text
apidata.encode("utf-8")
fetchdata=json.loads(apidata)
#print(type(p))
family=[]
commonname=[]
iucnRedListCategoryAndCriteria=[]
estimatedExtentOfOccurrenceEooKm2=[]
estimatedAreaOfOccupancyAooKm2=[]
extremeFluctuationsInExtentOfOccurrenceEoo=[]
extremeFluctuationsInTheNumberOfLocations=[]
extantResident=[]
habitatType=[]
generationLengthYears=[]
#residentialCommercialDevelopment=[]
#humanIntrusionsDisturbance=[]
threats=[]
useAndTrade=[]
populationTrend=[]
Class=[]


"""i = 0
for i in range(len(fetchdata)):"""


i=0
for i in range(len(fetchdata)):
    family.append(fetchdata[i]['family'])
    commonname.append(fetchdata[i]['commonName'])
    iucnRedListCategoryAndCriteria.append(fetchdata[i]['data']['assessmentInformation']['iucnRedListCategoryAndCriteria'])
    estimatedExtentOfOccurrenceEooKm2.append(fetchdata[i]['data']['geographicRange']['details']['estimatedExtentOfOccurrenceEooKm2'])
    estimatedAreaOfOccupancyAooKm2.append(fetchdata[i]['data']['geographicRange']['details']['estimatedAreaOfOccupancyAooKm2'])
    extremeFluctuationsInExtentOfOccurrenceEoo.append(fetchdata[i]['data']['geographicRange']['details']['extremeFluctuationsInExtentOfOccurrenceEoo'])
    extremeFluctuationsInTheNumberOfLocations.append(fetchdata[i]['data']['geographicRange']['details']['extremeFluctuationsInTheNumberOfLocations'])
    try:
        extantResident.append(fetchdata[i]['data']['geographicRange']['extantResident'])
    except:
        extantResident.append('NULL')
    habitatType.append(fetchdata[i]['data']['habitatAndEcology']['habitatType'])
    generationLengthYears.append(fetchdata[i]['data']['habitatAndEcology']['generationLengthYears'])
    #residentialCommercialDevelopment.append(fetchdata[i]['data']['threats']['residential&CommercialDevelopment'][0])
    threats.append(fetchdata[i]['data']['threats'])
    useAndTrade.append(fetchdata[i]['data']['useAndTrade']['details']['useAndTrade'])
    populationTrend.append(fetchdata[i]['populationTrend'])
    Class.append(fetchdata[i]['class'])

rows=zip(commonname,family,iucnRedListCategoryAndCriteria,estimatedExtentOfOccurrenceEooKm2,estimatedAreaOfOccupancyAooKm2,
         extremeFluctuationsInExtentOfOccurrenceEoo,extremeFluctuationsInTheNumberOfLocations,extantResident,habitatType,
         generationLengthYears,threats,useAndTrade,populationTrend,Class)
header=['commonname','family','iucnRedListCategoryAndCriteria','estimatedExtentOfOccurrenceEooKm2','estimatedAreaOfOccupancyAooKm2',
         'extremeFluctuationsInExtentOfOccurrenceEoo','extremeFluctuationsInTheNumberOfLocations','extantResident','habitatType',
         'generationLengthYears','threats','useAndTrade','populationTrend','Class']
with open('data.csv', "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in rows:
        try:
            writer.writerow(row)
        except:
            pass





#print(len(extantResident))
#print(extantResident)
#print(fetchdata[i]['data']['assessmentInformation']['yearPublished'])
#print(response.text)



#Connect to Google using a Proxie due to the Google Rate Limit
pytrends = TrendReq(hl='en-US',tz=360)

#Create Keyword_list and Region List

kw_list = ['nike air max']
Country = ['US'] 
regions = ['US-MS',	'US-MT',	'US-NC',	'US-ND',	'US-NE',	'US-NH',	'US-NJ',	'US-NM',	'US-NV',	'US-NY',	'US-OH',	'US-OK',	'US-SD',	'US-TN',	'US-TX',	'US-UT',	'US-VA',	'US-VT',	'US-WA',	'US-WI']
regionsname = ['Mississippi',	'Montana',	'North Carolina',	'North Dakota',	'Nebraska',	'New Hampshire',	'New Jersey',	'New Mexico',	'Nevada',	'New York',	'Ohio',	'Oklahoma',	'South Dakota',	'Tennessee',	'Texas',	'Utah',	'Virginia',	'Vermont',	'Washington',	'Wisconsin']	

#Records Interest Over Week from timeframe Period Above
i=0
for p in regions:
    
    print(str(p))
    
    pytrends.build_payload(kw_list,cat=0,timeframe='2019-10-26 2019-11-26',geo=str(p),gprop='')

    if p == regions[0]:
        CombinedNational = pytrends.interest_over_time()
        CombinedNational.rename(columns = {kw_list[0]: regionsname[i]}, inplace=True)
        
    else:
        CombinedNational = pd.concat([CombinedNational,pytrends.interest_over_time()],axis=1)
        CombinedNational.rename(columns = {kw_list[0]: regionsname[i]}, inplace=True)
    i = i +1
   
CombinedNational.drop(CombinedNational[['isPartial']], axis = 1, inplace = True)
CombinedNationalT = CombinedNational.transpose() 
CombinedNationalT.insert(0,'Subregions',Country[0],allow_duplicates = True)

#Saves Dataframe from Pandas to CSV
CombinedNationalT.to_csv('W:\googletrendz.csv',sep=',',na_rep='0')

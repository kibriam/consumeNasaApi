import functools

data = [
    {
        "camis": "50056419",
        "dba": "QUEENS SEAFOOD RESTAURANT",
        "boro": "Queens",
        "building": "8222",
        "street": "45TH AVE",
        "zipcode": "11373",
        "phone": "7184783330",
        "cuisine_description": "Chinese",
        "inspection_date": "2017-04-11T00:00:00.000",
        "action": "Violations were cited in the following area(s).",
        "violation_code": "04L",
        "violation_description": "Evidence of mice or live mice present in facility's food and/or non-food areas.",
        "critical_flag": "Y",
        "score": "16",
        "record_date": "2019-08-03T06:03:22.000",
        "inspection_type": "Cycle Inspection / Initial Inspection",
        "latitude": "40.741633416978",
        "longitude": "-73.88261186975",
        "community_board": "404",
        "council_district": "25",
        "census_tract": "048500",
        "bin": "4038416",
        "bbl": "4015360210",
        "nta": "QN50"
    },
    {
        "camis": "41343370",
        "dba": "LA SUPERIOR",
        "boro": "Brooklyn",
        "building": "295",
        "street": "BERRY STREET",
        "zipcode": "11249",
        "phone": "7183885988",
        "cuisine_description": "Mexican",
        "inspection_date": "2016-07-21T00:00:00.000",
        "action": "Establishment Closed by DOHMH.  Violations were cited in the following area(s) and those requiring immediate action were addressed.",
        "violation_code": "04C",
        "violation_description": "Food worker does not use proper utensil to eliminate bare hand contact with food that will not receive adequate additional heat treatment.",
        "critical_flag": "Y",
        "score": "51",
        "record_date": "2019-08-03T06:03:22.000",
        "inspection_type": "Cycle Inspection / Initial Inspection",
        "latitude": "40.713597801062",
        "longitude": "-73.963726020332",
        "community_board": "301",
        "council_district": "34",
        "census_tract": "055100",
        "bin": "3321289",
        "bbl": "3024170006",
        "nta": "BK73"
    },
    {
        "camis": "50033451",
        "dba": "INDUSTRY KITCHEN",
        "boro": "Manhattan",
        "building": "70",
        "street": "SOUTH ST",
        "zipcode": "10005",
        "phone": "2128715602",
        "cuisine_description": "American",
        "inspection_date": "2016-05-12T00:00:00.000",
        "action": "Violations were cited in the following area(s).",
        "violation_code": "10F",
        "violation_description": "Non-food contact surface improperly constructed. Unacceptable material used. Non-food contact surface or equipment improperly maintained and/or not properly sealed, raised, spaced or movable to allow accessibility for cleaning on all sides, above and underneath the unit.",
        "critical_flag": "N",
        "score": "8",
        "grade": "A",
        "grade_date": "2016-05-12T00:00:00.000",
        "record_date": "2019-08-03T06:03:22.000",
        "inspection_type": "Cycle Inspection / Initial Inspection",
        "latitude": "40.704872302248",
        "longitude": "-74.00531270385",
        "community_board": "101",
        "council_district": "01",
        "census_tract": "000700",
        "bin": "1087761",
        "bbl": "1000360030",
        "nta": "MN25"
    }
]


# filter, Keep only records which are critical
# critcalRecords = list(filter(lambda x: x['critical_flag'] == 'Y', data))
# print(critcalRecords)

# reduce.. Find maximum score among all entries.
# maxScore = functools.reduce(lambda x, y: max(x['score'], y['score']), data)
# print(maxScore)



# filter, Keep only records which are critical
# critcalRecords = list(filter(lambda x: x['boro'] == 'Queens', data))
# print(critcalRecords)

#  list comprehension, Keep only records with Mexican cuisine
# mexicanRecords = [x for x in data if x['cuisine_description'] == 'Mexican']
# print(mexicanRecords)

# create a list of camis and their scores only
subList = list(map(lambda x: {'camis': x['camis'], 'score': x['score']}, data))
print(subList)

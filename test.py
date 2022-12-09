import csv
independent = ['fasting','intermittent fasting','meat','fish','vegetable','fruit','legumes','grains',
                   'fats','saturated','refined sugars','dairy','nuts','Mediterranean','Vegetarian',
                   'Plant-based','Gluten fee','Vegan','Keto','Dairy Free','Low Fat','Okinawan',
                   'Alternate Healthy Eating Index','general exercise','aerobic/cardio exercise',
                   'muscle strengthening','resistance training','stretching','bone strengthening',
                   'Sleep Amount','Sleep quality','Stress Reduction relaxation','Stress meditation',
                   'mindfulness','tai chi','breathing','Stress distraction','Stress Induction sauna bathing',
                   'Stress Induction cold','Stress Induction heat','Calcium','Dietary Fiber','Fat','Saturated fat',
                   'Protein','Magnesium','Manganese','Phosphorus','Potassium','Vitamin A','Vitamin C','Vitamin D',
                   'Vitamin K','Biotin','Chloride','Chromium','Copper','Folate/Folic Acid','Molybdenum','Niacin (B3)',
                   'Pantothenic Acid','Riboflavin (B2)','Selenium','Sodium','Thiamin (B1)','Total carbohydrate',
                   'Added sugars','Choline','Vitamin B6','Vitamin B12','Vitamin E','Zinc','Cholesterol','Iodine',
                   'Iron','Nickel','Ashwagandha','Turmeric','Garlic','Matcha/green tea','fish oil/omega 3','plant sterols',
                   'NMN','NR','Calcium AKG','Alpha lipoic acid','fisetin','quercetin','PQQ','collagen peptides',
                   'hyalauronic acid','chlorella','spirulina','resveratrol','CoQ10','probioltics','melatonin','Acetyl-L-carnitine',
                   'olive oil','lutein','milk thistle','spermidine','creatine','trimethyl glycine']
dependent = ['lifespan', 'all-cause mortality', 'Disease', 'weight/BMI', 'Biological systems',
             'cardiovasular/ heart', 'digestive', 'endocrine', 'sensory system', 'immune and hematology',
             'lymphatic', 'muscular system', 'skeletal system/bones', 'nervous system/brain', 'reproductive system',
             'respiratory system/lungs', 'integumentary system/skin', 'urinary system', 'Performance', 'Physical',
             'mental', 'stress', 'happiness', 'depression', 'genomic instabilitry', 'telomere attrition',
             'epigenetic alteration',
             'loss of proteostasis', 'deregulated nutrient sensing', 'mitochondrial dysfunction', 'cellular senescence',
             'stem cell exhaustion', 'altered intercellular communication']
for str in independent:
    for str2 in dependent:
        print(str + str2)
def write_data_to_file(query, data_list, filename):
    fields = ['KeyWord','Title','Authors','Abstract','Link']
    query = query
    filename = 'table/' + filename
    data_list = data_list
    with open(filename,'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(data_list)
write_data_to_file("name",[],"name")
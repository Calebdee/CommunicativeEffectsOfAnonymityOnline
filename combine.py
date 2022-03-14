import json
import glob

result = []                                         #list that will store the results of all Json 
for f in glob.glob("*.json"):                       #here you will loop over multiple Json files
    with open(f, "rb", encoding='utf-16',errors='ignore') as infile:                    
        result.append(json.load(infile, strict=False))            #here appending the list with Jason content 

with open("merged_file.json", "wb") as outfile:    #filling the resultant file with Jason content
     json.dump(result, outfile, indent = 4)                 #json.dump will fill outpu
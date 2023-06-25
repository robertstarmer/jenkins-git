

import json
import sys


if __name__ == "__main__":
    #Creating a Dictionary
    mystock = {
    "Product": "Earphone",
    "Price": 800,
    "Quantity": 50,
    "InStock" : "Yes"
    }
    mystock['InStock'] = {'Product': 'Earphone', 'Price': 800, 'Quantity': 50, 'InStock': 'Yes'}
    with open("output.json",'w') as f:
        json.dump(mystock,f)

    # print(json.dumps(mystock))

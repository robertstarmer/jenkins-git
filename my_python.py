

import json
import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-mos_tasks_filename", required=False, type=str, default="mos_tasks.json")
    parser.add_argument("-skip_mos_tasks_print", required=False, action='store_true')

    args = parser.parse_args()
    # Creating a Dictionary
    mystock = {
        "Product": "Earphone",
        "Price": 800,
        "Quantity": 50,
        "InStock": "Yes"
    }
    mystock['InStock'] = {'Product': 'Earphone', 'Price': 800, 'Quantity': 50, 'InStock': 'Yes'}
    with open(args.mos_tasks_filename, 'w') as f:
        json.dump(mystock, f)

    # print(json.dumps(mystock))

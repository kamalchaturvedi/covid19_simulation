# -*- coding: utf-8 -*-
from dataflows import load, add_metadata, printer, dump_to_path, Flow
from shutil import rmtree
from pathlib import Path
BASE_URL='https://raw.githubusercontent.com/datasets/covid-19/master/data/'
CONFIRMED='us_confirmed.csv'
DATA_DIR='simulation_data'
def get_data_files():
    flow = Flow(
        # Load inputs
        load(f'{BASE_URL}{CONFIRMED}', format='csv', ),
        # Process them (if necessary)
        # Save the results
        add_metadata(name=DATA_DIR, title='''us_confirmed.csv'''),
        dump_to_path(DATA_DIR),
    )
    flow.process()
    print("received data")
    return 1

def delete_data_files():
    try:
        parent_path = Path(__file__).parent.parent.parent
        print(parent_path)
        rmtree(f'{parent_path}/{DATA_DIR}')
    except OSError as e:
        print("Error: %s : %s" % (DATA_DIR, e.strerror))

def run():
    get_data_files()
    delete_data_files()
if __name__ == "__main__":
    run()

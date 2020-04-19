# -*- coding: utf-8 -*-
from dataflows import load, add_metadata, printer, dump_to_path, Flow
from shutil import rmtree
from pathlib import Path
from pandas import read_csv
from matplotlib import pyplot
from covid19_simulation.model import CovidModel
BASE_URL='https://raw.githubusercontent.com/datasets/covid-19/master/data/'
WORLD_WIDE='worldwide-aggregated.csv'
KEY_COUNTRIES='key-countries-pivoted.csv'
DATA_DIR='simulation_data'
def get_data_file(filename):
    flow = Flow(
        # Load inputs
        load(f'{BASE_URL}{filename}', format='csv', ),
        # Save the results
        add_metadata(name=f'{filename}', title=f'{filename}'),
        dump_to_path(f'{DATA_DIR}/{filename}'),
    )
    flow.process()
    print(f'received file {filename}')
    return 1

def plot_data(filename):
    time_series = read_csv(f'{DATA_DIR}/{filename}/{filename}', header='infer',parse_dates=True, index_col=0)
    print(time_series.head)
    time_series.plot()
    pyplot.show()

def delete_data_files():
    try:
        parent_path = Path(__file__).parent.parent.parent
        print(parent_path)
        rmtree(f'{parent_path}/{DATA_DIR}')
    except OSError as e:
        print("Error: %s : %s" % (DATA_DIR, e.strerror))

def run():
    #get_data_file(WORLD_WIDE)
    #get_data_file(KEY_COUNTRIES)
    # plot_data(WORLD_WIDE)
    # plot_data(KEY_COUNTRIES)
    model = CovidModel()
    for i in range(0,14):
        infectiousness = model.infectiousnessModel()
        print(infectiousness)
    model.plotInfectiousness()
    delete_data_files()
if __name__ == "__main__":
    run()

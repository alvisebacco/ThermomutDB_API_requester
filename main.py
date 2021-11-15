# ALVISE BACCO
# THERMOMUT API  requester

import requests
from colorama import Fore
import json


class QueryToThermoMutDB:
    def __init__(self):

        # BASE URL

        self.base_url = 'http://biosig.unimelb.edu.au/thermomutdb/api/v1'

        # Variant information

        self.finds_data_by_three_letter_mutation_code_API = '/VariantInformation/mutation_code/'
        self.finds_data_by_organism_API = '/VariantInformation/source/'
        self.finds_data_by_uniprot_API = '/VariantInformation/uniprot/'

        # Thermodynamic Data

        self.finds_data_thermo_data_from_ddg_interval_API = '/ThermodynamicData/ddg/from/'
        self.finds_data_by_range_of_delta_Tm_API = '/ThermodynamicData/dtm/'
        self.find_data_by_experimental_effect_API = '/ThermodynamicData/effect/'

    def finds_data_by_three_letter_mutation_code(self, mutation_code):
        api = self.base_url + self.finds_data_by_three_letter_mutation_code_API + mutation_code
        response_obj = self.responder(api)
        for key in response_obj:
            print(Fore.BLUE + 'Protein name: ' + str(key['protein']['name']))
            print(Fore.BLUE + 'Source name: ' + str(key['protein']['source']['name']))
            print(Fore.BLUE + 'Uniprot: ' + str(key['protein']['uniprot']))
            print(Fore.BLUE + 'Mutation Code: ' + str(key['mutation_code']))
            print(Fore.BLUE + 'Mutation Type: ' + str(key['mutation_type']))
            print(Fore.BLUE + 'Mutation Based: ' + str(key['mutation_based']))
            print(Fore.BLUE + 'Blosum62: ' + str(key['blosum62']))
            print(Fore.BLUE + 'neu: ' + str(key['neu']))
            print(Fore.BLUE + 'ddg: ' + str(key['ddg']))
            print(Fore.BLUE + 'phi: ' + str(key['phi']))
            print(Fore.BLUE + 'psi: ' + str(key['psi']))
            print(Fore.BLUE + 'sst: ' + str(key['sst']))
            print(Fore.BLUE + 'rsa: ' + str(key['rsa']))
            print(Fore.BLUE + 'Mutated chain ' + str(key['mutated_chain']))
            print(Fore.RED + 'Temperature: ' + str(key['temperature']))
            print(Fore.BLUE + 'pH: ' + str(key['ph']))
            print(Fore.YELLOW + '-----------------------------------------------------------------------')
            print(Fore.YELLOW + '| ' +
                  Fore.RED +
                  'Free Gibbs Energy (ΔΔG) from wild-type: ' +
                  str(key['ddg']) +
                  ' kcal/mol' + Fore.YELLOW + '               |')
            print(Fore.YELLOW + '-----------------------------------------------------------------------')

    # EXAMPLE: pdb
    def finds_data_by_organism(self, organism):
        api = self.base_url + self.finds_data_by_organism_API + organism
        response_obj = self.responder(api)
        for info in response_obj:
            print(Fore.BLUE + 'Protein: ' + str(info['protein']))
            print(Fore.BLUE + 'Blosum62: ' + str(info['blosum62']))
            print(Fore.BLUE + 'PDB_wild: ' + str(info['PDB_wild']))
            print(Fore.BLUE + 'Reference: ' + str(info['reference']))
            print(Fore.BLUE + 'Mutation type: ' + str(info['mutation_type']))
            print(Fore.BLUE + 'Mutation code: ' + str(info['mutation_code']))
            print(Fore.RED + 'Temperature: ' + str(info['temperature']))
            print(Fore.BLUE + 'Uniprot: ' + str(info['uniprot']))
            print(Fore.YELLOW + '-----------------------------------------------------------------------')
            print(Fore.YELLOW + '| ' +
                  Fore.RED +
                  'Free Gibbs Energy (ΔΔG) from wild-type: ' +
                  str(info['ddg']) +
                  ' kcal/mol' + Fore.YELLOW + '               |')
            print(Fore.YELLOW + '-----------------------------------------------------------------------')

    def finds_data_by_uniprot(self, uniprot_code):
        api = self.base_url + self.finds_data_by_uniprot_API + uniprot_code
        response_obj = self.responder(api)
        for key in response_obj:
            print(Fore.BLUE + 'Name: ' + str(key['protein']['name']))
            print(Fore.BLUE + 'Sequence: ' + str(key['protein']['sequence']))
            print(Fore.BLUE + 'Source: ' + str(key['protein']['source']['name']))
            print(Fore.BLUE + 'Mutationcode: ' + str(key['mutation_code']))
            print(Fore.BLUE + 'Blosum62: ' + str(key['blosum62']))
            print(Fore.BLUE + 'ddg: ' + str(key['ddg']))
            print(Fore.RED + 'Temperature: ' + str(key['temperature']))
            print(Fore.BLUE + 'pH: ' + str(key['ph']))
            print(Fore.YELLOW + '-----------------------------------------------------------------------')
            print(Fore.YELLOW + '| ' +
                  Fore.RED +
                  'Free Gibbs Energy (ΔΔG) from wild-type: ' +
                  str(key['ddg']) +
                  ' kcal/mol' + Fore.YELLOW + '               |')
            print(Fore.YELLOW + '-----------------------------------------------------------------------')

    def finds_thermodynamic_data_from_ddg(self, _from, _to):
        api = self.base_url + self.finds_data_thermo_data_from_ddg_interval_API + _from + '/to/' + _to
        response_obj = self.responder(api)
        for key in response_obj:
            print(Fore.BLUE + 'Name: ' + key['protein']['name'])
            print(Fore.BLUE + 'Uniprot: ' + key['protein']['uniprot'])
            print(Fore.BLUE + 'Sequence: ' + key['protein']['sequence'])
            print(Fore.BLUE + 'PDB mutant: ' + str(key['pdb_mutant']))
            print(Fore.BLUE + 'Blosunm62: ' + str(key['blosum62']))
            print(Fore.RED + 'Temperature: ' + str(key['temperature']))
            print(Fore.BLUE + 'pH: ' + str(key['ph']))
            print(Fore.YELLOW + '-----------------------------------------------------------------------')
            print(Fore.YELLOW + '| ' +
                  Fore.RED +
                  'Free Gibbs Energy (ΔΔG) from wild-type: ' +
                  str(key['ddg']) +
                  ' kcal/mol' + Fore.YELLOW + '               |')
            print(Fore.YELLOW + '-----------------------------------------------------------------------')

    def finds_data_by_range_of_delta_tm(self, _from, _to):
        api = self.base_url + self.finds_data_by_range_of_delta_Tm_API + 'from/' + _from + '/to/' + _to
        response_obj = self.responder(api)
        for key in response_obj:
            print(Fore.BLUE + 'Name: ' + key['protein']['name'])
            print(Fore.BLUE + 'Uniprot: ' + key['protein']['uniprot'])
            print(Fore.BLUE + 'Sequence: ' + key['protein']['sequence'])
            print(Fore.BLUE + 'PDB mutant: ' + str(key['pdb_mutant']))
            print(Fore.BLUE + 'Blosunm62: ' + str(key['blosum62']))
            print(Fore.RED + 'Temperature: ' + str(key['temperature']))
            print(Fore.BLUE + 'pH: ' + str(key['ph']))
            print(Fore.YELLOW + '-----------------------------------------------------------------------')
            print(Fore.YELLOW + '| ' +
                  Fore.RED +
                  'Free Gibbs Energy (ΔΔG) from wild-type: ' +
                  str(key['ddg']) +
                  ' kcal/mol' + Fore.YELLOW + '               |')
            print(Fore.YELLOW + '-----------------------------------------------------------------------')

    def what_can_i_do(self):
        print(Fore.YELLOW + '-----' + Fore.RED + 'THERMOMUT' + Fore.BLUE + 'DB' + Fore.YELLOW + '-----\n')
        print(Fore.GREEN + 'VARIANT INFORMATION:')
        print(Fore.MAGENTA + '1. Finds data by three-letter mutation code')
        print(Fore.MAGENTA + '2. Finds data by organism')
        print(Fore.MAGENTA + '3. Finds data by uniprot code')

        print(Fore.GREEN + 'THERMODYNAMIC DATA:')
        print(Fore.MAGENTA + '4. Finds data by range of DDG: ')
        print(Fore.MAGENTA + '5. Finds data by range of Delta Tm: ')
        choice = input(Fore.GREEN + '> ')
        try:
            choice = int(choice)
        except ValueError as cast_error:
            print(Fore.RED + 'Only numbers are allowed! :/ ERROR: ' + str(cast_error))

        if choice == 1:
            print(Fore.LIGHTCYAN_EX + '> Example: D36N')
            mutation_code = input(Fore.MAGENTA + 'Mutation code: ')
            QueryToThermoMutDB().finds_data_by_three_letter_mutation_code(mutation_code)
        elif choice == 2:
            print(Fore.LIGHTCYAN_EX + '> Example: Escherichia coli | Enterobacteria phage T4 | Homo sapiens')
            pdb = input(Fore.MAGENTA + 'Organism: ')
            QueryToThermoMutDB().finds_data_by_organism(pdb)
        elif choice == 3:
            print(Fore.LIGHTCYAN_EX + '> Example: P04637')
            uniprot_code = input(Fore.MAGENTA + 'Uniprot code: ')
            QueryToThermoMutDB().finds_data_by_uniprot(uniprot_code)
        elif choice == 4:
            print(Fore.LIGHTCYAN_EX + '> Example: 1 to 100')
            ddg_range = input(Fore.MAGENTA + 'Range: ')
            _from, _to = self.split_range(ddg_range)
            QueryToThermoMutDB().finds_thermodynamic_data_from_ddg(_from, _to)

        elif choice == 5:
            print(Fore.LIGHTCYAN_EX + '> Example: 185 to 220')
            delta_t = input(Fore.MAGENTA + 'Range: ')
            _from, _to = self.split_range(delta_t)
            QueryToThermoMutDB().finds_data_by_range_of_delta_tm(_from, _to)

    @staticmethod
    def split_range(_range):
        if ' to ' in _range:
            ddg_range = str(_range).split(' to ')
            _from = ddg_range[0]
            _to = ddg_range[1]
            return _from, _to
        else:
            print('Invalid format, use 1to100 format.')

    @staticmethod
    def responder(api):
        response = requests.get(api)
        decoded_response = response.content.decode("utf-8")
        response_obj = json.loads(decoded_response)
        return response_obj


if __name__ == '__main__':
    while True:
        QueryToThermoMutDB().what_can_i_do()

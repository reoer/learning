import os
import csv

folder_path = 'data/*'
outcome_path = 'Intermediate/*'
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        with open(os.path.join(folder_path, filename), newline='') as f:
            data = list(csv.reader(f))
#            print(data)
            data2 = data[1:len(data)]
            first_elements = []
            int_list = []
            for row in data2:
                first_elements.append(row[0])
                int_list.append(list(map(int, row[2:-2])))
            my_list = [[first_elements[i]] + int_list[i] for i in range(len(first_elements))]
            result = {}
            for row in my_list:
                if row[0] not in result:
                    result[row[0]] = row[1:]
                else:
                    if sum(row[1:]) > sum(result[row[0]]):
                        result[row[0]] = row[1:]
                        with open(filename, 'w', newline='') as outcomes:
                            writer = csv.writer(outcomes)
#                            writer.writerow([os.path.join(outcome_path, filename),'variants_effect_3_prime_UTR_variant,variants_effect_5_prime_UTR_variant,variants_effect_downstream_gene_variant,variants_effect_exon_region,variants_effect_intron_variant,variants_effect_protein_protein_contact,variants_effect_splice_acceptor_variant,variants_effect_splice_donor_variant,variants_effect_splice_region_variant,variants_effect_upstream_gene_variant'])
                            for key, value in result.items():
                                writer.writerow([key, value])

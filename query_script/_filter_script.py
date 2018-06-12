
# coding: utf-8

# In[1]:

import os
import sys
sys.path.append('inst/python')
import helper
import query
import csv


# In[2]:


path = 'data/filtered/'
# set = ['G1_clustered_genes_annotations.tab','G2_clustered_genes_annotations.tab','G5_clustered_genes_annotations.tab','G6_clustered_genes_annotations.tab']
set = ['G1_clustered_genes_annotations.tab']

unique_gene_list = []
for data in set:
    gene_list = []
    with open(path + data, newline='') as input_file:
        dictReader = csv.DictReader(input_file, delimiter = "\t")
        for line in dictReader:
            for kegg_id in line['KEGG_ko'].split('|'):
                if not(kegg_id in unique_gene_list): unique_gene_list.append(kegg_id)
            for kegg_id in line['KEGG_module'].split('|'):
                if not(kegg_id in unique_gene_list): unique_gene_list.append(kegg_id)
            for kegg_id in line['KEGG_pathway'].split('|'):
                if not(kegg_id in unique_gene_list): unique_gene_list.append(kegg_id)
        print(len(unique_gene_list))
        print(len(gene_list))
#     filtered_list = list(filter(lambda gene: 750<int(gene['#gene'].split('_')[3]), gene_list))
#     print('%d: removed %d genes which length < 750 from %d genes' % (len(filtered_list), len(gene_list)-len(filtered_list), len(gene_list)))
#     filtered_set.append(filtered_list)

# In[3]:




# In[4]:


for i in range(3):
    if not os.path.exists(path+'filtered/'):
        os.makedirs(path+'filtered/')
    with open(path+'filtered/'+set[i], 'w',newline = '') as filtered:
        dictWriter = csv.DictWriter(filtered, delimiter = '\t', fieldnames=filtered_set[i][0].keys())
        dictWriter.writeheader()
        dictWriter.writerows(filtered_set[i])


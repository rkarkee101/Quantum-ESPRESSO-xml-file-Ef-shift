# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:15:43 2023

@author: rijan
"""
from bs4 import BeautifulSoup

def process_eigenvalues(eigenvalues_data):
    updated_values = []
    for value in eigenvalues_data:
        value = float(value)
        if value > 0.05:   #### units are in Hartree 1 Hartree = 27.2114 eV
            value -=  0.01   ########## units are in Hartree 
        updated_values.append(value)
    return updated_values

def process_xml(xml_file):
    with open(xml_file, 'r') as file:
        soup = BeautifulSoup(file, 'xml')
        eigenvalues_tags = soup.find_all('eigenvalues')
        for index, eigenvalues_tag in enumerate(eigenvalues_tags, start=1):
            eigenvalues_data = eigenvalues_tag.text.strip().split()
            updated_values = process_eigenvalues(eigenvalues_data)
            eigenvalues_tag.string = ' '.join(str(value) for value in updated_values)

        with open(f'updated_{xml_file}', 'w') as output_file:
            output_file.write(soup.prettify())

if __name__ == "__main__":
    xml_file = "scf.xml"
    process_xml(xml_file)



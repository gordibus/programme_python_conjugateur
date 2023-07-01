#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 20:53:01 2023

@author: gordibus
"""
def conjugaison():
    verb = input("Entrez votre verbe au premier groupe (qui termine par -er): ")
    temps = input("Entrez le temps auquel vous souhaitez le conjuger (présent (p), imparfait (imp) ou futur(f)): ")
    mode = input("Entrez le mode que vous souhaitez soit l'indicatif soit le conditionnel(ind ou cond): ")
    personne = input("Entrez la personne (1, 2 ou 3): ")
    nombre = input("Vous souhaitez au singulier ou  au pluriel ? (sg ou pl): ")
    if verb[-2:] == "er":
        stem = verb[:-2]
    else:
        return "Votre verbe n'est pas attribué"
    if temps == "p":
        if mode == "ind":
            endings = ['e', 'es', 'e', 'ons', 'ez', 'ent']
            if personne == '1':
                if nombre == 'sg':
                    return 'Je ' + stem + 'e'
                elif nombre == 'pl':
                    return 'Nous ' + stem + 'ons'
            elif personne == '2':
                if nombre == 'sg':
                    return 'Tu ' + stem + 'es'
                elif nombre == 'pl':
                    return 'Vous ' + stem + 'ez'
            elif personne == '3':
                if nombre == 'sg':
                    return 'Il/Elle ' + stem + 'e'
                elif nombre == 'pl':
                    return 'Ils/Elles ' + stem + 'ent'
        elif mode == 'cond':
            endings = ['erais', 'erais', 'erait', 'erions', 'eriez', 'eraient']
            if personne == '1':
                if nombre == 'sg':
                    return 'Je ' + verb + 'ais'
                elif nombre == 'pl':
                    return 'Nous ' + verb + 'ions'
            elif personne == '2':
                if nombre == 'sg':
                    return 'Tu ' + verb + 'ais'
                elif nombre == 'pl':
                    return 'Vous ' + verb + 'iez'
            elif personne == '3':
                if nombre == 'sg':
                    return 'Il/Elle ' + verb + 'ait'
                elif nombre == 'pl':
                    return 'Ils/Elles ' + verb + 'aient'
        else:
            return 'Mode non valide'
    elif temps == 'omp':
        if mode == 'ind':
            endings = ['ais', 'ais', 'ait', 'ions', 'iez', 'aient']
            if personne == '1':
                if nombre == 'sg':
                    return 'Je ' + stem + 'ais'
                elif nombre == 'pl':
                    return 'Nous ' + stem + 'ions'
            elif personne == '2':
                if nombre == 'sg':
                    return 'Tu ' + stem + 'ais'
                elif nombre == 'pl':
                    return 'Vous ' + stem + 'iez'
            elif personne == '3':
                if nombre == 'sg':
                    return 'Il/Elle ' + stem + 'ait'
                elif nombre == 'pl':
                    return 'Ils/Elles ' + stem + 'aient'
        else:
            return 'Mode non valide'
    elif temps == 'futur':
        if mode == 'ind':
            endings = ['erai', 'eras', 'era', 'erons', 'erez', 'eront']
            if personne == '1':
                if nombre == 'sg':
                    return 'Je ' + verb + 'ai'
                elif nombre == 'pl':
                    return 'Nous ' + verb + 'ons'
            elif personne == '2':
                if nombre == 'sg':
                    return 'Tu ' + verb + 'as'
                elif nombre == 'pl':
                    return 'Vous ' + verb + 'ez'
            elif personne == '3':
                if nombre == 'sg':
                    return 'Il/Elle/On ' + verb + 'a'
                elif nombre == 'pl':
                    return 'Ils/Elles ' + verb + 'ont'
        else:
            return 'Mode non valide'
    else:
        return 'Temps non valide'
print('Bienvenue dans le conjugueur de verbes !')
verbe = conjugaison()
print('Le verbe conjugué est :', verbe)

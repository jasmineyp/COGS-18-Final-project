class Mammals:
#my first main class that contains wildcats and mammals 

    """This is my first main class which contains wildcats and mammals"""
    
    def __init__(self, name, scientific_name, habitat, fun_facts, endangerment_status, reason_for_status, laws, charities):
        self.name = name 
        self.scientific_name = scientific_name 
        self.habitat = habitat 
        self.endangerment_status = endangerment_status 
        self.reason_for_status = reason_for_status 
        self.laws = laws 
        self.charities = charities 


class WildCats(Mammals):
    
    """This subclass inherits from my first main class and lists only wildcats"""
    
    def __init__(self, name, scientific_name, habitat, fun_facts, endangerment_status, reason_for_status, laws, charities):
        super().__init__(name, scientific_name, habitat, fun_facts, endangerment_status, reason_for_status, laws, charities)

bengal_tiger = WildCats("Bengal Tiger", "Panthera Tigris Tigris", "India", "Every bengal tiger has a unique set of stripes and no two are the same!",
                        "Endangered", "poaching and loss of habitat", "Convention on International Trade in Endangered Species of Wild Fauna and Flora (CITES)",
                        "WWF")
amur_tiger = WildCats("Amur Tiger", "Panthera tigris altaica", "Eastern Russia", "~40 Amur Tigers are left in the wild", "Endangered", 
                     "poaching and habitat loss",
                      "Convention on International Trade in Endangered Species of Wild Fauna and Flora (CITES)", "WWF")
iberian_lynx = WildCats("Iberian Lynx", "Lynx Pardinus","the Iberian Peninsula","Adult lynx need to eat a rabbit a day.",
                       "Endangered", "illegal hunting", "There are none.", "WWF")
iriomote_cats = WildCats ("Iriomote Cats", "Prionailurus bengalensis iriomotensis","Iriomote Island, Japan","A large number of Iriomote Cats have been killed by cars",
                         "Endangered", "human Population Growth","There are none.", "Feline Conservation Federation")

class MarineMammals(Mammals):
    def __init__(self, name, scientific_name, habitat, fun_facts, endangerment_status, reason_for_status, laws, charities):
            super().__init__(name, scientific_name, habitat, fun_facts, endangerment_status, reason_for_status, laws, charities)

florida_manatee = MarineMammals("Florida Manatee", "Trichechus manatus latirostris", "King's Bay, Florida", 
                             "Manatees are also known as 'sea cows'", "Endangered",
                             "boat collisions", "Florida is a sanction for manatees", "Bagheera")
vaquita_porpoise = MarineMammals("Vaquita Porpoise", "Phocoenidae", "the Northern Hemisphere", "Porpoises are one of the smallest marine mammals!", "Critically Endangered", "over hunting", "Adopting a vaquita","Porpoise.org")

mammals = [bengal_tiger, amur_tiger, iberian_lynx, iriomote_cats, florida_manatee, vaquita_porpoise]


class Reptiles: 
    """This is my second main class and it only contains reptiles"""
#my second main class     
    
    def __init__(self, name, scientific_name, habitat, fun_facts, endangerment_status, reason_for_status, laws, charities):
        
        self.name = name 
        self.scientific_name = scientific_name 
        self.habitat = habitat 
        self.fun_facts = fun_facts
        self.endangerment_status = endangerment_status 
        self.reason_for_status = reason_for_status 
        self.laws = laws 
        self.charities = charities 
        

hawksbill_turtle = Reptiles("Hawksbill Turtle", "Eretmochelys imbricata","in tropical coral reefs", "Hawksbills are able to eat sponges that are highly toxic to other marine mammals", "Critically endangered", " illegal Wildlife Trade", "Satellite tracking", "WWF")

softshelled_turtle = Reptiles("Yangtze giant softshell turtle", "Rafetus swinhoei", "Vietnam/China", "Its shell is very soft", "Critically endangered", " habitat destruction", "Florida Fish and Wildlife Conservation", "There are none")

radiated_tortoise = Reptiles("Raditated Tortoise", "Astrochelys radiata", "in southern Madagascar", "It gets its name from being yellow", "Critically endangered", " habitat destruction", "Malagasy law", "IUCN")

reptiles = [hawksbill_turtle, softshelled_turtle, radiated_tortoise]

class Birds:
#my third and last main class 

    """This is my third and last main class and it contains different types of birds"""

    def __init__(self, name, scientific_name, habitat, fun_facts, endangerment_status, reason_for_status, laws, charities):
            
        self.name = name 
        self.scientific_name = scientific_name 
        self.habitat = habitat 
        self.fun_facts = fun_facts
        self.endangerment_status = endangerment_status 
        self.reason_for_status = reason_for_status 
        self.laws = laws 
        self.charities = charities 



kakapo = Birds("Kakapo", "Strigops habroptilus","New Zealand", "They are the only birds that do not fly!", "Critically endangered", "hunting", "Under New Zealand Law", "Department of Conservation (DoC)")

crested_ibis = Birds("Crested ibis", "Nipponia nippon", "Asia", "The crested ebis is the world’s most threatened ibis species", "Critically endangered", "habitat destruction", "Law on Protection of Cultural Properties made in 1934", "Sado Japanese Crested Ibis Preservation Center")

california_condor = Birds("California condor", "Gymnogyps californianus", "Northern Arizona", "In early 2007, a California condor laid an egg in Mexico for the first time since at least the 1930s!", "Critically endangered", "poaching", "under california state law", "The Peregrine Fund")

                
birds = [kakapo, crested_ibis, california_condor]  




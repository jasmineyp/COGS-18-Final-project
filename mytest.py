assert WildCats

name = 'hobbes'
scientific_name = 'stuffed animal'
habitat = 'the imagination'
fun_facts = 'i like hot cocoa'
endangerment_status = 'time'
reason_for_status = 'global warming'
laws = 'calvins law'
charities = 'none'

hobbes = WildCats(name, scientific_name, habitat, fun_facts, endangerment_status, reason_for_status, laws, charities)

assert isinstance(hobbes, WildCats)
assert isinstance(hobbes, Mammals)
assert hobbes.name == name
assert hobbes.scientific_name == scientific_name
assert hobbes.habitat = habitat
assert hobbes.endangerment_status = endangerment_status
assert hobbes.reason_for_status = reason_for_status


from bloomfilter import BloomFilter
from random import shuffle

n = 20  # no of items to add
p = 0.05  # false positive probability

bloomf = BloomFilter(n, p)
print("Size of bit array:{}".format(bloomf.size))
print("False positive Probability:{}".format(bloomf.fp_prob))
print("Number of hash functions:{}".format(bloomf.hash_count))

# animal exists
animal_exists = ['Lion', 'Tiger']

# animal extinct
animal_extinct = ['Aurochs',
                  'Cape Lion',
                  'Carolina Parakeet',
                  'Dodo',
                  'Neanderthal',
                  'Quagga',
                  'Saber-Toothed Tiger',
                  'Steller’s Sea Cow',
                  'Tasmanian Tiger',
                  'Woolly Mammoth',
                  'Sumatran Rhino',
                  'Chinese paddlefish',
                  'Yangtze giant softshell turtle',
                  'Indian Cheetah',
                  'Spix Macaw',
                  'Catarina Pupfish',
                  'Indochinese tiger',
                  'West African Black Rhinoceros',
                  'Baiji White Dolphin',
                  'Pyrenean Ibex',
                  'Passenger Pigeon',
                  'Tasmanian Tiger',
                  'Stellers Sea Cow',
                  'Great Auk',
                  'Dodo',
                  'Broad-faced potoroo,'
                  'Eastern hare wallaby',
                  'Lake Mackay hare-wallaby',
                  'Desert rat-kangaroo',
                  'Thylacine',
                  'Toolache wallaby',
                  'Desert bandicoot',
                  'Yallara',
                  'Lesser bilby',
                  'Pig-footed bandicoot',
                  'Crescent nail-tail wallaby',
                  'Red-bellied gracile opossum',
                  'red-bellied gracile mouse opossum',
                  'Nullarbor dwarf bettong',
                  'Stellers sea cow',
                  'Bramble Cay melomys',
                  'Oriente cave rat',
                  'Torres cave rat',
                  'Imposter hutia',
                  'Montane hutia',
                  'Dwarf viscacha',
                  'Galápagos giant rat',
                  'Cuban coney',
                  'Hispaniolan edible rat',
                  'Puerto Rican hutia',
                  'Big-eared hopping mouse',
                  'Darling Downs hopping mouse',
                  'White-footed rabbit-rat',
                  'Capricorn rabbit rat',
                  'Short-tailed hopping mouse',
                  'Long-tailed hopping mouse',
                  'Great hopping mouse',
                  'Saint Lucia pilorie',
                  'Bulldog rat',
                  'Maclears rat',
                  'Fuegian dog',
                  'Baiji',
                  'Yangtze river dolphin',
                  'Dwarf hutia',
                  'Scimitar oryx',
                  'Giant fossa',
                  'Caribbean monk seal',
                  'Japanese sea lion',
                  'Sea mink',
                  'Falkland Islands wolf',
                  'Warrah',
                  'Madagascan dwarf hippopotamus',
                  'Schomburgks deer',
                  'Red gazelle',
                  'Bluebuck',
                  'Aurochs',
                  'Large sloth lemur',
                  'Large Palau flying fox',
                  'Dilophosaurus',
                  'Coelophysis',
                  'Ceratosaurus',
                  'Monolophosaurus',
                  'Spinosaurus',
                  'Allosaurus',
                  'Compsognathus',
                  'Tyrannosaurus rex',
                  'Struthiomimu',
                  'MononykusTherizinosaurus',
                  'OviraptorMicroraptor',
                  'VelociraptorPlateosaurus',
                  'Apatosaurus',
                  'Alamosaurus',
                  'Ankylosaurus',
                  'Stegosaurus',
                  'Iguanodon',
                  'Parasaurolophus',
                  'Triceratops',
                  'Pachycephalosaurus',
                  'Abelisaurus',
                  'Albertosaurus',
                  'Megamouth Shark']

for item in animal_exists:
    bloomf.add(item)

shuffle(animal_exists)
shuffle(animal_extinct)

test_words = animal_exists[:10] + animal_extinct
shuffle(test_words)
for word in test_words:
    if bloomf.check(word):
        if word in animal_extinct:
            print("'{}' is a false positive!".format(word))
        else:
            print("'{}' is probably present!".format(word))
    else:
        print("'{}' is definitely not present!".format(word))

animal = {
    'vertebrado': {
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba' 
        },

        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca'
        }
    },

    'invertebrado': {
        'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta'
        },

        'anelideo': {
            'hematofago': 'sanguessuga',
            'onivoro': 'minhoca'
        }
    }
}

type1 = input()
type2 = input()
type3 = input()

print(animal[type1][type2][type3])

cities = {
    'london': {
        'country': 'united kingdom',
        'population': '9 million',
        'fact': 'It has the biggest jewish coomunity in Europe'
    },
    'turin': {
        'country': 'italy',
        'population': '1 million',
        'fact': 'It was the first capital of Italy'
    },
    'paris': {
        'country': 'france',
        'population': '2 million',
        'fact': 'In 2019 a fire destryed the Notre Dame cathedral'
    },
}

for city, info in cities.items():
    print(f"\nInfo about {city.title()}:")
    print(f"\n\t- Country: {info['country'].title()}.\n\t- Population: {info['population']}.\n\t- Fact: {info['fact']}.")
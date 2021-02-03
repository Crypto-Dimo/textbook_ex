favourite_places = {
    'matt': ['rome', 'new york', 'prague'],
    'susan': ['berlin', 'paris', 'oslo'],
    'scott': ['madrid', 'caracas', 'buenos aires'],
}

for name, places in favourite_places.items():
    print(f"\n{name.title()}'s favourite places are:")
    for place in places:
        print(f"\t-{place.title()};")
        
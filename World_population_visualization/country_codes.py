from pygal.maps.world import COUNTRIES


def get_country_codes(country_name):
    """ Return 2-digit country code for given country"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    # If the country wasn't found, return None.
    return None


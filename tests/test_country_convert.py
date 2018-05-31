#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2018 TUNE, Inc. (http://www.tune.com)
#  @namespace logging_mv_integrations

import pytest

from pycountry_convert import (
    map_countries,
    country_alpha2_to_country_name,
    country_alpha2_to_continent_code,
    country_alpha3_to_country_alpha2,
    country_name_to_country_alpha2,
    country_name_to_country_alpha3,
    country_alpha3_to_country_name
)

class TestCountryConvert():
    def test_get_countries(self):
        cn_dict = map_countries()
        assert(cn_dict)
        assert(len(cn_dict) > 0)

    def test_country_alpha2_to_continent(self):
        cn_continent = country_alpha2_to_continent_code('US')
        assert(cn_continent)
        assert(cn_continent == 'NA')

        cn_continent = country_alpha2_to_continent_code('AU')
        assert(cn_continent)
        assert(cn_continent == 'OC')

        cn_continent = country_alpha2_to_continent_code('NZ')
        assert(cn_continent)
        assert(cn_continent == 'OC')

        cn_continent = country_alpha2_to_continent_code('JP')
        assert(cn_continent)
        assert(cn_continent == 'AS')

    def test_country_alpha2_to_country_name(self):
        cn_name = country_alpha2_to_country_name('JP')
        assert(cn_name)
        assert(cn_name == 'Japan')

        cn_name = country_alpha2_to_country_name('KR')
        assert(cn_name)
        assert(cn_name == 'Korea, Republic of')

        cn_name = country_alpha2_to_country_name('RU')
        assert(cn_name)
        assert(cn_name == 'Russian Federation')

    def test_country_name_to_country_alpha2(self):
        cn_a2_code = country_name_to_country_alpha2('USA')
        assert(cn_a2_code)
        assert(cn_a2_code == 'US')

        cn_a2_code = country_name_to_country_alpha2('United States')
        assert(cn_a2_code)
        assert(cn_a2_code == 'US')

        cn_a2_code = country_name_to_country_alpha2('South Korea')
        assert(cn_a2_code)
        assert(cn_a2_code == 'KR')

        cn_a2_code = country_name_to_country_alpha2('Russian Federation')
        assert(cn_a2_code)
        assert(cn_a2_code == 'RU')

    def test_country_name_to_country_alpha3(self):
        cn_a3_code = country_name_to_country_alpha3('USA')
        assert(cn_a3_code)
        assert(cn_a3_code == 'USA')

        cn_a3_code = country_name_to_country_alpha3('United States')
        assert(cn_a3_code)
        assert(cn_a3_code == 'USA')

        cn_a3_code = country_name_to_country_alpha3('South Korea')
        assert(cn_a3_code)
        assert(cn_a3_code == 'KOR')

        cn_a3_code = country_name_to_country_alpha3('Russian Federation')
        assert(cn_a3_code)
        assert(cn_a3_code == 'RUS')

    def test_country_alpha3_to_country_alpha2(self):
        cn_a2_code = country_alpha3_to_country_alpha2('USA')
        assert(cn_a2_code)
        assert(cn_a2_code == 'US')

        cn_a2_code = country_alpha3_to_country_alpha2('RUS')
        assert(cn_a2_code)
        assert(cn_a2_code == 'RU')

    def test_country_alpha3_to_country_name(self):
        cn_name = country_alpha3_to_country_name('USA')
        assert (cn_name)
        assert (cn_name == 'United States')

        cn_name = country_alpha3_to_country_name('JPN')
        assert (cn_name)
        assert (cn_name == 'Japan')

        cn_name = country_alpha3_to_country_name('KOR')
        assert (cn_name)
        assert (cn_name == 'Korea, Republic of')

        cn_name = country_alpha3_to_country_name('RUS')
        assert (cn_name)
        assert (cn_name == 'Russian Federation')

    def test_invalid_country_alpha2(self):
        with pytest.raises(KeyError) as e_key:
            country_alpha2_to_continent_code('AA')
        assert "Invalid Country Alpha-2 code: 'AA'" in str(e_key)

    def test_invalid_country_alpha3(self):
        with pytest.raises(KeyError) as e_key:
            country_alpha3_to_country_name('ZZZ')
        assert "Invalid Country Alpha-3 code: 'ZZZ'" in str(e_key)
def fetch_deforestation_data(start_year, end_year, region):
    # Mock data for different years
    if start_year == '2000':
        return {
            "deforestation_areas": [
                {"lat": -3.4653, "lon": -62.2159, "deforested_hectares": 1200}
            ]
        }
    elif start_year == '2010':
        return {
            "deforestation_areas": [
                {"lat": -2.1542, "lon": -55.1266, "deforested_hectares": 900}
            ]
        }
    elif start_year == '2020':
        return {
            "deforestation_areas": [
                {"lat": -3.4653, "lon": -64.2159, "deforested_hectares": 700}
            ]
        }
    else:
        return {
            "deforestation_areas": [
                {"lat": -3.4653, "lon": -62.2159, "deforested_hectares": 1000}
            ]
        }

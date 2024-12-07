# type: ignore
# flake8: noqa
# Convert country names to ISO3 codes
emissions_long_1990_2022["country_code"] = coco.convert(
    emissions_long_1990_2022["country"], to="ISO3"
)

fig_map = px.choropleth(
    emissions_long_1990_2022,
    locations="country_code",
    color="emissions",
    hover_name="country",
    animation_frame="year",
    title="Global CO2 Emissions (1990-2022)",
)

fig_map.show()



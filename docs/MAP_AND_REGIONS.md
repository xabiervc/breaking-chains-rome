# Map and Regions

## Fixed scale

The gameplay map contains 300 square miles of explorable land and city space. It is a deliberate abstraction of the empire, not a real-scale representation of all imperial territory.

## Region allocation

| Region | Area | Main hubs | Main travel mode |
|---|---:|---|---|
| Italia | 54 sq mi | Rome, Capua, Ostia | Roads, Tiber, coastal ships |
| Sicilia | 25 sq mi | Syracuse, Agrigentum | Roads, coastal ships |
| Graecia | 26 sq mi | Athens, Corinth, Thessalonica | Roads, Aegean ships |
| Thrace | 32 sq mi | Byzantium, Philippopolis | Roads, military routes |
| Asia Minor | 32 sq mi | Ephesus, Smyrna, Tarsus | Roads, coastal ships |
| Syria | 34 sq mi | Antioch, Damascus | Roads, caravans |
| Aegyptus | 30 sq mi | Alexandria, Memphis | Nile, roads, ships |
| Africa Proconsularis | 24 sq mi | Carthage, Utica | Roads, coastal ships |
| Hispania | 28 sq mi | Tarraco, Corduba, Gades | Roads, river routes |
| Gallia Narbonensis | 15 sq mi | Massilia, Nemausus | Roads, Rhône |

## Travel formula

`travel_minutes = route_units × terrain_factor × season_factor × transport_factor × weather_factor`

The route graph, factors, and rounding rules must be stored in data files. A route with the same inputs always produces the same duration and cost.

## Unlock rules

- Local movement is available from the beginning of each visited region.
- Long-distance routes unlock after physical discovery or a documented introduction mission.
- Fast travel requires a known route, a valid identity or escort, money, and no active lockdown.

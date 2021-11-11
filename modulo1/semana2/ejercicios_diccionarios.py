medallero = {"USA":{"Gold":36,"Silver":28,"Bronze":25},
            "MEX":{"Gold":16,"Silver":11,"Bronze":26},
            "CAN":{"Gold":14,"Silver":26,"Bronze":18},
            "BRA":{"Gold":13,"Silver":12,"Bronze":23},
            "CUB":{"Gold":10,"Silver":10,"Bronze": 9},
            "ARG":{"Gold":10,"Silver": 7,"Bronze":11},
            "COL":{"Gold": 8,"Silver": 9,"Bronze":12},
            "DOM":{"Gold": 4,"Silver": 6,"Bronze": 9},
            "PER":{"Gold": 4,"Silver": 2,"Bronze": 6},
            "CHI":{"Gold": 3,"Silver": 5,"Bronze": 5}}

# 10.- Cuantas medallas de oro tiene PER?
oro_per = medallero["PER"]['Gold']
print(oro_per)

# 11.- Cuantas medallas de plata tiene CUBA?
plata_cub = medallero["CUB"]["Silver"]
print(plata_cub)
# 12.- Cuantas medallas de oro tienen en conjunto COLOMBIA Y BRASIL
oro_col = medallero["COL"]["Gold"]
oro_bra = medallero["BRA"]["Gold"]
print(oro_col + oro_bra)
# 13.- En cuantas medallas de oro supera USA a BRASIL
oro_usa = medallero["USA"]["Gold"]
oro_bra = medallero["BRA"]["Gold"]
print(oro_usa - oro_bra)

#11.- cuantas medallas tiene CUBA?
print("Medallas de plata por CUBA:",medallero["CUB"]["Silver"])
 # 12.- Cuantas medallas de oro tienen en conjunto COLOMBIA Y BRASIL
medallas_total = sum(medallero["COL"].values())+sum(medallero["BRA"].values())
print("Brazil y Colombia obtuvieron",medallas_total,"medallas en conjunto")
# 13.- En cuantas medallas de oro supera USA a BRASIL
diferencia = medallero["USA"]["Gold"]-medallero["BRA"]["Gold"]
print("USA supera en",diferencia,"medallas de oro a Brazil")

# 11.- Cuantas medallas de plata tiene Cuba?
plata_cub = medallero["CUB"]["Silver"]
print(plata_cub)
# 12.- Cuantas medallas de oro tienen en conjunto COLOMBIA Y BRASIL
medallas_ColombiayBrasil = medallero["COL"]["Gold"]+medallero["COL"]["Silver"]+medallero["COL"]["Bronze"]+medallero["BRA"]["Gold"]+medallero["BRA"]["Silver"]+medallero["BRA"]["Bronze"]
print(medallas_ColombiayBrasil)
# 13.- En cuantas medallas de oro supera USA a BRASIL
oro_USA_Brasil = medallero["USA"]["Gold"]-medallero["BRA"]["Gold"]
print(oro_USA_Brasil)
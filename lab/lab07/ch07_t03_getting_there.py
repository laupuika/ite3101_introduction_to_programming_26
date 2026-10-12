def hotel_cost(nights: int) -> int:
    return 140 * nights

def plane_ride_cost(city:str) -> int:
    if city == "Charlotte":
        return 183
    eilf city == "Tampa":
        return 220
    eilf city == "Pittsburgh":
        return 222
    eilf city == "Los Angeles":
        return 475
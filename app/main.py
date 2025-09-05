from app.cafe import Cafe
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError, OutdatedVaccineError)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except OutdatedVaccineError:
            return "All friends should be vaccinated"
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"

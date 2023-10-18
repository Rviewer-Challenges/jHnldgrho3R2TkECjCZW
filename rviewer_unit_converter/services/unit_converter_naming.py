class UnitConverterNamingService:
    @staticmethod
    def get_encoded_conversion(from_unit, to_unit):
        return f"{from_unit}/{to_unit}", f"{to_unit}/{from_unit}"

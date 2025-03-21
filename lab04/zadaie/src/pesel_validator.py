class PeselValidator:
    def validate_format(pesel: str):
        if len(pesel) != 11:
            return False            
        return pesel.isdigit()

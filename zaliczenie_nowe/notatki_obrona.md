# Notatki do obrony projektu

## 1. Struktura projektu
- Projekt składa się z 3 głównych modułów:
  - `users.py` - zarządzanie użytkownikami
  - `reservation.py` - system rezerwacji
  - `reviews.py` - system recenzji
- Testy jednostkowe dla każdego modułu
- Pokrycie testami na poziomie >95%

## 2. Główne funkcjonalności

### System użytkowników (`users.py`)
- Zarządzanie użytkownikami (dodawanie, aktualizacja, usuwanie)
- Walidacja danych użytkownika (email, hasło)
- Powiązanie z systemem rezerwacji
- Zabezpieczenia przed usunięciem użytkownika z aktywnymi rezerwacjami

### System rezerwacji (`reservation.py`)
- Zarządzanie rezerwacjami pokoi
- Możliwość wyboru liczby łóżek (1-4)
- Walidacja dat rezerwacji
- Sprawdzanie dostępności pokoi
- Anulowanie rezerwacji

### System recenzji (`reviews.py`)
- Dodawanie recenzji (1-5 gwiazdek)
- Edycja i usuwanie recenzji
- Walidacja ocen i komentarzy
- Powiązanie recenzji z użytkownikami

## 3. Testy i jakość kodu

### Pokrycie testami
- `src/reservation.py`: 99%
- `src/reviews.py`: 100%
- `src/users.py`: 100%

### Rodzaje testów
- Testy podstawowych funkcjonalności
- Testy niepoprawnych danych wejściowych
- Testy przypadków brzegowych
- Testy pełnego cyklu życia obiektów
- Testy integracyjne między modułami

### Przykłady testowanych scenariuszy
1. Walidacja danych:
   - Poprawność emaili i haseł
   - Zakres ocen (1-5 gwiazdek)
   - Format dat rezerwacji
   - Liczba łóżek w pokoju

2. Przypadki brzegowe:
   - Próby usunięcia nieistniejących obiektów
   - Obsługa duplikatów
   - Aktualizacja tymi samymi danymi
   - Sekwencyjność ID po usunięciu

3. Integracja między modułami:
   - Powiązanie użytkowników z rezerwacjami
   - Usuwanie użytkowników z rezerwacjami
   - Zarządzanie recenzjami użytkowników

## 4. Dobre praktyki w kodzie

### Dokumentacja
- Wszystkie moduły mają dokładne docstringi
- Dokumentacja w języku polskim
- Opis klas i metod zgodny z Google Python Style Guide
- Szczegółowe opisy parametrów i zwracanych wartości

### Obsługa błędów
- Szczegółowe komunikaty błędów
- Walidacja wszystkich danych wejściowych
- Spójne nazewnictwo wyjątków
- Zabezpieczenie przed nieprawidłowym użyciem

### Struktura kodu
- Podział na logiczne moduły
- Spójny styl nazewnictwa
- Czytelne i zrozumiałe nazwy zmiennych i metod
- Odpowiednia organizacja testów

## 5. Możliwe pytania podczas obrony

1. Dlaczego zdecydowano się na taki podział na moduły?
   - Odpowiedź: Każdy moduł odpowiada za konkretną funkcjonalność, co zapewnia:
     - Łatwiejsze zarządzanie kodem
     - Lepszą testowalność
     - Możliwość niezależnego rozwoju każdego modułu

2. Jak zapewniono wysokie pokrycie testami?
   - Odpowiedź: Poprzez:
     - Systematyczne testowanie każdej funkcjonalności
     - Uwzględnienie przypadków brzegowych
     - Testowanie różnych scenariuszy użycia
     - Dokładne testy walidacji danych

3. Jakie są zabezpieczenia przed nieprawidłowym użyciem systemu?
   - Odpowiedź:
     - Szczegółowa walidacja wszystkich danych wejściowych
     - Zabezpieczenie przed usunięciem użytkownika z aktywnymi rezerwacjami
     - Kontrola poprawności dat i liczby łóżek
     - Sprawdzanie unikalności emaili

4. Jak można by rozszerzyć system w przyszłości?
   - Odpowiedź:
     - Dodanie systemu płatności
     - Implementacja systemu powiadomień
     - Rozszerzenie systemu recenzji o zdjęcia
     - Dodanie kategorii pokoi
     - Implementacja systemu rabatów

## 6. Wnioski końcowe

- Projekt spełnia wszystkie założone wymagania
- Wysoka jakość kodu potwierdzona testami
- Dokładna dokumentacja ułatwiająca rozwój
- Modułowa struktura umożliwiająca łatwe rozszerzanie
- Zabezpieczenie przed typowymi błędami użytkownika 
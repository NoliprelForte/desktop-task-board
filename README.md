Desktop Task Board
1. Opis projektu

Python Kanban Board to prosta aplikacja desktopowa napisana w języku Python. Program umożliwia zarządzanie zadaniami w formie tablicy kanban, podobnej do GitHub Projects, Trello lub Jira.

Aplikacja pozwala tworzyć zadania, przypisywać im statusy, przenosić je pomiędzy kolumnami oraz zapisywać dane lokalnie do pliku JSON. Projekt został wykonany z użyciem biblioteki customtkinter, która umożliwia tworzenie nowoczesnego interfejsu graficznego dla aplikacji desktopowych.

2. Cel projektu

Celem projektu było stworzenie prostej aplikacji desktopowej do organizacji zadań. Projekt miał również na celu przećwiczenie podstawowych zagadnień związanych z programowaniem obiektowym, tworzeniem GUI, obsługą zdarzeń użytkownika oraz zapisem danych do pliku.

Aplikacja może być używana do prostego zarządzania zadaniami w małych projektach.

3. Technologie

W projekcie wykorzystano:

Python,
customtkinter,
tkinter,
JSON,
pathlib,
programowanie obiektowe.
4. Główne funkcjonalności

Aplikacja umożliwia:

dodawanie nowych zadań,
wyświetlanie zadań w formie kafelków,
przypisywanie zadań do wybranych statusów,
zmianę statusu zadania za pomocą listy rozwijanej,
przeciąganie zadań pomiędzy kolumnami metodą drag and drop,
usuwanie zadań,
automatyczny zapis danych do pliku JSON,
automatyczne wczytywanie zapisanych zadań po ponownym uruchomieniu aplikacji.
5. Statusy zadań

W aplikacji dostępne są następujące statusy:

Backlog,
To do,
In progress,
Testing,
Done.

Każdy status jest przedstawiony jako osobna kolumna. Zadanie może znajdować się tylko w jednej kolumnie jednocześnie.

6. Struktura projektu

Struktura katalogów projektu wygląda następująco:

python-kanban-board/
│
├── main.py
│
├── ui/
│   ├── __init__.py
│   └── board.py
│
├── models/
│   ├── __init__.py
│   └── task.py
│
└── data/
    └── tasks.json
7. Opis plików
main.py

Plik main.py jest głównym punktem startowym aplikacji. Odpowiada za utworzenie obiektu aplikacji i uruchomienie głównej pętli programu.

ui/board.py

Plik board.py zawiera główną klasę odpowiedzialną za interfejs użytkownika. W tym pliku znajduje się logika tworzenia okna aplikacji, kolumn, kafelków zadań, obsługi przycisków, zmiany statusów oraz przeciągania zadań.

models/task.py

Plik task.py zawiera model zadania. Klasa Task przechowuje podstawowe informacje o zadaniu, czyli jego tytuł oraz aktualny status.

data/tasks.json

Plik tasks.json służy do zapisywania danych aplikacji. Zadania są zapisywane w formacie JSON, dzięki czemu po ponownym uruchomieniu programu użytkownik nadal widzi wcześniej utworzone zadania.

8. Model danych

Każde zadanie posiada dwa podstawowe pola:

title  - nazwa zadania
status - aktualny status zadania

Przykładowy zapis zadania w pliku JSON:

{
    "title": "Create basic app window",
    "status": "In progress"
}
9. Działanie aplikacji

Po uruchomieniu aplikacji wyświetlane jest główne okno programu. Na górze znajduje się pole tekstowe, w którym użytkownik może wpisać nazwę nowego zadania. Po kliknięciu przycisku Add task zadanie zostaje dodane do kolumny Backlog.

Każde zadanie jest wyświetlane jako osobny kafelek. Na kafelku znajduje się tytuł zadania, lista rozwijana ze statusem oraz przycisk Delete.

Status zadania można zmienić na dwa sposoby. Pierwszy sposób polega na wybraniu nowego statusu z listy rozwijanej. Drugi sposób polega na przeciągnięciu kafelka myszką do wybranej kolumny.

Po każdej zmianie dane są zapisywane do pliku tasks.json.

10. Obsługa drag and drop

Aplikacja posiada prostą obsługę przeciągania zadań pomiędzy kolumnami. Po kliknięciu i przytrzymaniu kafelka tworzony jest uproszczony podgląd przeciąganego zadania. Następnie użytkownik może przeciągnąć zadanie nad wybraną kolumnę i puścić przycisk myszy.

Po upuszczeniu zadania jego status jest aktualizowany, a dane zostają zapisane do pliku JSON.

11. Zapis i odczyt danych

Do zapisu danych wykorzystano plik JSON. Przy uruchamianiu aplikacji program sprawdza, czy istnieje plik tasks.json. Jeśli plik istnieje, aplikacja odczytuje z niego zapisane zadania. Jeśli plik nie istnieje, zostaje utworzony nowy pusty plik.

Dzięki temu użytkownik nie traci danych po zamknięciu programu.

12. Wymagania

Do uruchomienia aplikacji wymagane jest:

Python 3.10 lub nowszy,
biblioteka customtkinter.

Instalacja wymaganej biblioteki:

pip install customtkinter
13. Uruchomienie aplikacji

Aby uruchomić aplikację, należy przejść do głównego folderu projektu i wykonać polecenie:

python main.py

Aplikację można również uruchomić bezpośrednio z poziomu środowiska PyCharm, klikając prawym przyciskiem myszy na plik main.py i wybierając opcję Run.

14. Przykładowe zastosowanie

Aplikacja może być wykorzystana do:

organizacji prostych zadań projektowych,
planowania pracy nad projektem programistycznym,
nauki podstaw tworzenia aplikacji desktopowych,
nauki programowania obiektowego,
nauki zapisu i odczytu danych z pliku.
15. Możliwości dalszego rozwoju

Projekt można w przyszłości rozbudować o dodatkowe funkcje, takie jak:

edycja tytułu zadania,
dodawanie opisu zadania,
ustawianie priorytetu,
dodawanie terminów wykonania,
filtrowanie zadań,
wyszukiwanie zadań,
zapisywanie danych w bazie danych,
synchronizacja z GitHub Issues,
logowanie użytkownika,
eksport zadań do pliku.
16. Podsumowanie

Projekt Python Kanban Board jest prostą aplikacją desktopową do zarządzania zadaniami. Aplikacja posiada podstawowe funkcje typowe dla tablicy kanban, takie jak dodawanie zadań, zmiana statusu, przeciąganie pomiędzy kolumnami oraz zapis danych.

Projekt pokazuje praktyczne wykorzystanie języka Python do tworzenia aplikacji z interfejsem graficznym oraz prostego systemu przechowywania danych.

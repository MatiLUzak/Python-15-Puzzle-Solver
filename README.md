# Python-15-Puzzle-Solver

## 📌 Opis projektu

**Python-15-Puzzle-Solver** to aplikacja napisana w języku **Python**, która implementuje różne algorytmy do rozwiązywania łamigłówki **15-puzzle**. Projekt zawiera implementacje algorytmów takich jak **A\***, **BFS (Breadth-First Search)** oraz **DFS (Depth-First Search)**, a także moduł do wizualizacji grafu poszukiwań.

## 🛠 Wymagania

Aby uruchomić projekt, potrzebujesz:

- **Python 3.8** lub nowszy
- **pip** – menedżer pakietów dla Pythona

## 🚀 Instalacja

1. **Klonowanie repozytorium:**

   ```bash
   git clone https://github.com/MatiLUzak/python15puzzle.git
   cd python15puzzle
   ```

2. **Utworzenie i aktywacja środowiska wirtualnego (opcjonalnie, ale zalecane):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # lub
   venv\Scripts\activate  # Windows
   ```

3. **Instalacja zależności:**

   Upewnij się, że masz zainstalowane następujące biblioteki:

   - **networkx**
   - **matplotlib**

   Możesz je zainstalować za pomocą polecenia:

   ```bash
   pip install networkx matplotlib
   ```

## ▶️ Uruchomienie aplikacji

Aby uruchomić aplikację, użyj następującego polecenia:

```bash
python main.py
```

Domyślnie aplikacja używa algorytmu A\*. Możesz zmienić algorytm, edytując plik `main.py` i wybierając odpowiednią funkcję rozwiązującą.

## 📂 Struktura projektu

```
python15puzzle/
├── .idea/
├── build/
│   └── main/
├── data/
│   └── puzzle_initial_state.txt
├── dist/
├── astar.py
├── bfs.py
├── dfs.py
├── graf.py
├── main.py
├── main.spec
└── README.md
```

- **`astar.py`** – implementacja algorytmu A\* do rozwiązywania 15-puzzle.
- **`bfs.py`** – implementacja algorytmu BFS do rozwiązywania 15-puzzle.
- **`dfs.py`** – implementacja algorytmu DFS do rozwiązywania 15-puzzle.
- **`graf.py`** – moduł do wizualizacji grafu poszukiwań.
- **`main.py`** – główny skrypt uruchamiający aplikację.
- **`data/`** – katalog zawierający plik z początkowym stanem łamigłówki.

## ✍️ Autor

- **MatiLUzak** – [Profil GitHub](https://github.com/MatiLUzak)

## 📜 Licencja

Ten projekt jest licencjonowany na podstawie licencji MIT. Szczegóły znajdują się w pliku `LICENSE`.

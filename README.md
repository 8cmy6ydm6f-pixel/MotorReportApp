# Motor Report Generator

A robust, modular Python application designed to generate detailed Excel reports for motor testing data. This application processes data from various sources, including legacy `.xls` files, and produces comprehensive reports with noise analysis, comparisons, and graphical visualizations.

## 🚀 Features

-   **Automated Report Generation**: Generates professional Excel reports with summary, detailed SAP sheets, and comparison views.
-   **Legacy Support**: Seamlessly handles legacy `.xls` files (e.g., "Carichi Nominali") alongside modern formats.
-   **Noise Analysis**: Integrated processing of noise test data with dominant frequency analysis.
-   **Comparison Tools**: Compare multiple test labs or SAP codes with dedicated comparison sheets.
-   **Modern UI**: User-friendly GUI built with [Flet](https://flet.dev/), featuring dark mode support and responsive design.
-   **Modular Architecture**: Clean, maintainable codebase with separation of concerns (UI, Core Logic, Reporting).
-   **Cross-Platform**: Runs on Windows, macOS, and Linux.

## 🛠️ Tech Stack

-   **Language**: Python 3.8+
-   **GUI Framework**: [Flet](https://flet.dev/) (Flutter for Python)
-   **Data Processing**: `pandas`, `numpy`, `openpyxl`, `xlrd`
-   **Excel Generation**: `XlsxWriter`
-   **Testing**: `pytest`

## 📦 Installation

1.  **Clone the repository** (or download source):
    ```bash
    git clone <repository-url>
    cd MotorReportApp
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 🖥️ Usage

### Running the GUI
To start the application in your default web browser (or as a standalone window if configured):

```bash
python src/main.py
```

**Command Line Options:**
-   `--port <number>`: Specify the port to run the web server on (default: 8080).
-   `--no-browser`: Run in headless mode (useful for server deployments).

### Workflow
1.  **Setup**: Verify or configure the paths for your test data and registry files.
2.  **Search & Select**: Search for tests by SAP code or Test Number. Select the items you want to include in the report.
3.  **Configure**: Choose report options (e.g., include noise data, generate comparison sheets).
4.  **Generate**: Click "Generate Report" to create the Excel file.

## 📂 Project Structure

```
MotorReportApp/
├── assets/              # Static assets (logos, icons)
├── src/
│   ├── analysis/        # Data analysis logic (noise, images)
│   ├── config/          # Configuration management
│   ├── core/            # Core application logic (state, events)
│   ├── data/            # Data models and access layer
│   ├── reports/         # Excel report generation logic
│   ├── services/        # External services (file system, etc.)
│   ├── ui/              # Flet-based GUI components
│   ├── utils/           # Utility functions
│   └── main.py          # Application entry point
├── tests/               # Unit and integration tests
├── tools/               # Build and maintenance scripts
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## 🧪 Development

### Running Tests
Run the test suite using `pytest`:

```bash
pytest
```

### Building Executable
To build a standalone executable using PyInstaller:

```bash
python tools/build_app.py
```
The output will be in the `dist/` directory.

## 📄 License

All rights reserved.

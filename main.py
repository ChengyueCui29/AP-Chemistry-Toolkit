import tkinter as tk
import re

# ------------------ AUDITED DATA TABLES ------------------

atomic_masses = {
    "H": 1.008, "He": 4.0026, "Li": 6.94, "Be": 9.0122, "B": 10.81,
    "C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998, "Ne": 20.180,
    "Na": 22.990, "Mg": 24.305, "Al": 26.982, "Si": 28.085, "P": 30.974,
    "S": 32.06, "Cl": 35.45, "Ar": 39.948, "K": 39.098, "Ca": 40.078,
    "Sc": 44.956, "Ti": 47.867, "V": 50.942, "Cr": 51.996, "Mn": 54.938,
    "Fe": 55.845, "Co": 58.933, "Ni": 58.693, "Cu": 63.546, "Zn": 65.38,
    "Ga": 69.723, "Ge": 72.630, "As": 74.922, "Se": 78.971, "Br": 79.904,
    "Kr": 83.798, "Rb": 85.468, "Sr": 87.62, "Y": 88.906, "Zr": 91.224,
    "Nb": 92.906, "Mo": 95.95, "Tc": 98, "Ru": 101.07, "Rh": 102.906,
    "Pd": 106.42, "Ag": 107.868, "Cd": 112.414, "In": 114.818, "Sn": 118.710,
    "Sb": 121.760, "Te": 127.60, "I": 126.904, "Xe": 131.293, "Cs": 132.905,
    "Ba": 137.327, "La": 138.905, "Ce": 140.116, "Pr": 140.908, "Nd": 144.242,
    "Pm": 145, "Sm": 150.36, "Eu": 151.964, "Gd": 157.25, "Tb": 158.925,
    "Dy": 162.500, "Ho": 164.930, "Er": 167.259, "Tm": 168.934, "Yb": 173.045,
    "Lu": 174.967, "Hf": 178.49, "Ta": 180.948, "W": 183.84, "Re": 186.207,
    "Os": 190.23, "Ir": 192.217, "Pt": 195.084, "Au": 196.967, "Hg": 200.592,
    "Tl": 204.38, "Pb": 207.2, "Bi": 208.980, "Po": 209, "At": 210,
    "Rn": 222, "Fr": 223, "Ra": 226, "Ac": 227, "Th": 232.038,
    "Pa": 231.035, "U": 238.029, "Np": 237, "Pu": 244, "Am": 243,
    "Cm": 247, "Bk": 247, "Cf": 251, "Es": 252, "Fm": 257,
    "Md": 258, "No": 259, "Lr": 262, "Rf": 261, "Db": 268,
    "Sg": 269, "Bh": 270, "Hs": 277, "Mt": 278, "Ds": 281,
    "Rg": 282, "Cn": 285, "Nh": 286, "Fl": 289, "Mc": 289,
    "Lv": 293, "Ts": 294, "Og": 294
}

element_info = {
    "H": ("Hydrogen", 1), "He": ("Helium", 2), "Li": ("Lithium", 3), "Be": ("Beryllium", 4),
    "B": ("Boron", 5), "C": ("Carbon", 6), "N": ("Nitrogen", 7), "O": ("Oxygen", 8),
    "F": ("Fluorine", 9), "Ne": ("Neon", 10), "Na": ("Sodium", 11), "Mg": ("Magnesium", 12),
    "Al": ("Aluminum", 13), "Si": ("Silicon", 14), "P": ("Phosphorus", 15), "S": ("Sulfur", 16),
    "Cl": ("Chlorine", 17), "Ar": ("Argon", 18), "K": ("Potassium", 19), "Ca": ("Calcium", 20),
    "Sc": ("Scandium", 21), "Ti": ("Titanium", 22), "V": ("Vanadium", 23), "Cr": ("Chromium", 24),
    "Mn": ("Manganese", 25), "Fe": ("Iron", 26), "Co": ("Cobalt", 27), "Ni": ("Nickel", 28),
    "Cu": ("Copper", 29), "Zn": ("Zinc", 30), "Ga": ("Gallium", 31), "Ge": ("Germanium", 32),
    "As": ("Arsenic", 33), "Se": ("Selenium", 34), "Br": ("Bromine", 35), "Kr": ("Krypton", 36),
    "Rb": ("Rubidium", 37), "Sr": ("Strontium", 38), "Y": ("Yttrium", 39), "Zr": ("Zirconium", 40),
    "Nb": ("Niobium", 41), "Mo": ("Molybdenum", 42), "Tc": ("Technetium", 43), "Ru": ("Ruthenium", 44),
    "Rh": ("Rhodium", 45), "Pd": ("Palladium", 46), "Ag": ("Silver", 47), "Cd": ("Cadmium", 48),
    "In": ("Indium", 49), "Sn": ("Tin", 50), "Sb": ("Antimony", 51), "Te": ("Tellurium", 52),
    "I": ("Iodine", 53), "Xe": ("Xenon", 54), "Cs": ("Cesium", 55), "Ba": ("Barium", 56),
    "La": ("Lanthanum", 57), "Ce": ("Cerium", 58), "Pr": ("Praseodymium", 59), "Nd": ("Neodymium", 60),
    "Pm": ("Promethium", 61), "Sm": ("Samarium", 62), "Eu": ("Europium", 63), "Gd": ("Gadolinium", 64),
    "Tb": ("Terbium", 65), "Dy": ("Dysprosium", 66), "Ho": ("Holmium", 67), "Er": ("Erbium", 68),
    "Tm": ("Thulium", 69), "Yb": ("Ytterbium", 70), "Lu": ("Lutetium", 71), "Hf": ("Hafnium", 72),
    "Ta": ("Tantalum", 73), "W": ("Tungsten", 74), "Re": ("Rhenium", 75), "Os": ("Osmium", 76),
    "Ir": ("Iridium", 77), "Pt": ("Platinum", 78), "Au": ("Gold", 79), "Hg": ("Mercury", 80),
    "Tl": ("Thallium", 81), "Pb": ("Lead", 82), "Bi": ("Bismuth", 83), "Po": ("Polonium", 84),
    "At": ("Astatine", 85), "Rn": ("Radon", 86), "Fr": ("Francium", 87), "Ra": ("Radium", 88),
    "Ac": ("Actinium", 89), "Th": ("Thorium", 90), "Pa": ("Protactinium", 91), "U": ("Uranium", 92),
    "Np": ("Neptunium", 93), "Pu": ("Plutonium", 94), "Am": ("Americium", 95), "Cm": ("Curium", 96),
    "Bk": ("Berkelium", 97), "Cf": ("Californium", 98), "Es": ("Einsteinium", 99), "Fm": ("Fermium", 100),
    "Md": ("Mendelevium", 101), "No": ("Nobelium", 102), "Lr": ("Lawrencium", 103), "Rf": ("Rutherfordium", 104),
    "Db": ("Dubnium", 105), "Sg": ("Seaborgium", 106), "Bh": ("Bohrium", 107), "Hs": ("Hassium", 108),
    "Mt": ("Meitnerium", 109), "Ds": ("Darmstadtium", 110), "Rg": ("Roentgenium", 111), "Cn": ("Copernicium", 112),
    "Nh": ("Nihonium", 113), "Fl": ("Flerovium", 114), "Mc": ("Moscovium", 115), "Lv": ("Livermorium", 116),
    "Ts": ("Tennessine", 117), "Og": ("Oganesson", 118)
}

element_charges = {
    "H": "+1, -1", "He": "0", "Li": "+1", "Be": "+2", "B": "+3", "C": "+4, -4", "N": "-3", "O": "-2", "F": "-1",
    "Ne": "0",
    "Na": "+1", "Mg": "+2", "Al": "+3", "Si": "+4, -4", "P": "-3", "S": "-2", "Cl": "-1", "Ar": "0", "K": "+1",
    "Ca": "+2",
    "Sc": "+3", "Ti": "+4", "V": "+5", "Cr": "+3, +6", "Mn": "+2, +4, +7", "Fe": "+2, +3", "Co": "+2, +3", "Ni": "+2",
    "Cu": "+1, +2",
    "Zn": "+2", "Ga": "+3", "Ge": "+4", "As": "-3", "Se": "-2", "Br": "-1", "Kr": "0", "Rb": "+1", "Sr": "+2",
    "Y": "+3",
    "Zr": "+4", "Nb": "+5", "Mo": "+6", "Tc": "+7", "Ru": "+3", "Rh": "+3", "Pd": "+2", "Ag": "+1", "Cd": "+2",
    "In": "+3",
    "Sn": "+2, +4", "Sb": "+3, +5", "Te": "-2", "I": "-1", "Xe": "0", "Cs": "+1", "Ba": "+2", "La": "+3",
    "Ce": "+3, +4", "Pr": "+3",
    "Nd": "+3", "Pm": "+3", "Sm": "+3", "Eu": "+2, +3", "Gd": "+3", "Tb": "+3", "Dy": "+3", "Ho": "+3", "Er": "+3",
    "Tm": "+3",
    "Yb": "+3", "Lu": "+3", "Hf": "+4", "Ta": "+5", "W": "+6", "Re": "+4, +7", "Os": "+4, +8", "Ir": "+3, +4",
    "Pt": "+2, +4", "Au": "+1, +3",
    "Hg": "+1, +2", "Tl": "+1, +3", "Pb": "+2, +4", "Bi": "+3, +5", "Po": "+2, +4", "At": "-1", "Rn": "0", "Fr": "+1",
    "Ra": "+2", "Ac": "+3",
    "Th": "+4", "Pa": "+5", "U": "+3, +4, +5, +6", "Np": "+3, +4, +5, +6", "Pu": "+3, +4, +5, +6",
    "Am": "+3, +4, +5, +6",
    "Cm": "+3", "Bk": "+3, +4", "Cf": "+3", "Es": "+3", "Fm": "+3", "Md": "+2, +3", "No": "+2, +3", "Lr": "+3",
    "Rf": "+4", "Db": "+5",
    "Sg": "+6", "Bh": "+7", "Hs": "+8", "Mt": "N/A", "Ds": "N/A", "Rg": "N/A", "Cn": "+2", "Nh": "+1", "Fl": "+2",
    "Mc": "+3", "Lv": "N/A", "Ts": "-1", "Og": "0"
}

chem_constants = [
    ("Avogadro's (Na)", "6.022 x 10^23 mol⁻¹"),
    ("Gas Const (R)", "0.08206 L·atm/(mol·K)"),
    ("Gas Const (R)", "8.314 J/(mol·K)"),
    ("Planck's (h)", "6.626 x 10⁻³⁴ J·s"),
    ("Speed of Light (c)", "2.998 x 10⁸ m/s"),
    ("Electron Mass", "0.0005 amu"),
    ("Proton Mass", "1.007 amu"),
    ("Neutron Mass", "1.008 amu")
]

nonmetals = {"H", "C", "N", "O", "F", "P", "S", "Cl", "Se", "Br", "I", "He", "Ne", "Ar", "Kr", "Xe", "Rn"}


# ------------------ CORE TOOLKIT CLASS ------------------

class APChemToolkit:
    def __init__(self, root):
        self.root = root
        self.root.title("AP® Chemistry Toolkit V1.0")
        self.root.geometry("800x650")
        self.root.configure(bg="#f0f4f8")

        # HEADER
        header = tk.Frame(root, bg="#2c3e50", height=90)
        header.pack(fill="x", side="top")
        tk.Label(header, text="AP® Chemistry Toolkit V1.0", font=("Arial", 22, "bold"), bg="#2c3e50", fg="white").pack(
            pady=(15, 0))
        tk.Label(header, text="Created by: Chengyue Cui '29", font=("Arial", 9), bg="#2c3e50", fg="#bdc3c7").pack(
            pady=(0, 10))

        # MAIN CONTAINER
        self.main_container = tk.Frame(root, bg="#f0f4f8")
        self.main_container.pack(fill="both", expand=True)

        # SIDEBAR
        self.sidebar = tk.Frame(self.main_container, bg="#ffffff", width=220, bd=1, relief="solid")
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)
        self.sidebar.pack_propagate(False)

        # CONTENT
        self.content_frame = tk.Frame(self.main_container, bg="white", bd=1, relief="solid")
        self.content_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.create_nav_buttons()
        self.show_molar_mass_tool()

    def create_nav_buttons(self):
        nav_items = [
            ("Molar Mass", "#81c784", self.show_molar_mass_tool),
            ("Symbol Info", "#ce93d8", self.show_symbol_tool),
            ("Charge Lookup", "#ffb74d", self.show_charge_tool),
            ("Molecule/Compound Differentiator", "#64b5f6", self.show_diff_tool),
            ("Constants", "#cfd8dc", self.show_reference_tool),
        ]
        for txt, clr, cmd in nav_items:
            btn = tk.Button(self.sidebar, text=txt, font=("Arial", 9, "bold"), bg=clr, fg="black",
                            relief="flat", command=cmd, height=2, cursor="hand2", wraplength=180)
            btn.pack(fill="x", pady=5, padx=5)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    # --- TOOLS ---

    def show_molar_mass_tool(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Molar Mass Calculator", font=("Arial", 18, "bold"), bg="white",
                 fg="black").pack(pady=20)
        entry = tk.Entry(self.content_frame, font=("Arial", 14), width=20, fg="black", bd=2);
        entry.pack(pady=5)
        res_lbl = tk.Label(self.content_frame, text="Result: --", font=("Arial", 14), bg="white", fg="black");
        res_lbl.pack(pady=20)

        def run():
            m = self.calculate_molar_mass(entry.get().strip())
            res_lbl.config(text=f"Molar Mass: {m:.3f} g/mol" if m else "Error: Invalid Formula")

        tk.Button(self.content_frame, text="Calculate", font=("Arial", 12, "bold"), bg="#81c784", fg="black",
                  command=run).pack()

    def show_symbol_tool(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Detailed Symbol Info", font=("Arial", 18, "bold"), bg="white",
                 fg="black").pack(pady=20)
        entry = tk.Entry(self.content_frame, font=("Arial", 14), width=10, fg="black", bd=2);
        entry.pack()
        res_lbl = tk.Label(self.content_frame, text="", font=("Courier", 12), bg="white", justify="left", fg="black")
        res_lbl.pack(pady=20)

        def run():
            s = entry.get().strip().capitalize()
            if s in element_info:
                name, z = element_info[s];
                m = atomic_masses[s]
                info = (f"Symbol: {s}\nName: {name}\nAtomic Number: {z}\nMass: {m} amu\n"
                        f"Protons: {z}\nNeutrons: {round(m) - z}\nElectrons: {z}")
                res_lbl.config(text=info)
            else:
                res_lbl.config(text="Error: Symbol not found.")

        tk.Button(self.content_frame, text="Identify Symbol", font=("Arial", 12, "bold"), bg="#ce93d8", fg="black",
                  command=run).pack()

    def show_charge_tool(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Element Charge Lookup", font=("Arial", 18, "bold"), bg="white",
                 fg="black").pack(pady=20)
        entry = tk.Entry(self.content_frame, font=("Arial", 14), width=10, fg="black");
        entry.pack()
        res_lbl = tk.Label(self.content_frame, text="Common Charge: --", font=("Arial", 14, "bold"), bg="white",
                           fg="black");
        res_lbl.pack(pady=20)

        def run():
            s = entry.get().strip().capitalize()
            res_lbl.config(text=f"Common Charge: {element_charges.get(s, 'N/A')}")

        tk.Button(self.content_frame, text="Get Charge", font=("Arial", 12, "bold"), bg="#ffb74d", fg="black",
                  command=run).pack()

    def show_diff_tool(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Molecule/Compound Differentiator", font=("Arial", 16, "bold"), bg="white",
                 fg="black").pack(pady=20)
        entry = tk.Entry(self.content_frame, font=("Arial", 14), width=20, fg="black")
        entry.pack()
        res_lbl = tk.Label(self.content_frame, text="Classification: --", font=("Arial", 14), bg="white", fg="black")
        res_lbl.pack(pady=20)

        def run():
            formula = entry.get().strip()
            elements = set(re.findall(r'([A-Z][a-z]?)', formula))
            if not elements:
                res_lbl.config(text="Classification: Unknown")
                return

            metals_in = elements - nonmetals
            nonmetals_in = elements & nonmetals

            if metals_in and nonmetals_in:
                res = "Ionic Bond"
            elif nonmetals_in and not metals_in:
                res = "Covalent Bond"
            elif metals_in and not nonmetals_in:
                res = "Metallic Bond"
            else:
                res = "Unknown"

            res_lbl.config(text=f"Classification: {res}")

        tk.Button(self.content_frame, text="Differentiate", font=("Arial", 12, "bold"), bg="#64b5f6", fg="black",
                  command=run).pack()

    def show_reference_tool(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Key AP® Chemistry Constants", font=("Arial", 18, "bold"), bg="white",
                 fg="black").pack(pady=20)
        table_container = tk.Frame(self.content_frame, bg="#2c3e50", padx=1, pady=1)
        table_container.pack()
        for i, (name, val) in enumerate(chem_constants):
            tk.Label(table_container, text=name, bg="#ffffff", fg="black", width=22, anchor="w",
                     font=("Arial", 10, "bold"), padx=10).grid(row=i, column=0, sticky="nsew", padx=1, pady=1)
            tk.Label(table_container, text=val, bg="#ffffff", fg="black", width=28, anchor="w", font=("Arial", 10),
                     padx=10).grid(row=i, column=1, sticky="nsew", padx=1, pady=1)



    # --- LOGIC ---

    def calculate_molar_mass(self, formula):
        def parse(formula):
            stack = []
            pattern = r'([A-Z][a-z]?)(\d*)|(\()|(\))(\d*)'
            for token in re.finditer(pattern, formula):
                elem, num, open_p, close_p, close_num = token.groups()
                if elem:
                    stack.append((elem, int(num) if num else 1))
                elif open_p:
                    stack.append('(')
                elif close_p:
                    temp, mult = [], int(close_num) if close_num else 1
                    while stack and stack[-1] != '(': temp.append(stack.pop())
                    if stack: stack.pop()
                    for item in reversed(temp): stack.append((item[0], item[1] * mult))
            res = {}
            for e, c in stack: res[e] = res.get(e, 0) + c
            return res

        try:
            counts = parse(formula)
            return sum(atomic_masses[e] * c for e, c in counts.items())
        except:
            return None


if __name__ == "__main__":
    root = tk.Tk()
    app = APChemToolkit(root)
    root.mainloop()

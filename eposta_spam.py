# -*- coding utf-8 -*-
"""
===============================================================================
MINI MACHINE LEARNING PROJESI - E-POSTA SPAM TAHMINI
===============================================================================

Bu proje, kullanicinin disaridan bir CSV dosyasi secmesini ve bu veri uzerinde
console/terminal araciligiyla temel Machine Learning adimlarini uygulamasini
saglar.

PROJENIN AMACI
--------------
Bir e-postanin SPAM olup olmadigini tahmin eden bir Classification uygulamasi
olusturmaktir.

ORNEK CSV SUTUNLARI
-------------------
kelime_sayisi
link_sayisi
buyuk_harf_orani
supheli_kelime_sayisi
gonderici_puani
ek_var
spam

Ornek:
kelime_sayisi,link_sayisi,buyuk_harf_orani,supheli_kelime_sayisi,gonderici_puani,ek_var,spam
120,0,0.05,0,92,0,0
45,6,0.72,5,18,1,1

spam:
    0 -> Normal e-posta
    1 -> Spam e-posta

ONEMLI
------
Bu proje icin hedef sutun otomatik olarak 'spam' kabul edilir.
'spam' disindaki sutunlar feature olarak kullanilir.

Program sayisal ve kategorik sutunlari otomatik algilar.
"""

# -------------------------------------------------------------------------------------
# os / pathlib:

# pandas:

# numpy:

# matplotlib:

# scikit-learn

"""

"""

import os
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Appstate: new*
    def __init__(self): new*
    self.csv_path: Optional[Path] = None
    self.raw_df: Optional[pd.DataFrame] = None
    self.df: Optional[pd.DataFrame] = None

    self.target_column: Optional[str] = None
    self.target_column: List[str] = None

    self.model_results: List[Dict[str, Any]] = []

    self.preprocessing_completed: bool = False
    self.current_step: int = 1

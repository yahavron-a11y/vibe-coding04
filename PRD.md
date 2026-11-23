# מסמך דרישות מוצר (PRD) – CivicShield AI (מגן התודעה הלאומי)
## Product Requirements Document: National Multi-Agent Information Integrity & Democratic Resilience System (Assignment 2 Preliminary Report)

---

### 1. מבוא וחזון המוצר (Introduction & Vision)
פרויקט **CivicShield AI ("מגן התודעה הלאומי")** מהווה דוח מכין (Preliminary Design & Feasibility Report) מקיף בהיקף יעד של כ-40 עמודים (טווח מקובל: 37–45 עמודים; **תוצר סופי מאומת: 39 עמודי PDF — דף שער + 38 עמודים ממוספרים במספור ערבי רציף, 935,647 bytes, 0 שגיאות LaTeX**), המוגש כמענה למכרז ממשלתי ברמת תכנון לאומית בסביבת ענן ממשלתי ריבוני (**Sovereign Cloud / Nimbus**).
הפרויקט מגשר בין **מדעי המדינה**, **חקר התקשורת הפוליטית**, **המשפט החוקתי (הישראלי והאירופי)** ו**הנדסת מערכות רב-סוכניות מבוססות בינה מלאכותית (Multi-Agent AI Systems)**.

החזון של CivicShield AI הוא להגן על טוהר ההליך הדמוקרטי, אמון הציבור במוסדות המדינה והספרה הציבורית מפני מבצעי השפעה זרים (**FIMI — Foreign Information Manipulation and Interference**), פעילות בלתי אותנטית מתואמת (**CIB — Coordinated Inauthentic Behavior**), נחילי בוטים אוטונומיים, מסגור תקשורתי מקטב וזיופי עומק (**Deepfakes**) בזמן אמת — תוך שמירה קפדנית על חופש הביטוי החוקתי, עקרון *Behavior Not Speech*, פיקוח אנושי (*Human-in-the-Loop*), ופרטיות מובנית (*Privacy by Design*).

בניגוד לגישות מסורתיות של בדיקת עובדות בדיעבד (*Reactive Fact-Checking*), CivicShield AI מציגה פרדיגמה פרואקטיבית של **חיסון תודעתי (*Cognitive Prebunking*)** בשילוב מנוע תזמור רב-סוכנים (`Multi-Agent Orchestration Hub`), מנגנוני `Zero-Trust Guardrails`, אימות מבוסס מקורות (`Grounded RAG`), ולולאת בקרה מובנית (`Critic-in-the-Loop`).

---

### 2. יעדי הפרויקט (Core Objectives)
1. **אינטגרציה אקדמית בין תקשורת, מדעי המדינה ומשפט חוקתי:** עיגון הארכיטקטורה הטכנולוגית בתיאוריות מבוססות כגון קביעת סדר היום (*Agenda Setting*), מסגור (*Framing*), ספירלת השתיקה (*Spiral of Silence*), תיבות תהודה (*Echo Chambers*), תיאוריית החיסון (*Inoculation Theory*), דמוקרטיה מתגוננת (*Defensive Democracy*), ורגולציה ישראלית ואירופית (`INCD`, תקנות הגנת הפרטיות התשע"ז–2017, `DSA`).
2. **עמידה מלאה בדרישות מטלה 2 (דוח מכין):**
   - **היקף המסמך:** 37–45 עמודים (יעד אופטימלי: 40 עמודים) מעוצבים בסגנון ספר/דוח הנדסי-אקדמי.
   - **ארכיטקטורת LaTeX מודולרית (בתיקיית `agents/master/`):** מחלקת מסמך ייעודית ומקורית (`agents/master/civicshield.cls`) עם **מספור עמודים ערבי רציף** (דף שער לא ממוספר, ללא ספרות רומיות ב-Front Matter), קובץ ראשי (`agents/master/main.tex`), סקריפט בנייה וסנכרון אוטומטי (`agents/master/build.ps1`, `.latexmkrc`), מאגר ביבליוגרפיה (`agents/master/references.bib`), והפרדה לקובץ `.tex` נפרד עבור כל אחד מ-5 פרקי הדוח בתיקיית `agents/master/chapters/`.
   - **מנוע סימולציות Python ברמת Production ומימוש ייחוס בפרק 4:** 5 גרפים מדעיים מקוריים הנוצרים דטרמיניסטית על ידי מנוע סימולציות מוקשח (`agents/master/scripts/generate_figures.py` עם type hints קשיחים, ולידציה, טיפול בשגיאות ו-`numpy`/`matplotlib`), מוטמעים וקטורית כ-PDF בדוח וכ-PNG ב-`README.md` (`agents/master/figures/fig4_1..fig4_5`), לצד מימוש ייחוס הנדסי ב-Python המשולב ישירות בפרק 4 (`chapters/ch04_simulations.tex`).
   - **איורים וקטוריים בקוד TikZ בלבד:** אפס תמונות חיצוניות מהאינטרנט; כל תרשימי הארכיטקטורה, הזרימה ורכזת הסוכנים כתובים בקוד TikZ מקורי בתוך קובצי ה-LaTeX.
   - **עיצוב וויזואליזציה מקוריים:** פלטת צבעים ממלכתית-הנדסית (`CSNavy`, `CSTeal`, `CSGold`, `CSAlert`), כותרות פרקים ועמודים מותאמות, ותיבות תוכן ממוסגרות (`tcolorbox`).
3. **תזמור צוות סוכנים (Multi-Agent Orchestration — Lecture 4):** יישום מתודולוגיית ועדת מומחים של 5 סוכנים (`master`, `theory`, `architect`, `simulator`, `redteam`) עם תיקיות עבודה נפרדות תחת `agents/`, פרוטוקול `team.json`, ו-**Dual RedTeam → ReAct Audit Loop** לבדיקת חוקתיות, אנטי-צנזורה, עקביות מספרית ואיכות BiDi.
4. **התאמה מלאה לסביבת עברית ו-BiDi:** קימפול ב-`lualatex` + `bibtex` עם תמיכה תקנית מלאה בעברית מימין לשמאל (RTL) ובידוד מונחים ומשוואות בלועזית (LTR/BiDi).

---

### 3. דרישות המוצר והמפרט הפונקציונלי (System & Report Specifications)
#### א. דרישות המערכת המתוכננת (CivicShield AI)
- **ניטור וזיהוי (FR):** קליטת זרמי מידע ציבוריים בזמן אמת, זיהוי התנהגות מתואמת בלתי אותנטית (`CIB`) ומבצעי `FIMI`, ואיחוד ראיות רב-מודאלי לאיתור מניפולציות ו-`Deepfakes`.
- **מודלים מתמטיים וחיזוי:** הרצת מודל הדבקה תודעתית (`SIRI ODE`), דינמיקת דעות וקיטוב (`Hegselmann-Krause`), איחוד ראיות בייסיאני (`Bayesian Fusion`), תכנון קיבולת תורים (`M/M/c Erlang-C`), ומודל כלכלי חמש-שנתי (`5-Year ROI`).
- **חוקתיות, אבטחה ואנטי-צנזורה:** אכיפת *Behavior Not Speech* (אפס צנזורה אוטומטית), פיקוח אנושי ושיפוטי (`Human-in-the-Loop` / `Critic-in-the-Loop`), בקרת גישה `ABAC`, ותאימות מלאה לריבונות נתונים ללא הוצאת `PII` מגבולות ישראל.
- **דרישות לא-פונקציונליות (NFR):** עמידה בהשהיות זמן אמת תחת עומסי שיא, זמינות גבוהה בענן ממשלתי (`Nimbus` / `On-Premise Air-Gapped`), ושקיפות מלאה לביקורת.

#### ב. מבנה פרקי הדוח המכין ובעלות הסוכנים (Front Matter + 5 פרקים)
| חלק / פרק | קובץ (תחת `agents/master/`) | בעלים | יעד עמודים | אלמנטים מרכזיים |
| :--- | :--- | :---: | :---: | :--- |
| **Front Matter** | `main.tex`, `civicshield.cls` | `architect` / `master` | ~5 | דף שער, בקרת מסמך, תקציר מנהלים, תוכן עניינים ומילון מונחים |
| **פרק 1** | `chapters/ch01_vision.tex` | `theory` | ~6 | תמונת האיומים הלאומית, חזון אסטרטגי ומפת דרכים תלת-שלבית |
| **פרק 2** | `chapters/ch02_theory_law.tex`, `references.bib` | `theory` | ~8 | תקשורת פוליטית, מדעי המדינה ומשפט חוקתי (ישראל ו-EU) |
| **פרק 3** | `chapters/ch03_architecture.tex` | `architect` | ~9 | ארכיטקטורה 5-שכבתית, `Multi-Agent Hub`, מטריצות `FR/NFR` ואיורי TikZ |
| **פרק 4** | `chapters/ch04_simulations.tex` | `simulator` | ~8 | מידול מתמטי, 5 גרפי Python (`fig4_1`–`fig4_5`) וניתוח `5-Year ROI` |
| **פרק 5** | `chapters/ch05_safeguards_audit.tex` | `redteam` | ~4 | הגנות חוקתיות, אנטי-צנזורה, ביקורת `RedTeam -> ReAct` ו-QA |

---

### 4. מדדי קבלה ואימות (Acceptance Criteria — סטטוס סופי: הושלם ואומת ✅)
1. קובץ ה-PDF הסופי בשורש הפרויקט (`CivicShield_AI_Preliminary_Report.pdf`) מתקמפל ומסונכרן אוטומטית מ-`agents/master/main.pdf` בכל הרצת `agents/master/build.ps1` או `latexmk` ללא שגיאות (`LATEX_ERRORS_COUNT: 0`, `RMFAMILY_MATH_ERRORS_COUNT: 0`, `UNDEF_REFS: 0`, `UNDEF_CITES: 0`) ועם מספור עמודים ערבי רציף (אפס ספרות רומיות).
2. אורך המסמך עומד בטווח **37–45 עמודים** (בפועל: **39 עמודי PDF** / 38 עמודים ממוספרים, `935,647` bytes) מעוצבים ברמת מכרז ממשלתי.
3. **איכות פריסה, מילון מונחים ו-BiDi QA:** הושלמו תיקוני ה-BiDi QA של `redteam` ותיקוני הפריסה של `architect` — מילון המונחים מוצג במלואו בעמוד אחד (ללא פיצול עמודים 8–9), ללא כותרות סעיפים יתומות (`needspace` + `\raggedbottom`), ללא תיבות הדגשה מפוצלות וללא עמודי זנב יתומים.
4. כל 5 הגרפים מיוצרים על ידי מנוע ה-Python המחוזק `agents/master/scripts/generate_figures.py` ללא שגיאות ונכללים בדוח וב-`README.md`, ופרק 4 כולל מימוש ייחוס ב-Python ברמת Production.
5. כל האיורים ההנדסיים מבוססי TikZ בלבד ועוברים אימות אוטומטי באמצעות `py agents/master/scripts/verify_report.py`.
6. קיום תיעוד פרויקט מלא ומעודכן בשורש המאגר כולל `README.md`, `PRD.md`, `PLAN.md`, `TODO.md`, `team.json` ותיקיות הסוכנים תחת `agents/` — מעודכן בכל `git push`.
